# cheminfotutorial1023
material for cheminfo tutorial

## 関連情報
 - 開催日時: 2023年10月23日 13:00-17:00
 - 開催場所: 会場4会研修室

## 事前情報
 - 会場のネットワークが利用できるか不明です。Wifi等通信機器を必要に応じて。ご持参下さい。
 - 電源は主催者側で用意いたします。
 - 会場で環境を作ることはお薦めしません。事前に構築をしておきましょう。

## TS-01 ケモインフォマティクスチュートリアル
 - 中級者向けのケモインフォマティクスチュートリアルです

## Requirements
 - 本チュートリアルの資料はpython version 3.10にて作成しております

## 実施内容
1. 特定標的に関する特許から抽出した化合物データ解析
　データの前処理（正規化、脱塩など）ケミカルスペースの可視化、クラスタリング
2. 予測モデルの活用
　予測モデルの構築(データ準備,モデル最適化,モデル作成)
　予測モデルの利用した化合物の検証
3. 公共データを利用したVirtual Screeningの実施

## Prepare environments
 - 基本的にJupyterを使いチュートリアルを進めます
 - environments.ymlに記載してあるパッケージと合わせてvsflowのインストールが必要です。
 - 下記を参考に環境構築を事前に行ってきて下さい。うまく行かない場合は当日相談に乗ります。
 - 以下の例はCondaを利用した環境構築の手順です。condaを利用されない方は適宜必要なものを入れて下さい。
```
$ conda config --append channels conda-forge
$ conda env create -f environmnent.yml
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
