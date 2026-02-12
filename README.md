# Contour-Based Object Size Measurement using OpenCV

This project implements a basic rule-based computer vision system to measure the size of objects from static images using contour detection.

The system uses thresholding and contour analysis to extract object boundaries and compute pixel-based measurements.

---

## 📌 Project Overview

- Image preprocessing using grayscale conversion and Gaussian blur
- Object segmentation using thresholding (Otsu method)
- Contour detection using OpenCV
- Bounding box-based measurement
- Pixel-to-real-world unit conversion (using scale factor)

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- NumPy

---

## 🚀 Installation

pip install -r requirements.txt

## ▶️ Run the Project
python src/object_measurement.py

The script will:

Detect objects in the image

Draw bounding boxes around detected objects

Calculate contour area

Convert pixel area into approximate real-world units using a scale factor

Display and save the annotated output image

<img width="1118" height="823" alt="image" src="https://github.com/user-attachments/assets/dd33336b-d494-4a6d-a390-dbf56ac6f596" />

<img width="1120" height="782" alt="image" src="https://github.com/user-attachments/assets/4e820092-304b-4be5-bd2c-cb5992ff5f1d" />


--- 


## 📏 Measurement Method

Contour area is calculated using cv2.contourArea()

Object dimensions are approximated using bounding rectangles

Pixel values are converted to real-world units using a predefined calibration factor

Note: The calibration factor assumes a fixed pixel-to-unit ratio and is not dynamically computed.

---

##📷 Sample Use Cases

Coin measurement

Simple object dimension estimation

Basic inspection simulation

---

## 🧠 Limitations

Works best with clean background and high contrast

Objects should not heavily overlap

Calibration is approximate and assumes fixed scale

Designed for static images (no live camera feed)



