from fastapi import FastAPI, File, UploadFile, HTTPException
from PIL import Image
import numpy as np
import io

app = FastAPI(title="How AI Sees Images (Basic)")

def compute_brightness_contrast(img: Image.Image) -> dict:
    gray = img.convert("L")
    arr = np.array(gray).astype(np.float32)

    brightness = float(arr.mean())   # 0 to 255
    contrast = float(arr.std())      # higher = more contrast

    return {"brightness": brightness, "contrast": contrast}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze-image")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type or not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Please upload an image file.")

    data = await file.read()

    try:
        img = Image.open(io.BytesIO(data))
        img.load()
    except Exception:
        raise HTTPException(status_code=400, detail="Could not read the image.")

    stats = compute_brightness_contrast(img)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "format": img.format,
        "mode": img.mode,
        "width": img.width,
        "height": img.height,
        "stats": stats,
    }
