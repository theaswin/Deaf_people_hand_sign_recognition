# Importing all libraries
import cv2
import mediapipe as mp
import HandTrackingModule as htm

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

        # Angle


    fingers = detector.fingersUp()
    fin = str(fingers)

    # 1 == thumb
    # 4 == fore finger
    # 7 == middle finger
    # 10 == Ring
    # 13 == small

# for detection of exception chars G , J , N , O , P , R , S , T 

    if (fin[1] == '1' and fin[4] =='1' and fin[7] == '0' and fin[10]=='0' and fin[13]=='0'):
        G = cv2.imread('/home/user/Desktop/Deaf_people_hand_sign/Data/g.jpg')
        G = cv2.resize(G,(300,300))
        cv2.imshow('Alphabet',G)
    else:
        print('kk')






























    cv2.imshow("Video",image)
    if cv2.waitKey(1) & 0xFF == 27:
        break