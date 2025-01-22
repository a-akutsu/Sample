import cv2
import glob
import time
import sys
from datetime import datetime

# 0にするとmacbookのカメラ、1にすると外付けのUSBカメラにできる
cap = cv2.VideoCapture(0)

# 顔判定で使うxmlファイルを指定する。(opencvのpathを指定)
cascade_path = '"opencvの格納されているパス"/data/haarcascades/haarcascade_frontalface_alt.xml'
cascade = cv2.CascadeClassifier(cascade_path)

# 写真を格納するフォルダを指定
dir = "任意のフォルダパス"

# 欲しいファイルの数
num = 300
label = str(input("人を判別するを半角英数3文字でで入力してください ex.slf："))

# 現在のフォルダ内のファイル数
file_number = len(glob.glob("任意のフォルダパス/*"))

# 撮影した写真枚数の初期値
count = 0

# ラベルの文字数を確認
if not len(label) == 3:
    print("半角英数3文字で入力してください")
    sys.exit()

while True:
    # フォルダの中に保存された写真の枚数がnum以下の場合は撮影を続ける
    if count < num:
        # cap reflesh
        time.sleep(0.01)
        print("あと{}枚です".format(num-count))

        # 撮影時間
        now = datetime.now()
        r, img = cap.read()

        # 結果を保存するための変数を用意しておく
        img_result = img

        # グレースケールに変換
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # 顔判定 minSize で顔判定する際の最小の四角の大きさを指定できる。(小さい値を指定し過ぎると顔っぽい小さなシミのような部分も判定されてしまう。)
        faces = cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))

        # 顔があった場合
        if len(faces) > 0:
            # 複数の顔があった場合、１つずつ四角で囲っていく
            for face in faces:
                # faceには(四角の左上のx座標, 四角の左上のy座標, 四角の横の長さ, 四角の縦の長さ) が格納されている。
                # 顔だけ切り出して保存
                x = face[0]
                y = face[1]
                width = face[2]
                height = face[3]
                # 50×50の大きさにリサイズ
                roi = cv2.resize(img[y:y + height, x:x + width], (50, 50), interpolation=cv2.INTER_LINEAR)
                cv2.imwrite(dir+label+"__"+str(now)+'.jpg', roi)

        # 現在の写真枚数から初期値を減産して、今回撮影した写真の枚数をカウント
        count = len(glob.glob("/任意のフォルダパス/*")) - file_number

    # フォルダの中に保存された写真の枚数がnumを満たしたので撮影を終える
    else:
        break

# カメラをOFFにする
cap.release()
