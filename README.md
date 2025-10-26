**📸 Real-Time YOLOv8 Object Detection System**

This project implements a high-performance, real-time object detection system designed to analyze live video streams from a webcam using the state-of-the-art **YOLOv8m** model. It processes frames instantly to identify, classify, and localize objects, making it ideal for applications like surveillance, smart retail analytics, or human-computer interaction.

✨ **Key Features & Technologies**

* **Real-Time Performance:** Engineered a Python and OpenCV pipeline to maintain high FPS processing for smooth, live video analysis.
* **YOLOv8m Architecture:** Utilizes the **Medium (M)** size model from the Ultralytics YOLOv8 series for an excellent balance of speed and detection accuracy.
* **Live Webcam Integration:** Direct acquisition of the video stream using OpenCV's `cv2.VideoCapture`.
* **Visual Output:** Renders **bounding boxes**, **confidence scores**, and **class labels** directly onto the video feed.
* **Tools:** Python, **OpenCV (cv2)**, **Ultralytics YOLOv8**, **NumPy**.

## 🚀 Getting Started

These instructions will get a copy of the project up and running on your local machine.

### Prerequisites

You need **Python 3.8+** and **`pip`** installed.

```bash
# Optional: Create a new virtual environment
python -m venv venv
source venv/bin/activate

**Installation **

Clone the repository:


git clone [https://github.com/Roohi2204/YOLOv8-RealTime-Webcam-Detector.git](https://github.com/Roohi2204/YOLOv8-RealTime-Webcam-Detector.git)

cd YOLOv8-RealTime-Webcam-Detector

**Install the dependencies:**


pip install -r requirements.txt

Running the Detector.Ensure a webcam is connected and accessible by your system.

**Run the main script:**

python main.py

A window will open displaying the live feed. Press the 'q' key to close the application.
