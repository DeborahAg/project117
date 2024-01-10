import os
import cv2

path = "images"

images = []

for file in os.listdir(path):
    name, ext = os.path.splitext(file)
    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path + "/" + file
        print(file_name)
        images.append(file_name)

print(len(images))
count = len(images)
img = cv2.imread(images[0])
height,width,chanels = img.shape

video = cv2.VideoWriter("Friends_Video.mp4", cv2.VideoWriter_fourcc(*'DIVX'),5,(width,height))
for i in range(count):
    frame = cv2.imread(images[i])
    video.write(frame)

video.release()
print("Done!")
