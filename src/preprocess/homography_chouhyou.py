import cv2
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

#from IPython.display import display, Image

#def display_cv_image(image, format='.png'):
#    decoded_bytes = cv2.imencode(format, image)[1].tobytes()
#    display(Image(data=decoded_bytes))

img_path = "/home/ocr_receipt/src/preprocess/"
img_name = "settai6.jpg"
org_name = img_path + "img/" + img_name
gray_name = img_path + "img_gray/gray_" + img_name
t1_name = img_path + "img_t1/t1_" + img_name
draw_name = img_path + "img_draw/draw_" + img_name
dst_name = img_path + "img_dst/dst_" + img_name
th1_ = img_path + "img_th1/th1_" + img_name

img = cv2.imread(org_name)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gray_name,gray)
ret,th1 = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
cv2.imwrite(t1_name,th1)

hist = cv2.calcHist([gray],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

# 輪郭抽出
contours, hierarchy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 面積の大きいもののみ選別
areas = []
for cnt in contours:
    area = cv2.contourArea(cnt)
    if area > 100000:
        epsilon = 0.1*cv2.arcLength(cnt,True)
        approx = cv2.approxPolyDP(cnt,epsilon,True)
        areas.append(approx)

cv2.drawContours(img,areas,-1,(0,255,0),3)
cv2.imwrite(draw_name,img)

img = cv2.imread(org_name)
dst = []
pts1 = np.float32(areas[0])
yoko = int(pts1[3][0][0] - pts1[0][0][0])
tate = int(pts1[1][0][1] - pts1[0][0][1])
pts2 = np.float32([[0,0],[0,tate],[yoko,tate],[yoko,0]])
#pts2 = np.float32([[300,600],[300,0],[0,0],[0,600]])

M = cv2.getPerspectiveTransform(pts1,pts2)
#dst = cv2.warpPerspective(img,M,(600,300))
dst = cv2.warpPerspective(img,M,(yoko,tate))
dst1 = cv2.warpPerspective(th1,M,(yoko,tate))

cv2.imwrite(dst_name,dst)
cv2.imwrite(th1_,dst1)

img = cv2.imread(dst_name)

gray_name = img_path + "img_gray/gray_1_" + img_name
t1_name = img_path + "img_t1/t1_1_" + img_name
draw_name = img_path + "img_draw/draw_1_" + img_name
dst_name = img_path + "img_dst/dst_1_" + img_name
th1_ = img_path + "img_th1/th1_1_" + img_name

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite(gray_name,gray)
ret,th1 = cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
cv2.imwrite(t1_name,th1)
