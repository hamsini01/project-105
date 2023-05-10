import os
import cv2
path = "Images/"
Image =[]



for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file      
        images.append(file_name)
        print(file_name)
print(len(Images))
count = len(Images)
fram = cv2.imread (Images [0])
height,width,chanels=fram.shape
size= (width,height)
print(size)
output=cv2.VideoWriter("video.avi",cv2.VideoWriter_fourcc(*"DIVX"),0.8,size)
for i in range(-1,0,-1):
    fram=cv2.imread(Images[i])
    output.write(fram)
output.release()
print("done")    
