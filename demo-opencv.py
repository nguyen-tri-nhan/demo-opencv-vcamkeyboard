from cvzone.HandTrackingModule import HandDetector
import cv2

cap = cv2.VideoCapture(0)
cap.set(3, 1920)
cap.set(4, 1080)
detector = HandDetector(detectionCon=0.8)

keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]

lmList = 0
bbox = 0

def drawAll(img, buttonList):
  for button in buttonList:
    x, y = button.pos
    w, h = button.size
    cv2.rectangle(img, button.pos, (x+w, y+h), (255, 0, 255), cv2.FILLED)
    cv2.putText(img, button.text, (x + 20, y + 65), cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return img

class Button():
  def __init__(self, pos, text, size=[85, 85]):
    self.pos = pos
    self.size = size
    self.text = text

buttonList = []

for i in range(len(keys)):
  for j, key in enumerate(keys[i]):
    buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

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


    img = drawAll(img, buttonList)

    cv2.imshow("Image", img)
    cv2.waitKey(1)