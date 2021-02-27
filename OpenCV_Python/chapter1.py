import cv2

# img = cv2.imread("Resources/lena.png")
# cv2.imshow("output", img)
# cv2.waitKey(0)

# cap = cv2.VideoCapture('Resources/test_video.mpq4')
#
# while True:
#     success, img = cap.read()
#     cv2.imshow('video',img)
#     if cv2.waitKey(1) & 0xFF ==ord('q'):
#         break

cap = cv2.VideoCapture(0)
cap.set(3, 640)  # 3 is Width
cap.set(4, 480)  # 4 is Height
cap.set(10, 100)  # 10 is Brightness

while True:
    success, img = cap.read()
    cv2.imshow('video', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
