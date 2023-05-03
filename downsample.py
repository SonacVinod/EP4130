import os
import cv2


# Get the list of all files and directories
path = "test"
dir_list = os.listdir(path)
i=0
# print(dir_list)
for dir in dir_list:
    aa=os.listdir(path+'/'+dir)
    for a in aa:
        addr=path+'/'+dir+'/'+a
        image = cv2.imread(addr)
        image = cv2.pyrDown(image)
        image = cv2.pyrDown(image)
        sp="tdata/"+str(i)+'.jpg'
        cv2.imwrite(sp, image)
        i+=1
        print(i)
print("done")