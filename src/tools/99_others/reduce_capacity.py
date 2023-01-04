from PIL import Image

# PNG画像を8bitカラーに変換して減色
# 表現力が落ちるが、画質を保ったまま画像容量を大幅に削減できる
img = Image.open('./receipt_img/th1_dst_img_resize.png')
img_p = img.convert('P')
img_p.save('./receipt_img/th1_dst_img_resize_P.png')