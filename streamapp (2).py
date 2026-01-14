import streamlit as st
from PIL import Image, ImageDraw, ImageFont
#pip install ultralytics

from ultralytics import YOLO

model_path = r"C:\Users\GAYAL\OneDrive\Desktop\GAYAL\best.pt"
model = YOLO(model_path)

def draw_boxes(image, results):
    """Draws bounding boxes on the image based on model's results."""
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    object_counts = {}

    for result in results:
        if hasattr(result, 'boxes'):
            for box in result.boxes:
                bbox = box.xyxy[0].tolist()
                conf = box.conf.item()
                cls_idx = int(box.cls.item())
                cls_name = result.names[cls_idx]

                xmin, ymin, xmax, ymax = bbox
                draw.rectangle([xmin, ymin, xmax, ymax], outline="red", width=2)
                label = f"{cls_name} {conf:.2f}"
                draw.text((xmin, ymin - 10), label, fill="red", font=font)

                if cls_name in object_counts:
                    object_counts[cls_name] += 1
                else:
                    object_counts[cls_name] = 1

    return image, object_counts

def detect_and_display(image):
    pil_image = Image.open(image)
    results = model(pil_image, imgsz=640)
    pil_image_resized = pil_image.resize((640, 640))  # Corrected resize function call

    results_img, object_counts = draw_boxes(pil_image_resized, results)
    return results_img, object_counts

def main():
    st.title('YOLO Object Detection')
    st.write('Upload an image, and the YOLO model will detect objects in it, displaying their counts and bounding boxes.')

    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Image', use_column_width=True)
        result_image, object_counts = detect_and_display(uploaded_file)
        st.image(result_image, caption='Result Image with Detected Objects', use_column_width=True)
        
        st.write("Detected objects and their counts:")
        pipe_counts = {}  # Dictionary to store pipe counts for each class
        for obj, count in object_counts.items():
            if 'pipe' in obj.lower():  # Check if the class name contains 'pipe'
                pipe_counts[obj] = count
            st.write(f"- {obj}: {count}")
        
        st.write("\nPipe detection summary:")
        for obj, count in pipe_counts.items():
            st.write(f"- {obj}: {count}")

if __name__ == "__main__":
    main()
