import cv2
import numpy as np
import HandTrackingModule as htm
import mediapipe as mp
import math
import poseModule as pm


detector = pm.poseDetector()
# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

detector = htm.handDetector()


while True:
    success,image = cap.read()


    image = cv2.resize(image,(900,600))
    # image = cv2.flip(image,2)

    # find hand landmarks
    image = detector.findHands(image)
    lmlist = detector.findPosition(image)



    if len(lmlist) !=0:
        thumb1 = lmlist[4][0] #   zero |thumb
        index1 = lmlist[8][0] #   one  |index
        middle1 = lmlist[12][0] # two |middle
        ring1 = lmlist[16][0] #      three | Ring
        small1 = lmlist[20][0] #    four  | small


        # print(lmlist[4][1:]," new ",lmlist[8][1:])
        # Distance b/w thumb and index
        T_S_distance = math.dist((lmlist[4][1],lmlist[4][2]),(lmlist[20][1],lmlist[20][2]))
        T_I_distance = math.dist((lmlist[4][1],lmlist[4][2]),(lmlist[8][1],lmlist[8][2]))
        M_T_distance = math.dist((lmlist[12][1],lmlist[12][2]),(lmlist[4][1],lmlist[4][2]))
        R_T_distance = math.dist((lmlist[16][1],lmlist[16][2]),(lmlist[4][1],lmlist[4][2]))
        I_M_distance = math.dist((lmlist[8][1],lmlist[8][2]),(lmlist[12][1],lmlist[12][2]))
        R_M_distance = math.dist((lmlist[16][1],lmlist[16][2]),(lmlist[12][1],lmlist[12][2]))
        S_Z_distance = math.dist((lmlist[20][1],lmlist[20][2]),(lmlist[0][1],lmlist[0][2]))
        print(S_Z_distance)
        # Angle b/w points

        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[7][1:]
        x3,y3 = lmlist[6][1:]

        I_I_I_angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        
        # points 

        x4,y4 = lmlist[8][1:] 
        x5,y5 = lmlist[5][1:] 
        x6,y6 = lmlist[4][1:] 

        I_I_T_angle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                             math.atan2(y4 - y2, x4 - x5))
        


    fingers = detector.fingersUp()
    # print(fingers)

    fin = str(fingers)
    # print(fin[10])
    
    # 1 == thumb
    # 4 == fore finger
    # 7 == middle finger
    # 10 == Ring
    # 13 == small

# loop for do function
    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
        print("A")

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '1'):
        print("B")

    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance<20):
        print("C")

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '0' and fin[13]=='0' and fin[10]=='0'and T_S_distance<70):
        print('D')

    if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0'):
        print("E")

    if (fin[13] == '1' and fin[10] == '1' and fin[7] == '1' and fin[1]== '0' and fin[4] == '0'):
        print("F")

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
    #     print("G")

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and I_M_distance<50):
        print("H")

    if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '1'):
        print("I")

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_S_distance<30):
    #     print("J")

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
        print("K")

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_T_angle>60):
        print("L")

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '0' and R_M_distance<40):
        print("M")
    
    # if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
    #     print("N")

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance<30):
    #     print("O")

    # if (fin[1] == '1' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
    #     print("P")
    
    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
        print("Q")

    # if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and M_T_distance < 50):
    #     print("R")

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_S_distance>20):
    #     print("S")

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and R_T_distance<50):
    #     print("O")

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and R_T_distance<50):
    #     print("S")

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and R_T_distance<50):
    #     print("T")

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
    #     print("U")    

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and I_M_distance>50):
        print("U") # R

    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
        print("A") # V

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '0' and R_M_distance>50):
        print("W")

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_I_angle<80):
        print("X")

    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '1'):
        print("Y")

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_T_angle<30):
        print("Z")

        
        
        

        
        
    cv2.imshow("screen",image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
