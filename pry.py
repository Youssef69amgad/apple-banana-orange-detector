from ultralytics import YOLO



model = YOLO('yolov8s.pt')  


model.train(
    data="conf.yaml",
    augment=True,           
    mosaic=True,            
    mixup=0.1,              
    hsv_h=0.015,            
    hsv_s=0.7,              
    hsv_v=0.4,              
    flipud=0.0,             
    fliplr=0.5,             
    copy_paste=0.1,  
    epochs=50,
    imgsz=640,
    batch=16
)

