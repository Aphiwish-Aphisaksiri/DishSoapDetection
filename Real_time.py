from ultralytics import YOLO

model = YOLO('runs\\detect\\train27\\weights\\best.pt')
results = model(0, show=True)