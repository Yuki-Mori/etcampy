# etcampy
ETロボコンのカメラシステムにアクセスし，映像を取得するためのユーティリティツールです．

## Installation
以下のコマンドでインストールします．
インストールにはPython3以上が必要です．

```bash
$ git clone https://github.com/Yuki-Mori/etcampy.git
$ cd etcampy
$ python setup.py install
```

## Usage
カメラシステムに組み込まれているRaspberry PiのIPを `192.168.11.100` と仮定して説明します．
### カメラのキャリブレーション
ターミナルコマンドを通じてカメラにアクセスし，カメラの映像を見ることができます．

ターミナルで以下のコマンドを実行すると，カメラの映像を映し出すウィンドウが立ち上がります．
```bash
$ etcampy calib "http://192.168.11.100/?action=stream"
```
立ち上がったウィンドウ上で， `q` キーを打つと停止します．

また，何も指定しないとPCに付属のWebカメラで起動します．
```bash
$ etcampy calib
```

### スクリプト上からカメラにアクセスして画像を保存する．
以下のようにスクリプトを用いて画像を保存できます．

```python
import etcampy as ec

# ラズパイから取得
url = "http://192.168.11.100/?action=stream"
path = './test01.jpg'
ec.save_image(path,url)

# URLを指定しないとPCのWebカメラの画像を保存します．
path = './test02.jpg'
ec.save_image(path)
```
