#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import json
import datetime

args = sys.argv
address = args[1]
print (address)

# url
url = "http://alice6.nem.ninja:7890/account/harvests?" + "address" + "=" + address
print (url)

# get request
response = requests.get(url)

# response.json()でJSONデータに変換して変数へ保存
jsonData = response.json()

# ネメシスブロック日時
nemesisBlockTime = 1427587585

for jsonObj in jsonData['data']:
    timestamp = nemesisBlockTime + jsonObj['timeStamp']
    date = datetime.datetime.fromtimestamp(timestamp, datetime.timezone(datetime.timedelta(hours=9))).strftime("%Y/%m/%d %H:%M:%S")
    amount = str(jsonObj['totalFee'] / 1000000)
    print(date + "," + amount)
