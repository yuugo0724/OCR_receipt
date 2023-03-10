import pyocr
import pyocr.builders
import cv2
from PIL import Image
import numpy as np

tools = pyocr.get_available_tools()
tool = tools[0]

def get_box(img, tool, show=True):
  """
  img:PIL.Image.Image
  """
  results = tool.image_to_string(
    img,
    lang='jpn',
    builder=pyocr.builders.LineBoxBuilder(tesseract_layout=6)
  )
  img_np = np.array(img)
  w, h = img_np.shape[0], img_np.shape[1]
  for box in results:
    if box.content == ' ' or box.content == '':
        continue
    if (box.position[0][0] == 0) and (box.position[0][1] == 0) and (box.position[1][0] == w) and (box.position[1][1] == h):
      continue
    cv2.rectangle(img_np, box.position[0], box.position[1], (0, 255, 0), 1)
  #if show:
  #    display(Image.fromarray(img_np))
  return img_np, results

def split_images(img, h_split, w_split):
  """
  画像を分割し、分割後の画像と元画像における座標を返す
  img:numpy
  """
  h,w = img.shape[0],img.shape[1]
  images = []
  new_h = int(h / h_split)
  new_w = int(w / w_split)
  start_coordinates = []
  for _h in range(h_split):
    h_start = _h * new_h
    h_end = h_start + new_h
    for _w in range(w_split):
      w_start = _w * new_w
      w_end = w_start + new_w
      images.append(img[h_start:h_end, w_start:w_end])
      #images.append(img[h_start:h_end, w_start:w_end, :])
      coordinate = {}
      coordinate['h_start'] = h_start
      coordinate['h_end'] = h_end
      coordinate['w_start'] = w_start
      coordinate['w_end'] = w_end
      start_coordinates.append(coordinate)
    return images, start_coordinates

def get_splitImages2originalPositins(images, img_resize, start_coordinates, show=True):
  """
  分割後の画像それぞれのどこに文字があるかどうかを識別する
  また、それらの結果を元の座標系に戻してpositionsとして返す
  images:list
  img_resize:numpy
  start_coordinates:list
  """
  positions = []
  for i, (img, coordinate)  in enumerate(zip(images, start_coordinates)):
    bb,results = get_box(Image.fromarray(img), tool, show=False)
    w,h = img.shape[0],img.shape[1]
    for box in results:
      if box.content == ' ' or box.content == '':
        continue
      if (box.position[0][0] == 0) and (box.position[0][1] == 0) and (box.position[1][0] == w) and (box.position[1][1] == h):
        continue
      
      position = [[p[0],p[1]] for p in box.position]
      position[0][0] += coordinate['w_start']
      position[0][1] += coordinate['h_start']
      position[1][0] += coordinate['w_start']
      position[1][1] += coordinate['h_start']
      cv2.rectangle(img_resize, position[0], position[1], (0, 255, 0), 1)
      positions.append(position)
  #if show:
  #    display(Image.fromarray(img_resize))
  return positions

def get_mask(img, positions):
  mask = np.zeros_like(img)
  for p in positions:
    cv2.rectangle(mask, p[0], p[1], (255, 255, 255), thickness=-1)
  return mask

def results2positions(results):
  positions = []
  for box in results:
    if box.content == ' ' or box.content == '':
      continue
    if (box.position[0][0] == 0) and (box.position[0][1] == 0) and (box.position[1][0] == w) and (box.position[1][1] == h):
      continue
    positions.append([box.position[0], box.position[1]])
  return positions

base_dir = '/home/ocr_receipt1/src1/img/'
img_name = 'wikipedia.png'
img_org_path = base_dir + "org/" + img_name
get_box_path = base_dir + "get_box/get_box_" + img_name
resize_path = base_dir + "resize/resize_" + img_name
mask_resize_path = base_dir + "mask_resize/mask_resize_" + img_name
find_str_path = base_dir + "find_str/find_str_" + img_name
org_mask_path = base_dir + "org_mask/org_mask_" + img_name

img_org = Image.open(img_org_path)

img_np,results = get_box(img_org,tool)
cv2.imwrite(get_box_path,img_np)

# 画像の拡大
img_resize = cv2.resize(img_np, (int(img_np.shape[1] * 4), int(img_np.shape[0] * 4)), interpolation=cv2.INTER_CUBIC)
#img_resize = cv2.resize(img_np, (int(img_np.shape[0] * 4), int(img_np.shape[1] * 4)), interpolation=cv2.INTER_CUBIC)
cv2.imwrite(resize_path,img_resize)

# 画像を分割する
images, start_coordinates = split_images(np.array(img_resize), 5, 5)
# 分割画像のそれぞれをOCRに入れ、どこに文字が有るか判定する
# また、このときに返ってくるpositionsには、分割前の座標系でどこに文字があったのかが示されている
positions = get_splitImages2originalPositins(images, img_resize, start_coordinates, show=False)
# 分割画像から特定された文字の位置がマスクになるようにする
mask_resize = get_mask(img_resize, positions)
cv2.imwrite(mask_resize_path,mask_resize)

# 元の画像サイズに戻す
mask_resize = cv2.resize(mask_resize, (img_np.shape[0],img_np.shape[1]))

# リサイズ画像を分割せずに、どこに文字が有るかを求める
img_np, results = get_box(img_org, tool, show=False)
cv2.imwrite(find_str_path,img_np)

positions = results2positions(results)
# リサイズ画像から特定された文字の位置がマスクになるようにする
original_mask = get_mask(img_np, positions)
cv2.imwrite(org_mask_path,original_mask)


# mask_resize（分割画像）とoriginal_mask（リサイズ画像）のORを求める
#bitwise_or = cv2.bitwise_or(original_mask[:,:], mask_resize[:,:])
#bitwise_or = cv2.bitwise_or(original_mask[:,:,0], mask_resize[:,:,0])

