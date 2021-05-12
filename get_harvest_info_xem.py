#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import datetime

if len(sys.argv) != 2:
    print('Usage:')
    print('  python3 get_harvest_info_xem.py [your_xem_address]')
    sys.exit(1)

args = sys.argv
address = args[1]

# baseUrl
baseUrl = "http://go.nem.ninja:7890/account/harvests?" + "address" + "=" + address

# get request
response = requests.get(baseUrl)
if response.status_code != requests.codes.ok:
    print("status code:" + str(response.status_code))
    print("Make sure the address you specified is correct.")
    sys.exit(1)

# response.json()でJSONデータに変換して変数へ保存
jsonData = response.json()

# ネメシスブロック日時
nemesisBlockTime = 1427587585

# ハーベスト回数
harvestCount = 0

# 出力csvのヘッダ記載
if jsonData['data'] != []:
    f = open('harvest_info_xem.csv', 'w', encoding='UTF-8')
    f.write('date,amount\n')

# 要素数が0で無い場合に繰り返す
while jsonData['data'] != []:
    # 要素数分繰り返す
    harvestCount += len(jsonData['data'])
    # 最後の要素のidを記録するための変数
    last_id = 0
    for jsonObj in jsonData['data']:
        timestamp = nemesisBlockTime + jsonObj['timeStamp']
        date = datetime.datetime.fromtimestamp(timestamp, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y/%m/%d %H:%M:%S")
        amount = str(jsonObj['totalFee'] / 1000000)
        f.write(date + "," + amount + '\n')
        # 要素のidを記録
        last_id = str(jsonObj['id'])
    # 最後の要素のidをqueryに追加して再度get request
    url = baseUrl + "&" + "id" + "=" + last_id
    # get request
    response = requests.get(url)
    # response.json()でJSONデータに変換して変数へ保存
    jsonData = response.json()

f.close()
print("Done.")
