import cv2
import numpy as np

img_dir = '/home/ocr_receipt1/src1/report_img/'
report_name = 'wakusen.png'
edges_name = 'wakusen_edges.png'
out_name = 'wakusen_out.png'
img_report = img_dir + report_name
img_edges = img_dir + edges_name
img_out = img_dir + out_name

img = cv2.imread(img_report)

# BGR -> グレースケール
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# エッジ抽出 (Canny)
edges = cv2.Canny(gray, 1, 100, apertureSize=3)
cv2.imwrite(img_edges, edges)
# 膨張処理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
edges = cv2.dilate(edges, kernel)
# 輪郭抽出
contours, hierarchy = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# 面積でフィルタリング
rects = []
for cnt, hrchy in zip(contours, hierarchy[0]):
    if cv2.contourArea(cnt) < 1000:
        continue  # 面積が小さいものは除く
    if hrchy[3] == -1:
       continue  # ルートノードは除く
    # 輪郭を囲む長方形を計算する。
    rect = cv2.minAreaRect(cnt)
    rect_points = cv2.boxPoints(rect).astype(int)
    rects.append(rect_points)

# x-y 順でソート
rects = sorted(rects, key=lambda x: (x[0][1], x[0][0]))

# 描画する。
for i, rect in enumerate(rects):
    color = np.random.randint(0, 255, 3).tolist()
    cv2.drawContours(img, rects, i, color, 2)
    cv2.putText(img, str(i), tuple(rect[0]), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
    
    print('rect:\n', rect)

cv2.imwrite(img_out, img)
