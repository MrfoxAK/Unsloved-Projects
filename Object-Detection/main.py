import cv2
import matplotlib.pyplot as plt



conig_file = "ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
frozen_model = "frozen_inference_graph.pb"

model = cv2.dnn.readNetFromONNX(frozen_model,conig_file)
# model = cv2.dnn_DetectionModel(frozen_model,conig_file)


classLabels = []
f_name = "coco.names"

with open(f_name,'rt') as f:
    classLabels = f.read().rstrip('\n').split('\n')

print(classLabels)









