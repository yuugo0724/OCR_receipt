import os
import cv2

input_dir = 'input'
output_dir = 'output'
tran_ext = 'png'

def convert_to_png(file_name, image_path, output_dir):
  output_path = os.path.join(output_dir,file_name) + '.' + tran_ext
  img = cv2.imread(image_path)
  cv2.imwrite(output_path, img, [int(cv2.IMWRITE_PNG_COMPRESSION ),0])

for current_dir, sub_dirs, file_list in os.walk(input_dir):
  for file in file_list:
    file_info = os.path.splitext(file)
    file_name = file_info[0]
    ext = file_info[1]
    if ext == ".JPEG" or ext == ".JPG" or ext == ".jpeg" or ext == ".jpg":
      img_path = os.path.join(current_dir,file)
      convert_to_png(file_name, img_path, output_dir)
