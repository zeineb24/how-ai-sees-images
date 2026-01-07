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
## How to run locally

### Install dependencies
```bash
pip install -r requirements.txt
```
### Start the server
```bash
uvicorn app:app --reload
```
### Open the interactive API documentation
```arduino
http://127.0.0.1:8000/docs
```
---
## Available endpoints
### GET /health

Simple health check to verify that the server is running.

### POST /analyze-image

Upload an image and receive basic visual analysis
(brightness, contrast, lighting).

---
## What this project demonstrates

Building a clean backend API with FastAPI

Handling image uploads safely

Performing basic computer vision analysis

Returning structured, interpretable JSON outputs

Writing simple and readable backend code

This project serves as a foundation that can be easily extended.
---
## Possible extensions

Add a lightweight image classifier

Compare AI perception vs human description

Highlight uncertainty in low-quality images

Extend to multimodal analysis (image + text)
---
# License

MIT License
