import torch
import clip
from PIL import Image
import io

model, preprocess = clip.load("ViT-B/32")

def create_clip_embedding(image_bytes: bytes, text: str):
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image_tensor = preprocess(image).unsqueeze(0)
    text_tokens = clip.tokenize([text])
    with torch.no_grad():
        image_feat = model.encode_image(image_tensor)
        text_feat = model.encode_text(text_tokens)
        combined = (image_feat + text_feat) / 2
    return combined[0].tolist()