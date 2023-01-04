import os
import cv2
import numpy as np
import sys

args = sys.argv
input_dir = 'input'
output_dir = 'output'
th_num = int(args[1])

def threshold(file_name, image_path, output_dir):
  img = cv2.imread(image_path)
  gray_name = os.path.join(output_dir, "img_gray", "gray_" + file_name)
  t1_name = os.path.join(output_dir, "img_t1", "t1_" + file_name)

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(gray_name,gray)
  ret,th1 = cv2.threshold(gray,th_num,255,cv2.THRESH_BINARY)
  cv2.imwrite(t1_name,th1)

for current_dir, sub_dirs, file_list in os.walk(input_dir):
  for file in file_list:
    file_info = os.path.splitext(file)
    file_name = file_info[0]
    ext = file_info[1]
    if ext == ".PNG" or ext == ".png":
      img_path = os.path.join(current_dir,file)
      threshold(file, img_path, output_dir)
