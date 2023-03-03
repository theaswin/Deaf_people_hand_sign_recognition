# Importing all libraries
import cv2
import mediapipe as mp
import HandTrackingModule as htm
import math
cap = cv2.VideoCapture(0)

# assigning the htm
detector = htm.handDetector()

while True:

    # reading image
    ret,image = cap.read()
    # Reference image
    Reference = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Referece.jpg')
    cv2.imshow('Refererence',Reference)

    # resizing image
    image = cv2.resize(image,(900,600))

    # finding hands and Hands
    image = detector.findHands(image)
    # finding x,y position of fingers
    lmlist = detector.findPosition(image)

    if len(lmlist) != 0:
        thumb1 = lmlist[4][0]   #   zero  |thumb
        index1 = lmlist[8][0]   #   one   |index
        middle1 = lmlist[12][0] #   two   |middle
        ring1 = lmlist[16][0]   #   three | Ring
        small1 = lmlist[20][0]  #   four  | small

        # Distance
        T_I_distance = math.dist((lmlist[4][1],lmlist[4][2]),(lmlist[8][1],lmlist[8][2]))
        print(T_I_distance)

        # Angle


    fingers = detector.fingersUp()
    print(fingers)
    fin = str(fingers)

    # 1 == thumb
    # 4 == fore finger
    # 7 == middle finger
    # 10 == Ring
    # 13 == small

# for detection of exception chars G , J , N , O , P , R , S , T 

    if (fin[1] == '1' and fin[4] =='1' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0' and T_I_distance >70 ):
        G = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/g.jpg')
        G = cv2.resize(G,(300,300))
        cv2.imshow('Alphabet',G)


    if (fin[1] == '0' and fin[4] =='0' and fin[7] == '0' and fin[10]=='0' and fin[13]=='1'):
        J = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/j.jpg')
        J = cv2.resize(J,(300,300))
        cv2.imshow('Alphabet',J)

    if (fin[1] == '0' and fin[4] =='1' and fin[7] == '1' and fin[10]=='0' and fin[13]=='0'):
        N = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/n.jpg')
        N = cv2.resize(N,(300,300))
        cv2.imshow('Alphabet',N)

    if (fin[1] == '1' and fin[4] =='0' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0' and T_I_distance<40):
        O = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/o.jpg')
        O = cv2.resize(O,(300,300))     
        cv2.imshow('Alphabet',O)

    # if (fin[1] == '0' and fin[4] =='1' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0'):
    #     P = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/p.jpg')
    #     P = cv2.resize(P,(300,300))
    #     cv2.imshow('Alphabet',P)

    if (fin[1] == '1' and fin[4] =='1' and fin[7] == '1' and fin[10]=='0' and fin[13]=='0'):
        R = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/r.jpg')
        R = cv2.resize(R,(300,300))
        cv2.imshow('Alphabet',R)

    if (fin[1] == '0' and fin[4] =='0' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0'):
        S = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/s.jpg')
        S = cv2.resize(S,(300,300))
        cv2.imshow('Alphabet',S)

    if (fin[1] == '1' and fin[4] =='0' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0' and T_I_distance>40):
        T = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/t.jpg')
        T = cv2.resize(T,(300,300))
        cv2.imshow('Alphabet',T)
































    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF == 27:
        break