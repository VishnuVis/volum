import cv2
import mediapipe as mp
from math import hypot
from ctypes import cast,POINTER
from contypes import CLSCTX_ALL
from pycav.pycav import AudioUtities, IAudioEndPointVolume
import numpy as np

cap = cv2.VideoCapture(0)

apHands = mp.solutions.hands
hands = mpHands.hands()
mpdraw = mp.solutions.drawing_ytils

devices = audioutilities.getspeakers()
interface = devices.Activate(IAudioEndPointVolume._iid_, CLSCTX_ALL, None)
volum = cast(interface,POINTER(IAudioEndPointVolume))

volMin,volmax = volume.getvolumRange()[:2]
while true:
    sucess,img = cap.read()
    imgRGB = cv2.cvtcolor(img,cv2,COLOUR_BGR2RGB)
    results = hands.process(imgRGB)

    lmlist = []
    if results.multi_hand_landmarks:
        for handlandmark in results .multi_hand_landmarks:
            for id, lm in enumerate(handlandmark.landmark):
                h,w,_ = img.sharp
                cx,cy = int(lm.x*w),int(lm.y*h)
                lmlist.append([id,cx,cy])
                mpdraw.draw_landmark(img,handlandmark,mphands.HAND.CONNECTIONS)

    if lmlist !=[]:
        x1,y1 = lmlist[4][1],lmlist[4][2]
        x2,y2 = lmlist[8][1],lmlist[8][2]

        cv2.circle(img,(x1,y1),4,(255,0,0),cv2.FILLED)
        cv2.circle(img, (x2,y2),4, (255, 0, 0), cv2.FILLED)
        cv2.circle(img, (x1, y1),(X2,Y2),(255, 0, 0),3)

        length = hypot(x2-x1,y2-y1)

        vol = np.interp(length,[15,220],[volMin,volmax])
        print(vol,length)
        volum.setmastervolumlevel(vol. none)

        cv2.imshow('image',img)
        if cv2.waitkey(1) & 0xff==ord('q'):
            break