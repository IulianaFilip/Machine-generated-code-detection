import cv2
import numpy as np

class AIFaceEyeDetector:
    def __init__(self, image_path, face_cascade_path, eye_cascade_path):
        self.image_path = image_path
        self.face_cascade = cv2.CascadeClassifier(face_cascade_path)
        self.eye_cascade = cv2.CascadeClassifier(eye_cascade_path)
        self.image = cv2.imread(image_path)
        self.gray_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        self.detected_faces = []

    def detect_faces(self, scale_factor=1.3, min_neighbors=5):
        # Detect faces in the grayscale image
        self.detected_faces = self.face_cascade.detectMultiScale(
            self.gray_image, scaleFactor=scale_factor, minNeighbors=min_neighbors
        )
        print(f"Detected {len(self.detected_faces)} faces")
        return self.detected_faces

    def detect_and_draw_eyes(self, face_coords):
        for (x, y, w, h) in face_coords:
            # Draw rectangle around face
            cv2.rectangle(self.image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # Region of interest for eyes
            roi_gray = self.gray_image[y:y + h, x:x + w]
            roi_color = self.image[y:y + h, x:x + w]
            
            eyes = self.eye_cascade.detectMultiScale(roi_gray)
            print(f"Detected {len(eyes)} eyes in face at ({x}, {y})")
            
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    def show_result(self, window_name="Detected Faces and Eyes"):
        cv2.imshow(window_name, self.image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # File paths
    image_file = "jp.png"
    face_cascade_file = "haarcascade_frontalface_default.xml"
    eye_cascade_file = "haarcascade_eye.xml"

    detector = AIFaceEyeDetector(image_file, face_cascade_file, eye_cascade_file)
    faces = detector.detect_faces()
    detector.detect_and_draw_eyes(faces)
    detector.show_result()
