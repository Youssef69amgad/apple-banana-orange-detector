from ultralytics import YOLO
import cv2

# 1️⃣ Load your trained YOLOv8 model
model = YOLO("runs/detect/train8/weights/best.pt")  # change path if needed

# 2️⃣ Choose input: 0 for webcam, or provide image path
use_webcam = True  # Set False to test on image
image_path = "test.jpg"

if use_webcam:
    cap = cv2.VideoCapture(0)  # Open default webcam
    if not cap.isOpened():
        print("Cannot open webcam")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # 3️⃣ Run YOLO prediction
        results = model.predict(frame, verbose=False)

        # 4️⃣ Render predictions on frame
        annotated_frame = results[0].plot()  # returns frame with boxes

        # 5️⃣ Show window
        cv2.imshow("YOLOv8 Detection", annotated_frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

else:
    # For single image
    results = model.predict(image_path)
    annotated_image = results[0].plot()
    cv2.imshow("YOLOv8 Detection", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
