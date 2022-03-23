import cv2
import glob
import os

i = 0

path = input("Please type in the location of the pictures you wish to resize...: ")
bw = input("Do you wish for the picture to be colored, or black & white? 0 = BW, 1 = COLORED....: ")
dim = input("What dimensions do you wish the photo to have? Ex(2000 1000)...: ")
try:
    arr = [float(x) for x in dim.split(' ')]
except:
    'Invalid Input. Please type dimensions as stated above (Ex: 1000 2000)...: '
final_destination = input("Where would you like to save these photos?...: ")


try:
    print(arr)
except:
    print("Operation failed, please make sure you have typed your inputs correctly")
    exit()

images = glob.glob(f"{path}/*.jpg")

prev = input("Would you like to preview the pictures? y/n...: ")

if prev == 'y':
    for img in images:
        image = cv2.imread(img, int(bw))
        re = cv2.resize(image, (int(arr[0]), int(arr[1])))
        cv2.imshow("pic", re)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    satisfied = input('Do you wish to proceed and save the pictures? y/n')
    if satisfied == 'y':
        for img in images:
            image = cv2.imread(img, int(bw))
            re = cv2.resize(image, (int(arr[0]), int(arr[1])))
            cv2.imwrite(os.path.join(final_destination, f"file{i}.png"), re)
            i = i + 1
    else:
        exit()
else:
    for img in images:
            image = cv2.imread(img, int(bw))
            re = cv2.resize(image, (int(arr[0]), int(arr[1])))
            cv2.imwrite(os.path.join(final_destination, f"file{i}.png"), re)
            i = i + 1
