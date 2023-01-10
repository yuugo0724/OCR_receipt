import os
import cv2
import numpy as np

input_dir = 'input'
output_dir = 'output'
threshold_count = 10000

def homography(file_name, image_path, output_dir):
  img = cv2.imread(image_path)
  gray_name = os.path.join(output_dir, "img_gray", "gray_" + file_name)
  t1_name = os.path.join(output_dir, "img_t1", "t1_" + file_name)
  draw_name = os.path.join(output_dir, "img_draw", "draw_" + file_name)
  dst_name = os.path.join(output_dir, "img_dst", "dst_" + file_name)
  th1_name = os.path.join(output_dir,"img_th1", "th1_" + file_name)

  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(gray_name,gray)
  ret,th1 = cv2.threshold(gray,190,255,cv2.THRESH_BINARY)
  cv2.imwrite(t1_name,th1)

  # 輪郭抽出
  contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

  # 面積の大きいもののみ選別
  areas = []
  for cnt in contours:
      area = cv2.contourArea(cnt)
      if area > threshold_count:
          epsilon = 0.1*cv2.arcLength(cnt,True)
          approx = cv2.approxPolyDP(cnt,epsilon,True)
          areas.append(approx)

  cv2.drawContours(img,areas,-1,(0,255,0),3)
  cv2.imwrite(draw_name,img)

for current_dir, sub_dirs, file_list in os.walk(input_dir):
  for file in file_list:
    file_info = os.path.splitext(file)
    file_name = file_info[0]
    ext = file_info[1]
    if ext == ".PNG" or ext == ".png":
      img_path = os.path.join(current_dir,file)
      homography(file, img_path, output_dir)
