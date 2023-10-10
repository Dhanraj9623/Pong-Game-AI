import cv2
import numpy as np
import mss
from PIL import Image 
from ppadb.client import Client
import threading

paddle_x = 2092
paddle_y= 535
paddle_y_min = 200
paddle_y_max = 920
ball_y = 0

adb = Client(host = '127.0.0.1',port=5037)
devices = adb.devices()

if len(devices) == 0:
    print("no devices attached ")
    quit()

device = devices [0]

running = True
def move_paddle():
    global paddle_y
    
    while running:
        to = ball_y * 2
        if ball_y <paddle_y_min:
            to = paddle_y_min
        if ball_y > paddle_y_max:
            to = paddle_y_max
        
        
        x1 = paddle_x
        x2 = paddle_x
        y1 = paddle_y
        y2 = to 
        
        
        device.shell(f'input touchscreen swipe {x1} {y1} {x2} {y2} 100')
        paddle_y = to 

t=threading.Thread(target=move_paddle)
t.start()

sct = mss.mss()

while True:
    scr = sct.grab({'left': 0, 'top': 40, 'width': 800, 'height': 400})
    img = np.array(scr)
    
    cv2.rectangle(img,(380,20),(450,120),(0,0,0),-1)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    
    circles = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=1,maxRadius=40)
    
    if circles is not None:
        circles = np.uint16(circles)
        
        for pt in circles [0, :]:
            x,y,r =pt[0],pt[1],pt[2]
            cv2.circle(img,(x,y),r,(0,0,255),5)
            ball_y=y
        
    
    cv2.imshow('output', img)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        running = False
        break

    
