"""
YOLOv8 inference demo script

Usage:
  python yolov8_inference.py --source demo.mp4 --model yolov8l.pt --output runs/detect

Requires `ultralytics` (listed in `requirements.txt`).
"""
import argparse
import os
from ultralytics import YOLO


def parse_args():
    p = argparse.ArgumentParser(description="YOLOv8 demo inference")
    p.add_argument("--model", default="yolov8l.pt", help="Model to use (e.g. yolov8n.pt, yolov8l.pt)")
    p.add_argument("--source", default="demo.mp4", help="Image/video/source path or camera index")
    p.add_argument("--output", default="runs/detect", help="Output folder for saved results")
    return p.parse_args()


def main():
    args = parse_args()
    os.makedirs(args.output, exist_ok=True)

    print(f"Loading model: {args.model}")
    model = YOLO(args.model)

    print(f"Running inference on: {args.source}")
    # `save=True` writes annotated results to disk
    model.predict(source=args.source, save=True, project=args.output, name="yolov8_demo", exist_ok=True)

    out_dir = os.path.join(args.output, "yolov8_demo")
    print(f"Results saved to: {out_dir}")


if __name__ == "__main__":
    main()
