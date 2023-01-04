import os
import cv2
from PIL import Image
import pillow_heif

input_dir = 'input'
output_dir = 'output'
tran_ext = 'png'

def convert_heic(file_name, image_path, output_dir):
  heif_file = pillow_heif.read_heif(image_path)
  output_path = os.path.join(output_dir,file_name) + '.' + tran_ext
  for img in heif_file:
    image = Image.frombytes(
      img.mode,
      img.size,
      img.data,
      'raw',
      img.mode,
      img.stride
    )
    image.save(output_path, tran_ext)

for current_dir, sub_dirs, file_list in os.walk(input_dir):
  for file in file_list:
    file_info = os.path.splitext(file)
    file_name = file_info[0]
    ext = file_info[1]
    if ext == ".HEIC" or ext == ".heic":
      img_path = os.path.join(current_dir,file)
      convert_heic(file_name, img_path, output_dir)


#img = cv2.imread('./receipt_img/dst_img.jpg')
#cv2.imwrite('./receipt_img/dst_img.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION ),0])
#img = cv2.imread('./receipt_img/t1_img.jpg')
#cv2.imwrite('./receipt_img/t1_img.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION ),0])
#img = cv2.imread('./receipt_img/teiki.jpg')
#cv2.imwrite('./receipt_img/teiki.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION ),0])
#img = cv2.imread('./receipt_img/th1_dst_img.jpg')
#cv2.imwrite('./receipt_img/th1_dst_img.png', img, [int(cv2.IMWRITE_PNG_COMPRESSION ),0])

