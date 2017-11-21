import cv2


print("Hello Word")

while True:

    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    cv2 .imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break