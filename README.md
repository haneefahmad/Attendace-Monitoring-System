
# Face Recognition Attendance System

This is a simple attendance system that uses **face recognition** to mark attendance in real-time using a webcam. It identifies registered faces, marks them as "Present", and saves the data with a timestamp into a CSV file named by date.

---

## Features

- Recognizes pre-registered faces using the `face_recognition` library
- Records name and time of attendance into a `.csv` file
- Prevents duplicate entries for the same person
- Live video feed with name overlay
- Auto-saves attendance based on date

---

## Requirements

- Python 3.x
- OpenCV
- face_recognition
- NumPy
- CSV (built-in)
- Webcam

Install dependencies:

```bash
pip install face_recognition opencv-python numpy
````

---

## Folder Structure

```
Facedetect_Attendance/
│
├── bala.jpg
├── haneef.jpg
├── haytham.jpg
├── main.py
├── 2025-07-23.csv (generated automatically)
```

---

## How It Works

1. Loads images of known individuals and encodes their facial features.
2. Captures video from the webcam.
3. For each frame:

   * Detects faces and matches them with the known encodings.
   * If a match is found, displays the person's name and marks them as present.
   * Saves the name and timestamp in a CSV file (named using current date).
4. Press `q` to exit.

---

## Face Images

Make sure your face images (e.g., `bala.jpg`, `haneef.jpg`, `haytham.jpg`) are in the same folder as the script, or update the file paths accordingly.

```python
bala_image = face_recognition.load_image_file("C://...//bala.jpg")
```

---

## Attendance File

* A new CSV file (e.g., `2025-07-23.csv`) is created each time the script runs.
* Contains two columns: **Name** and **Time**.
* Example content:

```
bala, 09-15-22
haneef, 09-15-25
```

---

## Notes

* The webcam feed is scaled down to speed up processing.
* Attendance is marked only once per person per session.
* Uses the current system date and time.

---


