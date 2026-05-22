from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data="small_dataset/data.yaml",
    epochs=1,
    imgsz=224,
    batch=1,
    workers=0,
    device="cpu"
)
