# get_harvest_info_xem

XEMのハーベスト履歴を取得してCSV出力するツールです。
自分用に作ったのでバグがあるかもしれませんが、シンプルな内容なので簡単にお使い頂けると思います。

## 前提(premise)

* `python3`コマンドが実行可能
* MacOSでのみ動作確認しました。

## 準備(preparation)

$ curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
$ python3 get-pip.py
$ pip3 install requests

## 実行(execution)

$ git clone https://github.com/kkogr/get_harvest_info_xem.git
$ cd get_harvest_info_xem
$ python3 get_harvest_info_xem.py [address]

## 結果(output)

以下のような内容のharvest_info_xem.csvというcsvファイルが生成されます。

```
date,amount
2021/05/02 00:25:37,0.0
2021/04/21 00:19:17,0.0
2021/04/19 22:56:37,4.05
・
・
・
```
