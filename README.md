# 🧑‍🏫 Face Recognizer Attendance System

This project is a real-time **Face Recognition-Based Attendance System** using **OpenCV** and the powerful **face_recognition** library in Python. It detects and recognizes faces from a live webcam feed and automatically logs attendance by matching them with pre-stored images.

---

## 🧠 Project Overview

- 🎥 **Real-Time Detection**: Uses webcam to capture and recognize faces
- 📁 **Known Faces Database**: Images of registered individuals are stored and used for recognition
- 📅 **Attendance Log**: Attendance is automatically recorded with timestamp
- 💻 **Tech Stack**: Python, OpenCV, face_recognition, NumPy, Pandas

---

## 🔧 Features

- Face detection and recognition in real-time
- Logs recognized faces into a CSV file with name and timestamp
- Easily extensible: Just add a new image to the database to register a new person
- Lightweight and efficient using `dlib`-based face encodings

---

## 📸 Sample Output

![facerec](https://github.com/user-attachments/assets/5735455d-91d9-4ec5-a60d-c647a41a5193)
![Screenshot 2025-06-28 222527](https://github.com/user-attachments/assets/1044aa46-7b9f-4e36-8cc1-8c857a9e5683)

---

## 💡 Future Enhancements
- Add GUI dashboard to monitor live attendance
- Store data in a database (MySQL or MongoDB)
- Send daily reports via email
- Integrate mask detection for COVID-safe attendance



---
