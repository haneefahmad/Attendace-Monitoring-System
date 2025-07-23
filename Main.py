import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Load face encodings and names
bala_image = face_recognition.load_image_file("C://Users//madha//OneDrive//Desktop//Projects//Facedetect_Attendance//bala.jpg")
bala_encoding = face_recognition.face_encodings(bala_image)[0]

haneef_image = face_recognition.load_image_file("C://Users//madha//OneDrive//Desktop//Projects//Facedetect_Attendance//haneef.jpg")
haneef_encoding = face_recognition.face_encodings(haneef_image)[0]

haytham_image = face_recognition.load_image_file("C://Users//madha//OneDrive//Desktop//Projects//Facedetect_Attendance//haytham.jpg")
haytham_encoding = face_recognition.face_encodings(haytham_image)[0]

known_face_encoding = [
    bala_encoding,
    haneef_encoding,
    haytham_encoding,
]

known_faces_names = ["bala", "haneef", "haytham"]

students = known_faces_names.copy()

# Open CSV file for writing
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_filename = current_date + ".csv"

with open(csv_filename, "w+", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Open video capture
    video_capture = cv2.VideoCapture(0)

    while True:
        _, frame = video_capture.read()
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Face recognition using face_locations
        face_locations = face_recognition.face_locations(small_frame)
        face_encodings = face_recognition.face_encodings(small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)

            if matches[best_match_index]:
                name = known_faces_names[best_match_index]

            face_names.append(name)

            # Update attendance and display name on the frame
            if name in known_faces_names:
                font = cv2.FONT_HERSHEY_SIMPLEX
                bottomLeftCornerOfText = (10, 100)
                fontScale = 1.5
                fontColor = (255, 0, 0)
                thickness = 3
                lineType = 2

                cv2.putText(
                    frame,
                    name + " Present",
                    bottomLeftCornerOfText,
                    font,
                    fontScale,
                    fontColor,
                    thickness,
                    lineType,
                )

                if name in students:
                    students.remove(name)
                    print(students)
                    current_time = now.strftime("%H-%M-%S")
                    csv_writer.writerow([name, current_time])

        # Display the frame
        cv2.imshow("Attendance System", frame)

        # Break the loop when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Release the video capture and close the CSV file
    video_capture.release()
    cv2.destroyAllWindows()
