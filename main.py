import cv2
from ultralytics import YOLO


model = YOLO('yolov8m.pt')  # Medium model for better accuracy


class_names = model.model.names


cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Parameters
CONFIDENCE_THRESHOLD = 0.5
GREEN = (0, 255, 0)
FONT = cv2.FONT_HERSHEY_SIMPLEX

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Optional: resize for faster processing
    # frame = cv2.resize(frame, (640, 480))

    # Run YOLO model on the frame
    results = model(frame)[0]

    # Draw bounding boxes for all detected objects above confidence threshold
    for data in results.boxes.data.tolist():
        xmin, ymin, xmax, ymax, confidence, class_id = int(data[0]), int(data[1]), int(data[2]), int(data[3]), data[4], int(data[5])
        if float(confidence) < CONFIDENCE_THRESHOLD:
            continue
        class_name = class_names[class_id]
        cv2.rectangle(frame, (xmin, ymin), (xmax, ymax), GREEN, 2)
        cv2.putText(frame, f"{class_name} {confidence:.2f}", (xmin, ymin - 5), FONT, 0.5, GREEN, 2)

    # Display the frame
    cv2.imshow("YOLOv8m Real-Time Detection", frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
