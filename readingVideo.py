import cv2

videoFileName = "ball.mp4"

video = cv2.VideoCapture(videoFileName)

frames = []
for i in range(10):
 ret, frame = video.read()
 if frame is not None:
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 frames.append(gray)

video.release()

for frame in frames:
  cv2.imshow("lame", frame)
  cv2.waitKey()

print()