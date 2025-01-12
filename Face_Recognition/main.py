import sys
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import sqlite3
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)
from datetime import datetime
import cv2 as cv
import numpy as np
import pickle
from sklearn.preprocessing import LabelEncoder
from keras_facenet import FaceNet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QImage,QIcon, QPixmap
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QLabel,
    QVBoxLayout,
    QPushButton,
    QWidget,
    QHBoxLayout,
    QMessageBox,QInputDialog
)

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Initialize face recognition
facenet = FaceNet()
faces_embeddings = np.load("faces_embeddings_done_4classes.npz")
Y = faces_embeddings['arr_1']
encoder = LabelEncoder()
encoder.fit(Y)
haarcascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
model = pickle.load(open("svm_model_160x160.pkl", 'rb'))



class FaceRecognitionApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Face Recognition")
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowIcon(QIcon("../icon/Logo.png"))

        # SQLite database connection
        self.conn = sqlite3.connect('../db/face_recognition.db')
        self.crs = self.conn.cursor()

        # Initialize webcam
        self.cap = cv.VideoCapture(0)
        self.webcam_width = int(self.cap.get(cv.CAP_PROP_FRAME_WIDTH))  # Default 640
        self.webcam_height = int(self.cap.get(cv.CAP_PROP_FRAME_HEIGHT))  # Default 480

        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QHBoxLayout(self.central_widget)

        # Webcam feed section
        self.webcam_label = QLabel("Webcam Feed")
        self.webcam_label.setAlignment(Qt.AlignCenter)
        self.webcam_label.setFixedSize(self.webcam_width, self.webcam_height)
        self.webcam_label.setStyleSheet(
            """
            background-color: #000;
            color: white;
            border: 5px solid #4CAF50;
            border: 30px;
            """
        )
        # masking for rounded corners
        self.layout.addWidget(self.webcam_label)

        # Info panel
        self.info_panel = QVBoxLayout()
        self.layout.addLayout(self.info_panel)

        self.person_image_label = QLabel("Person Image")
        self.person_image_label.setFixedSize(150, 150)
        self.person_image_label.setStyleSheet(
            """
            border: 1px solid black;
            border: 10px;
            """
        )
        self.info_panel.addWidget(self.person_image_label, alignment=Qt.AlignCenter)
        label_style = """
        QLabel {
            color: #333; /* Dark gray text */
            font-size: 16px;
            font-weight: bold;
            text-align: center
        }
        """
        self.person_name_label = QLabel("Name: Unknown")
        self.person_name_label.setAlignment(Qt.AlignCenter)  # Center alignment
        self.person_name_label.setStyleSheet(label_style)
        self.info_panel.addWidget(self.person_name_label)

        self.person_id_label = QLabel("ID: Unknown")
        self.person_id_label.setAlignment(Qt.AlignCenter)  # Center alignment
        self.person_id_label.setStyleSheet(label_style)
        self.info_panel.addWidget(self.person_id_label)

        self.person_dep = QLabel("Departement: Unknown")
        self.person_dep.setAlignment(Qt.AlignCenter)  # Center alignment
        self.person_dep.setStyleSheet(label_style)
        self.info_panel.addWidget(self.person_dep)

        self.person_role = QLabel("Role: Unknown")
        self.person_role.setAlignment(Qt.AlignCenter)  # Center alignment
        self.person_role.setStyleSheet(label_style)
        self.info_panel.addWidget(self.person_role)
        

        # Buttons
        button_style = """
        QPushButton {
            background-color: #4CAF50;
            color: white;
            font-size: 14px;
            border: none;
            border: 8px;
            padding: 10px 20px;
        }
        QPushButton:hover {
            background-color: #45a049;
        }
        QPushButton:disabled {
            background-color: #d3d3d3;
            color: #808080;
        }
        """
        self.start_button = QPushButton("Start Predictions")
        self.start_button.setStyleSheet(button_style)
        self.start_button.clicked.connect(self.start_predictions)
        self.info_panel.addWidget(self.start_button)

        self.stop_button = QPushButton("Stop Predictions")
        self.stop_button.setStyleSheet(button_style)
        self.stop_button.clicked.connect(self.stop_predictions)
        self.stop_button.setEnabled(False)
        self.info_panel.addWidget(self.stop_button)

        # Timer for updating frames
        self.timer = QTimer()
        self.timer.timeout.connect(self.process_frame)

        self.unknown_counter = 0  # Counter for consecutive "Unknown" detections
        self.frame_count = 0
        self.frame_results = {}

        self.fetch_setttings()


    def fetch_setttings(self):
            query = "SELECT threshold,email_sender,email_receiver,password FROM Settings where setting_id = 1"
            self.crs.execute(query)
            row = self.crs.fetchall()

            self.CONFIDENCE_THRESHOLD = row[0][0] / 100
            self.SMTP_SERVER = "smtp.gmail.com"  # Use your email provider's SMTP server
            self.SMTP_PORT = 587
            self.EMAIL_ADDRESS = row[0][1]  # Your email address
            self.SECURITY_EMAIL = row[0][2]  # Security team's email
            self.EMAIL_PASSWORD = row[0][3]  # Your email password

    def send_alert_email(self):
        try:
            # Capture a screenshot from the webcam
            ret, frame = self.cap.read()
            if ret:
                screenshot_path = "unknown_person_screenshot.jpg"
                cv.imwrite(screenshot_path, frame)

                subject = "Security Alert: Unknown Person Detected"
                body = (
                    f"An unknown person has been detected multiple times "
                    f"by the Company Access Control System. Please investigate immediately.\n\n"
                    f"Screenshot attached."
                )

                # Email configuration
                message = MIMEMultipart()
                message["From"] = self.EMAIL_ADDRESS
                message["To"] = self.SECURITY_EMAIL
                message["Subject"] = subject

                # Attach the screenshot
                with open(screenshot_path, "rb") as attachment:
                    part = MIMEImage(attachment.read(), name=screenshot_path)
                    message.attach(part)

                message.attach(MIMEText(body, "plain"))

                with smtplib.SMTP(self.SMTP_SERVER, self.SMTP_PORT) as server:
                    server.starttls()
                    server.login(self.EMAIL_ADDRESS, self.EMAIL_PASSWORD)
                    server.sendmail(self.EMAIL_ADDRESS, self.SECURITY_EMAIL, message.as_string())

                print("Alert email with screenshot sent to security.")
                os.remove(screenshot_path)  # Remove the screenshot after sending the email

        except Exception as e:
            print(f"Failed to send alert email: {e}")


    def resizeEvent(self, event):
        # Dynamically adjust the resized photo
        pixmap = self.person_image_label.pixmap()
        if pixmap:
            resized_pixmap = pixmap.scaled(
                self.person_image_label.width(),
                self.person_image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.person_image_label.setPixmap(resized_pixmap)

        # Ensure labels remain centered (Name and ID)
        self.person_name_label.setAlignment(Qt.AlignCenter)
        self.person_id_label.setAlignment(Qt.AlignCenter)
        super().resizeEvent(event)


    def start_predictions(self):
        self.start_button.setEnabled(False)
        self.stop_button.setEnabled(True)
        self.frame_count = 0
        self.frame_results = {}
        self.timer.start(50)  # Capture frames every 50ms

    def stop_predictions(self):
        self.timer.stop()
        self.start_button.setEnabled(True)
        self.stop_button.setEnabled(False)

    def process_frame(self):
        if self.frame_count < 15:
            ret, frame = self.cap.read()
            if ret:
                rgb_img = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
                gray_img = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                faces = haarcascade.detectMultiScale(gray_img, 1.3, 5)

                if len(faces) > 0:
                    largest_face = max(faces, key=lambda face: face[2] * face[3])
                    (x, y, w, h) = largest_face

                    face_img = rgb_img[y:y+h, x:x+w]
                    face_img_resized = cv.resize(face_img, (160, 160))
                    face_img_resized = np.expand_dims(face_img_resized, axis=0)
                    ypred = facenet.embeddings(face_img_resized)
                    face_name = model.predict(ypred)[0]
                    confidence = max(model.predict_proba(ypred)[0])

                    if confidence >= self.CONFIDENCE_THRESHOLD:
                        final_name = encoder.inverse_transform(np.array([face_name]))[0]
                    else:
                        final_name = "Unknown"

                    # Update frame results
                    if final_name in self.frame_results:
                        self.frame_results[final_name] += 1
                    else:
                        self.frame_results[final_name] = 1

                    # Draw bounding box and name
                    cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 255), 2)
                    cv.putText(frame, final_name, (x, y-10), cv.FONT_HERSHEY_SIMPLEX,
                            1, (0, 255, 0), 2, cv.LINE_AA)

                # Display the frame in UI
                qimg = QImage(frame.data, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                self.webcam_label.setPixmap(QPixmap.fromImage(qimg))

                self.frame_count += 1
        else:
            self.timer.stop()
            # Determine the most recurrent name
            if self.frame_results:
                final_name = max(self.frame_results, key=self.frame_results.get)

                if final_name == "Unknown":
                    self.unknown_counter += 1
                    if self.unknown_counter == 2:  # Trigger alert after two cycles
                        self.send_alert_email()
                        self.unknown_counter = 0  # Reset counter after alert
                else:
                    self.unknown_counter = 0  # Reset counter if not "Unknown"

                # Update UI with person info if it's not "Unknown"
                if final_name != "Unknown":
                    self.person_name_label.setText(f"Name: {final_name}")
                    self.update_person_info(final_name)

                # Reset frame tracking
                self.frame_count = 0
                self.frame_results = {}


    def update_person_info(self, final_name):
        self.crs.execute("""
            SELECT Users.user_id, Users.photo_path, Departements.dep_name, Users.role
            FROM Users
            JOIN Departements ON Users.dep_id = Departements.dep_id
            WHERE Users.name = ?
        """, (final_name,))
        
        user_data = self.crs.fetchone()
        
        if user_data:
            self.person_id_label.setText(f"ID: {user_data[0]}")
            self.person_dep.setText(f"Department: {user_data[2]}")
            self.person_role.setText(f"Role: {user_data[3]}")
            self.update_person_image(user_data[1])
            
            # Log into AccessLogs table
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.crs.execute("INSERT INTO AccessLogs (user_id, timestamp) VALUES (?, ?)", (user_data[0], timestamp))
            self.conn.commit()

            # Get the last saved log_id
            self.crs.execute("SELECT last_insert_rowid()")
            log_id = self.crs.fetchone()[0]

            # Show feedback dialog with buttons
            feedback_dialog = QMessageBox()
            feedback_dialog.setWindowTitle("Feedback")
            feedback_dialog.setText("Is this person correct?")
            feedback_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
            feedback_dialog.setIcon(QMessageBox.Question)

            response = feedback_dialog.exec()

            if response == QMessageBox.Yes:
                self.store_feedback(log_id, True, user_data[0])
            elif response == QMessageBox.No:
                while True:
                    id_dialog = QInputDialog()
                    new_id, id_ok = id_dialog.getText(self, 'Enter ID', 'Enter the correct ID:')

                    if not id_ok:
                        break  # Exit if the user cancels the input

                    if new_id.isdigit():
                        new_id = int(new_id)
                        # Validate the new ID against the Users table
                        self.crs.execute("SELECT user_id, photo_path, dep_name, role , name FROM Users JOIN Departements ON Users.dep_id = Departements.dep_id WHERE user_id = ?", (new_id,))
                        new_user_data = self.crs.fetchone()

                        if new_user_data:
                            # Update the UI with the new user's information
                            self.person_id_label.setText(f"ID: {new_user_data[0]}")
                            self.person_dep.setText(f"Department: {new_user_data[2]}")
                            self.person_role.setText(f"Role: {new_user_data[3]}")
                            self.person_name_label.setText(f"Name: {new_user_data[4]}")
                            self.update_person_image(new_user_data[1])
                            
                            # Log feedback and update the database
                            self.store_feedback(log_id, False, new_id)
                            break  # Exit the loop after successful update
                        else:
                            QMessageBox.warning(self, 'Invalid ID', 'The entered ID does not belong to any user.')
                    else:
                        QMessageBox.warning(self, 'Invalid Input', 'Please enter a valid numeric ID.')


        else:
            self.person_name_label.setText(f"Name: Unknown")
            self.person_id_label.setText("ID: Unknown")
            self.person_dep.setText(f"Department: Unknown")
            self.person_role.setText(f"Role: Unknown")
            self.update_person_image("profiles\\Unknown\\unknown.jpg")  # Fallback image if user is not found

    def store_feedback(self, log_id, pred, reeluser):
        try:
            if isinstance(reeluser, int):  # Check if reeluser is an integer
                self.crs.execute("INSERT INTO Feedback (idlogs, pred, reeluser) VALUES (?, ?, ?)", 
                            (log_id, pred, reeluser))
                self.conn.commit()
            else:
                raise ValueError("ID must be an integer.")
        except sqlite3.Error as e:
            print(f"Error storing feedback: {e}")
            self.conn.rollback()  # Rollback in case of an error
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


    def update_person_image(self, photo_path):
        try:
            # Load the image from the given path
            if os.path.exists(photo_path):
                person_img = QPixmap(photo_path)
            else:
                person_img = QPixmap("profiles\\Unknown\\unknown.jpg")  # Fallback image if path is invalid

            # Resize the image to fill the label while maintaining aspect ratio
            person_img_resized = person_img.scaled(
                self.person_image_label.width(),
                self.person_image_label.height(),
                Qt.KeepAspectRatioByExpanding,  # Ensures the image fills the QLabel
                Qt.SmoothTransformation,
            )

            # Set the resized image to the QLabel
            self.person_image_label.setPixmap(person_img_resized)

        except Exception as e:
            print(f"Error loading or resizing image: {e}")
            self.person_image_label.clear()  # Clear the label in case of an error

    def resizeEvent(self, event):
        # Dynamically adjust the image size to match the QLabel dimensions
        pixmap = self.person_image_label.pixmap()
        if pixmap:
            resized_pixmap = pixmap.scaled(
                self.person_image_label.width(),
                self.person_image_label.height(),
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation,
            )
            self.person_image_label.setPixmap(resized_pixmap)
        super().resizeEvent(event)


    def closeEvent(self, event):
        self.cap.release()
        self.conn.close()
        cv.destroyAllWindows()
        event.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = FaceRecognitionApp()
    main_window.show()
    sys.exit(app.exec())