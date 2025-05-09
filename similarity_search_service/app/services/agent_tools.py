import requests
from PIL import Image
import io
import imagehash
import re
from collections import Counter
from typing import List, Optional
from app.models.anomaly import Post
from dotenv import load_dotenv
import os

load_dotenv()
PROXY_API_KEY = os.environ["PROXY_API_KEY"]
PROXY_BASE_URL = os.environ["PROXY_BASE_URL"]

def check_duplicate_images(posts: List[Post]) -> Optional[str]:
    """Detect if the user has posted the same image more than once (by perceptual hash)."""
    seen_hashes = {}
    for post in posts:
        if post.image_url:
            blob_name = str(post.image_url).split("/")[-1]
            download_url = f"{PROXY_BASE_URL}/download/{blob_name}"
            try:
                headers = {"x-api-key": PROXY_API_KEY}
                resp = requests.get(download_url, headers=headers)
                resp.raise_for_status()
                image = Image.open(io.BytesIO(resp.content))
                img_hash = str(imagehash.phash(image))
                if img_hash in seen_hashes:
                    return f"Duplicate image detected in posts {seen_hashes[img_hash]} and {post.id}"
                seen_hashes[img_hash] = post.id
            except Exception as e:
                print(f"Image check error for {blob_name}: {e}")
    return None

def check_links(posts: List[Post]) -> Optional[str]:
    """Detect if any post contains an external link."""
    link_pattern = re.compile(r"(https?://\S+|www\.\S+)", re.IGNORECASE)
    for post in posts:
        if post.description and link_pattern.search(post.description):
            return f"External link detected in post {post.id}"
    return None

def check_post_frequency(posts: List[Post]) -> Optional[str]:
    """Detect if user made 3 or more posts in a single day."""
    date_counts = Counter(post.date for post in posts if post.date)
    for date, count in date_counts.items():
        if count >= 3:
            return f"High posting frequency: {count} posts on {date}"
    return None
