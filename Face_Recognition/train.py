import cv2 as cv
import os
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from keras_facenet import FaceNet
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pickle
from mtcnn.mtcnn import MTCNN


os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

class FACELOADING:
    def __init__(self, directory):
        self.directory = directory
        self.target_size = (160, 160)
        self.X = []
        self.Y = []
        self.detector = MTCNN()

    def extract_face(self, filename):
        try:
            img = cv.imread(filename)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            if img is None:
                raise FileNotFoundError(f"Image not found: {filename}")
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            x, y, w, h = self.detector.detect_faces(img)[0]['box']
            x, y = abs(x), abs(y)
            face = img[y:y+h, x:x+w]
            face_arr = cv.resize(face, self.target_size)
            return face_arr
        except Exception as e:
            print(f"Error processing {filename}: {e}")
            return None

    def load_faces(self, dir):
        FACES = []
        for im_name in os.listdir(dir):
            try:
                path = os.path.join(dir, im_name)
                single_face = self.extract_face(path)
                if single_face is not None:
                    FACES.append(single_face)
            except Exception as e:
                pass
        return FACES

    def load_classes(self):
        for sub_dir in os.listdir(self.directory):
            path = os.path.join(self.directory, sub_dir)
            FACES = self.load_faces(path)
            labels = [sub_dir for _ in range(len(FACES))]
            print(f"Loaded {len(labels)} images successfully for class '{sub_dir}'.")
            self.X.extend(FACES)
            self.Y.extend(labels)

        return np.asarray(self.X), np.asarray(self.Y)

    def plot_images(self):
        plt.figure(figsize=(18, 16))
        for num, image in enumerate(self.X):
            ncols = 3
            nrows = len(self.Y) // ncols + 1
            plt.subplot(nrows, ncols, num + 1)
            plt.imshow(image)
            plt.axis('off')
        plt.show()

# Load data
faceloading = FACELOADING("augmented_dataset/")
X, Y = faceloading.load_classes()

# FaceNet embedding function
embedder = FaceNet()

def get_embedding(face_img):
    face_img = face_img.astype('float32') # 3D(160x160x3)
    face_img = np.expand_dims(face_img, axis=0) 
    yhat = embedder.embeddings(face_img)
    return yhat[0] # 512D image (1x1x512)

# Generate embeddings
EMBEDDED_X = [get_embedding(img) for img in X]
EMBEDDED_X = np.asarray(EMBEDDED_X)
np.savez_compressed('faces_embeddings_done_4classes.npz', EMBEDDED_X, Y)

# Label Encoding
encoder = LabelEncoder()
encoder.fit(Y)
Y_encoded = encoder.transform(Y)

# Train SVM
X_train, X_test, Y_train, Y_test = train_test_split(EMBEDDED_X, Y_encoded, shuffle=True, random_state=17)
model = SVC(kernel='linear', probability=True)
model.fit(X_train, Y_train)

# Save the model
with open('svm_model_160x160.pkl', 'wb') as f:
    pickle.dump(model, f)

print(f"Model accuracy: {accuracy_score(Y_test, model.predict(X_test))}")
