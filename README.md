# 🎯 SmartVision Distance Detector

> A real-time object detection system powered by YOLOv8 and OpenCV to calculate and alert the **distance of approaching objects** (like people, cars, buses) from the camera using pixel-metric calibration.

---

## 🚀 Features

- ✅ **YOLOv8 Object Detection** with support for multiple classes (person, car, bus)
- 📏 **Distance Estimation** using calibrated pixels-per-meter
- 🔔 **Real-time Alarm System**: Beeps when objects are too close (configurable)
- 📹 **Video Output Recording** with visual overlays
- 🧠 **Multithreading for smooth beeping & video processing**
- 🎨 **Custom Bounding Boxes**, Labels, and Warning Indicators

---

## 🧠 How It Works

1. **YOLOv8** detects the objects in real-time.
2. For each detected object, the **centroid distance** from the camera's bottom center is computed.
3. If the distance is below a threshold (e.g., 5 meters), a **beeping sound** is triggered.
4. A **colored warning circle** on-screen shows current alert status.

---

## 📁 Project Structure

SmartVision-DistanceDetector/
│

├── app.py # Optional GUI or main app entry

├── main.py # Main script with full distance logic

├── with_sound.py # Alternate version with sound alert

├── functions.py # Helper functions (if modularized)

├── test5.mp4 # Input video (test footage)

├── visioneye-distance-calculation.avi # Output video

├── yolo11n.pt # YOLO model weights

├── requirements.txt # Python dependencies

├── README.md # You’re reading it!

└── .gitignore # To exclude unnecessary files


---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8+
- pip
- [YOLOv8](https://docs.ultralytics.com) installed via Ultralytics

### 📦 Installation

```bash
# Clone the repo
git clone https://github.com/gprabhat65/SmartVision-DistanceDetector.git
cd SmartVision-DistanceDetector

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate  # On Windows

# Install dependencies
pip install -r requirements.txt

Run the Application
python main.py

🔊 Customization
You can modify:

WARNING_DISTANCE = 5 → for changing alert distance

pixel_per_meter = 100 → for calibration based on your camera

CIRCLE_RADIUS and CIRCLE_CENTER → for alert indicator positioning


📦 Requirements
txt
Copy
Edit
opencv-python
ultralytics
torch
Install with: pip install -r requirements.txt

❗ Important Notes
Ensure your .pt model file (yolo11n.pt) is placed in the project directory.

Do not push large .pt or .mp4 files to GitHub without using Git LFS.

Avoid uploading __pycache__/, .idea/, or .avi outputs — include them in .gitignore.

🧠 Future Improvements
Add GUI with PyQt or Tkinter

Export analytics as CSV

Add camera calibration module for real-world accuracy

🧑‍💻 Author
Prabhat Kumar Gupta

📄 License

### ✅ Bonus: Recommended `.gitignore`

Create a `.gitignore` file with:

```gitignore
__pycache__/
.idea/
*.pt
*.mp4
*.avi
.DS_Store
.env
