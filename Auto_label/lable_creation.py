import cv2
import os
import time
from ultralytics import YOLO

classes = 3
model = YOLO('yolov8n-pose.pt')

# for each class 
for my_class in range(classes):
    directory = "./captured_images/" + str(my_class)
    sorted_list = os.listdir(directory)
    sorted_list.sort() 

    # for each images 
    for image in sorted_list:
        path_to_img = directory + "/"+ image
        image_name, extension = os.path.splitext(image)

        results = model.track(path_to_img,save=True) 

        tensor_data_Keypoints = results[0].keypoints.xyn
        tensor_data_bounding_box = results[0].boxes.xywhn

        with open('./data/labels/train/'+ image_name + ".txt",'w') as file:
            
            i = 0

            for bounding_box in tensor_data_bounding_box:
            
                file.write("{} ".format(my_class))

                # file.write("\n")

                for coord in bounding_box:
                    file.write("{} ".format(coord))

                # file.write("\n")

            # for i in range(tensor_data_Keypoints.size(0)):

                for j in range(tensor_data_Keypoints.size(1)):
                    flag = 0
                    for k in range(tensor_data_Keypoints.size(2)):
                        # Write element to file
                        file.write("{} ".format(tensor_data_Keypoints[i, j, k]))
                        if(tensor_data_Keypoints[i, j, k] == 0):
                            flag = 1
                    if(flag == 1):
                        file.write("0 ")
                    else: 
                        file.write("2 ")
                file.write("\n")
                i += 1