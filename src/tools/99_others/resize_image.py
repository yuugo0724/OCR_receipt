import cv2

img = cv2.imread('./receipt_img/dst_img.png')
img_info = img.shape
y_img = int(img_info[0]/2)
x_img = int(img_info[1]/2)
dst = cv2.resize(img,dsize=(x_img,y_img))
cv2.imwrite('./receipt_img/dst_img_resize.png', dst)

img = cv2.imread('./receipt_img/t1_img.png')
img_info = img.shape
y_img = int(img_info[0]/2)
x_img = int(img_info[1]/2)
dst = cv2.resize(img,dsize=(x_img,y_img))
cv2.imwrite('./receipt_img/t1_img_resize.png', dst)

img = cv2.imread('./receipt_img/teiki.png')
img_info = img.shape
y_img = int(img_info[0]/2)
x_img = int(img_info[1]/2)
dst = cv2.resize(img,dsize=(x_img,y_img))
cv2.imwrite('./receipt_img/teiki_resize.png', dst)

img = cv2.imread('./receipt_img/th1_dst_img.png')
img_info = img.shape
y_img = int(img_info[0]/10)
x_img = int(img_info[1]/10)
print(y_img)
print(x_img)
dst = cv2.resize(img,dsize=(x_img,y_img))
cv2.imwrite('./receipt_img/th1_dst_img_resize.png', dst)
