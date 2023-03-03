import cv2
import numpy as np
import HandTrackingModule as htm
import mediapipe as mp
import math
import poseModule as pm


# mpHands = mp.solutions.hands
# hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)
# mpDraw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

detector = htm.handDetector()


while True:
    success,image = cap.read()
    Reference = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Referece.jpg')
    cv2.imshow('Reference',Reference)


    image = cv2.resize(image,(900,600))
    # image = cv2.flip(image,2)

    # find hand landmarks
    image = detector.findHands(image)
    lmlist = detector.findPosition(image)



    if len(lmlist) !=0:
        thumb1 = lmlist[4][0]   #   zero  |thumb
        index1 = lmlist[8][0]   #   one   |index
        middle1 = lmlist[12][0] #   two   |middle
        ring1 = lmlist[16][0]   #   three | Ring
        small1 = lmlist[20][0]  #   four  | small


        # print(lmlist[4][1:]," new ",lmlist[8][1:])
        # Distance b/w thumb and index
        T_S_distance = math.dist((lmlist[4][1],lmlist[4][2]),(lmlist[20][1],lmlist[20][2]))
        T_I_distance = math.dist((lmlist[4][1],lmlist[4][2]),(lmlist[8][1],lmlist[8][2]))
        M_T_distance = math.dist((lmlist[12][1],lmlist[12][2]),(lmlist[4][1],lmlist[4][2]))
        R_T_distance = math.dist((lmlist[16][1],lmlist[16][2]),(lmlist[4][1],lmlist[4][2]))
        I_M_distance = math.dist((lmlist[8][1],lmlist[8][2]),(lmlist[12][1],lmlist[12][2]))
        R_M_distance = math.dist((lmlist[16][1],lmlist[16][2]),(lmlist[12][1],lmlist[12][2]))
        S_Z_distance = math.dist((lmlist[20][1],lmlist[20][2]),(lmlist[0][1],lmlist[0][2]))
        # Angle b/w points

        x1,y1 = lmlist[8][1:]
        x2,y2 = lmlist[7][1:]
        x3,y3 = lmlist[6][1:]

        I_I_I_angle = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                             math.atan2(y1 - y2, x1 - x2))
        
        # Angle between iit 

        x4,y4 = lmlist[8][1:] 
        x5,y5 = lmlist[5][1:] 
        x6,y6 = lmlist[4][1:] 

        I_I_T_angle = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                             math.atan2(y4 - y2, x4 - x5))
        
        # Angle between  8,5,12

        x7,y7 = lmlist[8][1:] 
        x8,y8 = lmlist[5][1:] 
        x9,y9 = lmlist[12][1:] 


        I_H_M_angle = math.degrees(math.atan2(y7 - y8, x7 - x8) -
                             math.atan2(y9 - y2, x9 - x5))
        


    fingers = detector.fingersUp()
    # print(fingers)

    fin = str(fingers)
    
    # 1 == thumb
    # 4 == fore finger
    # 7 == middle finger
    # 10 == Ring
    # 13 == small

# loop to see the alphabets
    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
        A = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/a.png')
        A = cv2.resize(A,(300,300))
        cv2.imshow('pic',A)

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '1'):
        B = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/b.png')
        B = cv2.resize(B,(300,300))
        cv2.imshow("pic",B)

    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance<50):
        C = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/c.png')
        C = cv2.resize(C,(300,300))
        cv2.imshow("pic",C)

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '0' and fin[13]=='0' and fin[10]=='0'and T_S_distance>30):
        D = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/d.png')
        D = cv2.resize(D,(300,300))
        cv2.imshow("pic",D)

    if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0'):
        E = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/e.png')
        E = cv2.resize(E,(300,300))
        cv2.imshow("pic",E)

    if (fin[13] == '1' and fin[10] == '1' and fin[7] == '1' and fin[1]== '0' and fin[4] == '0'):
        F = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/f.jpg')
        F = cv2.resize(F,(300,300))
        cv2.imshow("pic",F)

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
    #     print("G")

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and I_M_distance<50):
        H = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/h.jpg')
        H = cv2.resize(H,(300,300))
        cv2.imshow("pic",H)

    if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '1'):
        I = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/i.jpg')
        I = cv2.resize(I,(300,300))
        cv2.imshow("pic",I)

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_S_distance<30):
    #     print("J")

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and T_I_distance>90):
        K = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/k.jpg')
        K = cv2.resize(K,(300,300))
        cv2.imshow("pic",K)

    if (fin[1] == '1' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_T_angle>60):
        L = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/l.jpg')
        L = cv2.resize(L,(300,300))
        cv2.imshow("pic",L)

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '0' and R_M_distance<40):
        M = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/m.jpg')
        M = cv2.resize(M,(300,300))
        cv2.imshow("pic",M)

    # if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
    #     print("N")

    # if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_I_distance<30):
    #     print("O")

    # if (fin[1] == '1' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
    #     print("P")
    
    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
        Q = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/q.jpg')
        Q = cv2.resize(Q,(300,300))
        cv2.imshow("pic",Q)

#    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0'):
#        R = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/r.jpg')
#        R = cv2.resize(R,(300,300))
#        cv2.imshow("pic",R)

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and T_S_distance>20):
    #     print("S")

    # if (fin[1] == '0' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and R_T_distance<50):
    #     print("T")

   

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and I_M_distance>50 and I_H_M_angle<50):
        U = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/u.jpg')
        U = cv2.resize(U,(300,300))
        cv2.imshow("pic",U)


    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '0' and fin[13] == '0' and I_H_M_angle>50):
        V = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/v.jpg')
        V = cv2.resize(V,(300,300))
        cv2.imshow("pic",V)


    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '1' and fin[10]== '1' and fin[13] == '0' and R_M_distance>50):
        W = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/w.jpg')
        W = cv2.resize(W,(300,300))
        cv2.imshow("pic",W)

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_I_angle<160):
        X = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/x.jpg')
        X = cv2.resize(X,(300,300))
        cv2.imshow("pic",X)

    if (fin[1] == '1' and fin[4] == '0' and fin[7] == '0' and fin[10]== '0' and fin[13] == '1'):
        Y = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/y.jpg')
        Y = cv2.resize(Y,(300,300))
        cv2.imshow("pic",Y)

    if (fin[1] == '0' and fin[4] == '1' and fin[7] == '0' and fin[10]== '0' and fin[13] == '0' and I_I_I_angle>170):
        Z = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/z.jpg')
        Z = cv2.resize(Z,(300,300))
        cv2.imshow("pic",Z)

        
        
        

        
        
    cv2.imshow("screen",image)
    if cv2.waitKey(1) & 0xFF == 27:
        break
