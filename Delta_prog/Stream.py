import sys
import numpy as np
import cv2

#Parametry usuwajace efekt rybiego oka
DIM=(768, 432)
K=np.array([[559.5570240342355, 0.0, 399.2668277470481], [0.0, 569.4305514418312, 269.0848227696134], [0.0, 0.0, 1.0]])
D=np.array([[-0.06102882844568303], [-0.6321857003065529], [2.0311417763083495], [-1.1833229519134025]])
def undistort(img):
    h,w = img.shape[:2]
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    return undistorted_img
#stream rtsp kamera nad robotem typu delta
cap = cv2.VideoCapture('rtsp://service:Init12345.@192.168.99.149:554/?h264')
cap.set(cv2.CAP_PROP_BUFFERSIZE,0)
x = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #usuniecie efektu rybiego oka
    undframe = undistort(frame)
    # Display the resulting frame
    cv2.imshow('frame',undframe)
    #zamkniecie przez klawisz q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()





