# cheminfotutorial1023
material for cheminfo tutorial

## 関連情報
 - 開催日時: 2023年10月23日 13:00-17:00
 - 開催場所: 会場4階研修室

## 事前情報
 - 会場のネットワークは利用できますが、速度は期待できないとお考えください(必要に応じてWifi等通信機器をご持参下さい)。
 - 電源は主催者側で用意いたします。
 - 環境構築には時間がかかるため、会場で環境を作ることは推奨しません。事前に構築をしてください。

## TS-01 ケモインフォマティクスチュートリアル
 - 中級者向けのケモインフォマティクスチュートリアルですので、基本的なjupyter notebook,pythonの操作に関しては理解しているという前提ですすめます。

## Requirements
 - 本チュートリアルの資料はpython version 3.10にて作成しておりますが、下記(Prepare environments)を参照してください。

## 実施内容
1. 特定標的に関する特許から抽出した化合物データ解析
    1. データの前処理（正規化、脱塩など）ケミカルスペースの可視化、クラスタリング
       
1. 予測モデルの活用
    1. 予測モデルの構築(データ準備,モデル最適化,モデル作成)
    1. 予測モデルの利用した化合物の検証
       
1. 公共データを利用したVirtual Screeningの実施

## Prepare environments
 - 基本的にJupyterを使いチュートリアルを進めます
 - environments.ymlに記載してあるパッケージと合わせてvsflowのインストールが必要です。
 - 下記を参考に環境構築を事前に行ってきて下さい。うまく行かない場合は当日までに[Discussions](https://github.com/cbi-society/cheminfotutorial1023/discussions)で質問してもらえれば対応します。

```
$ conda config --append channels conda-forge
$ conda env create -f environment.yml
$ conda activate cbi2023

### 下記のコマンドを実行

$ git clone https://github.com/czodrowskilab/VSFlow.git
$ cd VSFlow
$ pip install .

```

## Author
 - 大川 和史（旭化成ファーマ株式会社）
 - 新井　浩一郎（旭化成ファーマ株式会社）
 - 高橋 一敏（味の素株式会社）
 - 芹沢 貴之（第一三共株式会社）
 - 宮野 奈津美（帝人ファーマ株式会社）
