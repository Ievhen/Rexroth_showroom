import time
from PIL import Image
import cv2
import numpy as np
from matplotlib import pyplot as plt
import tensorflow as tf
from tensorflow import keras
import os
import mysql.connector
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
import paho.mqtt.client as mqtt

#łączenie sie z bazą danych
def db_connect(ip, username, password, db):
    return mysql.connector.connect(
        host=ip,
        user=username,
        password=password,
        database=db
    )

#dane Brokera MQTT
MQTT_BROKER_IP = '192.168.99.90'
MQTT_BROKER_PORT = 1883

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
pts1 = np.float32([[5,15], [256,21], [20,235], [235,235]]) 
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]]) 
#kulka = "Zielone"

#calibration/ funkcja usuwająca efekt rybiego oka z obrazu
DIM=(768, 432)
K=np.array([[559.5570240342355, 0.0, 399.2668277470481], [0.0, 569.4305514418312, 269.0848227696134], [0.0, 0.0, 1.0]])
D=np.array([[-0.06102882844568303], [-0.6321857003065529], [2.0311417763083495], [-1.1833229519134025]])
def undistort(img):
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img
mag_x=255
mag_y=130
w=260
h=250

#take neural network model directory path from DB
db = db_connect('192.168.99.90', 'iotuser', 'iotuser', 'showroom')
cursor = db.cursor()
sql = f"SELECT * FROM showroom.init_param WHERE param_id = '6'"
cursor.execute(sql)
myresult = cursor.fetchall()

#wprowadzenie modelu sieci neuronowej z komputera przemyslowego
reconstructed_model = keras.models.load_model(myresult[0][4])

#kategorie rozpoznawanych klas
class_names = np.array(["Red","Blue","Empty", "Green","Yellow"])

#main loop
while True:
    #Subscribe topic/ czekanie na otrzymanie szukanego koloru
    msg = subscribe.simple('SERVICES/DELTA/COLOR/REQ', hostname=MQTT_BROKER_IP)
    kulka = f"{msg.payload.decode()}"
    print("Recived ... " + kulka)
    #połączenie z kamera, stream RTSP
    cap = cv2.VideoCapture('rtsp://service:Init12345.@192.168.99.149:554/?h264')

    # Capture frame
    ret, frame = cap.read()
    undframe = undistort(frame)
    # Display the resulting frame
    cropped = undframe[mag_y:mag_y+h, mag_x:mag_x+w]
    image=cropped
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

    # Apply Perspective Transform Algorithm 
    matrix = cv2.getPerspectiveTransform(pts1, pts2) 
    result = cv2.warpPerspective(image, matrix, (300, 300)) 
    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()
    color3 = []
    color2 = []
    x = []
    #wycięcie/przybliżenie poszczególnych miejsc magazynu (10 kolumn, <0-9>)
    for i in range(0, 10):
        color = result[275:300, 0+i*30:34+i*30]
        color2.append(cv2.resize(color,(224,224)))

    predicted_label_batch = []
    array_index = []
    #powtórz operację identyfikacji dopoki nie znajdzie odpowiedniego koloru, jeśli nie znalazl zwróc 'None'
    for i in range(0, 10):
        image = color2[i]
        #zmiana na reprezentacje RGB
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        input_arr = keras.preprocessing.image.img_to_array(image)
        norm_img = np.zeros((224,224))
        #zmiana reprezentacji pikseli na zakrez <0-1>
        input_arr = cv2.normalize(input_arr, norm_img, 1, 0,cv2.NORM_MINMAX);
        input_arr = np.array([input_arr])
        #wprowadzenie na sieć neuronowa/ obraz rozdzielczosci 224,224/ reprezentacja RGB/ 
        #przedstawiaja przyblizenie poszczególnych kulek
        predicted_batch = reconstructed_model.predict(input_arr)
        predicted_id = np.argmax(predicted_batch, axis=-1)
        predicted_label_batch = class_names[predicted_id]
        
        #przerwij pętle jeśli znalazl
        if predicted_label_batch == kulka:
            array_index = i
            break
        else:
            array_index = "None"
    #Wyslij na ktorym miejscu znaleziono kulke o danym kolorze / numer kolumny
    publish.single('SERVICES/DELTA/COLOR/ANS', array_index ,hostname = MQTT_BROKER_IP,port = MQTT_BROKER_PORT)
