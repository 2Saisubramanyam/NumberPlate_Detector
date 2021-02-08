import cv2

fh=480
fw=640
mina=500
plate = cv2.CascadeClassifier("res\haarcascade_russian_plate_number.xml")
cap = cv2.VideoCapture(0)
cap.set(3,fw)
cap.set(4,fh)
cap.set(10,150)

while True:
    success, img = cap.read()
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    nplate= plate.detectMultiScale(img,1.1,4)

    for (x, y, w, h) in nplate:
        area = w*h
        if(area>mina):
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 0), 3)
            cv2.putText(img,"number plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),3)
            imgRoi = img[y:y+h,x:x+w]
            cv2.imshow("roi",imgRoi)

    cv2.imshow("result",img)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break








