from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I"]]

lmList = 0
bbox = 0

class Button():
  def __init__(self, pos, text, size=[85, 85]):
    self.pos = pos
    self.size = size
    self.text = text
    x, y = self.pos
    w, h = self.size
    cv2.rectangle(img, self.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, self.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)


buttonLst = []

while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)

    if hands:
      #Hand 1
      hand1 = hands[0]
      lmList1 = hand1["lmList"]
      bbox1 = hand1["bbox"]
      centerPoint1 = hand1["center"]
      handType1 = hand1["type"]
      lmList = lmList1
      bbox = bbox1

      if len(hands) == 2:
        hand2 = hands[1]
        lmList2 = hand2["lmList"]
        bbox2 = hand2["bbox"]
        centerPoint2 = hand2["center"]
        handType2 = hand2["type"]
        lmList = lmList2
        bbox = bbox2


    for x in range (0, 8):
      buttonLst.append(Button([100 * x + 50, 100], "Q"))

    cv2.imshow("Image", img)
    cv2.waitKey(1)