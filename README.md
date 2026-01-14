# Automated Syringes And Vials — Counting System

This repository contains code and a small dataset for detecting and counting syringes and vials using YOLO models.

Contents
- `Syringes And Vials/` — dataset (train/valid/test) and labels
- Notebooks: `yolo v7.ipynb`, `yolo v8.ipynb`, `yolo v9.ipynb`, `yolov8l.ipynb`
- `streamapp.py` — example streaming/app script

Quick start
1. Clone the repo.
2. Create a Python virtual environment and install dependencies (if you have a `requirements.txt`).

Example:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt  # if present
```

Notes
- Large dataset files (images, videos) are included in the `Syringes And Vials` folder; consider using Git LFS if you want to track large binaries efficiently.
- If you want, I can add a `requirements.txt`, more detailed usage instructions, or CI that runs model tests.

Recommended model
 - **YOLOv8** is recommended for this project (balance of accuracy and ease-of-use).
 - A demo inference script is included: `yolov8_inference.py` (uses the `ultralytics` package).

Quick inference example

```powershell
# Create and activate virtual env
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt

# Run the YOLOv8 demo on the demo video
python yolov8_inference.py --source demo.mp4 --model yolov8l.pt --output runs/detect
```

Notes on models:
 - Use `yolov8n.pt` for fastest, `yolov8l.pt` or `yolov8x.pt` for higher accuracy.
 - The script will save annotated results under `runs/detect/yolov8_demo`.
