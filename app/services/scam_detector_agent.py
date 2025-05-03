from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from typing import List, Optional
from jsonschema import validate
import json
from app.models.anomaly import userPosts, Post, AnomalyResponse
from app.services import agent_tools

class ScamState(dict):
    user_id: str
    posts: List[Post]
    suspicious_reasons: List[str]
    suspicious_score: int
    llm_analysis: Optional[dict]

LLM_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "is_suspicious": {"type": "boolean"},
        "confidence": {"type": "number", "minimum": 0, "maximum": 1},
        "suspicious_indicators": {"type": "array", "items": {"type": "string"}},
        "explanation": {"type": "string"},
        "recommendation": {"enum": ["flag", "monitor", "ignore"]}
    },
    "required": ["is_suspicious", "confidence", "suspicious_indicators", "explanation", "recommendation"]
}

llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.1)

def validate_llm_response(response: dict) -> bool:
    try:
        validate(instance=response, schema=LLM_RESPONSE_SCHEMA)
        return True
    except Exception as e:
        print(f"LLM response validation failed: {e}")
        return False

def analyze_user_with_llm(posts: List[Post]) -> dict:
    formatted_posts = [
        {
            "id": post.id,
            "text": post.description or "",
            "timestamp": str(post.timestamp),
            "date": post.date,
            "has_image": bool(post.image_url)
        }
        for post in posts[:5]
    ]
    system_prompt = """You are an expert fraud and scam detector for social media platforms.
Analyze these posts to identify potential scammers, spammers, or fraudulent users.
Look for suspicious patterns such as inconsistent story details, urgent personal information requests, too-good-to-be-true offers, pressure to act quickly, unusual reward mentions, and inconsistent posting style.
Return a JSON with:
{
  "is_suspicious": true/false,
  "confidence": 0.1-1.0,
  "suspicious_indicators": ["list of specific suspicious elements found"],
  "explanation": "detailed explanation of your reasoning",
  "recommendation": "flag" or "monitor" or "ignore"
}"""
    user_prompt = f"POSTS:\n{json.dumps(formatted_posts, indent=2)}\nProvide your analysis in the JSON format specified."
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]
    try:
        response = llm.invoke(messages)
        content = response.content
        start_idx = content.find('{')
        end_idx = content.rfind('}') + 1
        if start_idx >= 0 and end_idx > start_idx:
            json_str = content[start_idx:end_idx]
            analysis = json.loads(json_str)
            if not validate_llm_response(analysis):
                raise ValueError("Invalid LLM response format")
            return analysis
        else:
            raise ValueError("Could not extract JSON from LLM response")
    except Exception as e:
        print(f"Error in LLM analysis: {e}")
        return {
            "is_suspicious": False,
            "confidence": 0.0,
            "suspicious_indicators": ["Analysis failed"],
            "explanation": f"Error analyzing user: {str(e)}",
            "recommendation": "monitor"
        }

def scam_detector_agent(user_posts: userPosts) -> AnomalyResponse:
    suspicious_reasons = []
    suspicious_score = 0

    # Run tools (all expect List[Post])
    if (reason := agent_tools.check_duplicate_images(user_posts.posts)):
        suspicious_reasons.append(reason)
        suspicious_score += 1
    if (reason := agent_tools.check_links(user_posts.posts)):
        suspicious_reasons.append(reason)
        suspicious_score += 1
    if (reason := agent_tools.check_post_frequency(user_posts.posts)):
        suspicious_reasons.append(reason)
        suspicious_score += 1

    # LLM analysis
    analysis = analyze_user_with_llm(user_posts.posts)
    if analysis.get("is_suspicious", False):
        for indicator in analysis.get("suspicious_indicators", []):
            suspicious_reasons.append(indicator)
            suspicious_score += 1

    flagged = suspicious_score >= 3
    return AnomalyResponse(
        flagged=flagged,
        suspicious_score=suspicious_score,
        suspicious_reasons=suspicious_reasons
    )
