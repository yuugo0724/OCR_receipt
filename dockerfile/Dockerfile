# ベースイメージの指定
FROM python:3.9-slim

# メタ情報
LABEL maintainer="ygaoqiao742@gmail.com"
LABEL version="1.0"
LABEL description="ocr_receipt用のpythonイメージ"

# rootのパスワード設定
RUN echo "root:Cb8a0e1f-1784" | chpasswd

# 環境変数
ENV USER ocr_receipt

# 一般権限のユーザを追加
RUN useradd -m ${USER}
# sudo権限を付与
RUN gpasswd -a ${USER} sudo
# パスワード設定
RUN echo "${USER}:Cb8a0e1f-1784" | chpasswd
# apt更新
RUN apt update
RUN apt list --upgradable
# 必要なパッケージのインストール
RUN apt install -y git \
    wget \
    unzip \
    libgl1-mesa-dev \
    libglib2.0-0 \
    tk-dev
# ユーザの切り替え
USER ${USER}

# PATHを追加
ENV PATH $PATH:/home/${USER}/.local/bin/
# 作業ディレクトリを変更
WORKDIR /tmp/work

# pipでインストールするパッケージを記載したテキストファイル
COPY requirements.txt ${PWD}
# pipアップグレード
RUN pip install --upgrade pip
# pip実行
RUN pip install -r requirements.txt
RUN pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

# 作業ディレクトリを変更
WORKDIR /home/ocr_receipt
# ソースコードを配置するディレクトリを作成
RUN mkdir /home/ocr_receipt/src/

# OCR_Japaneaseの準備
RUN cd /home/ocr_receipt/src/
RUN git clone https://github.com/tanreinama/OCR_Japanease.git
RUN git clone https://github.com/JingyunLiang/SwinIR.git
RUN wget https://nama.ne.jp/models/ocr_jp-v2.zip
RUN unzip ocr_jp-v2.zip
