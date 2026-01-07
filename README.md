# how-ai-sees-images

A beginner-friendly computer vision API that shows **how an AI system perceives an image**, using simple visual signals such as brightness and contrast.

This project is intentionally simple and focuses on **interpretability** rather than complex models.

---

## Why this project exists

Most AI demos jump directly to predictions.  
This project takes a step back and answers a more basic question:

> What visual information does an AI see before making a decision?

By exposing low-level image properties, this API helps understand:

- lighting conditions
- image quality
- potential sources of uncertainty for vision models

---

## What the API does

You upload an image, and the API returns:

- image metadata (size, format)
- brightness level
- contrast level
- a simple interpretation of lighting conditions

Example output:

```json
{
  "width": 640,
  "height": 427,
  "stats": {
    "brightness": 120.6,
    "contrast": 66.8,
    "lighting": "Normal"
  }
}
```

## Tech stack

- Python
- FastAPI
- Pillow
- NumPy
- Uvicorn

---
