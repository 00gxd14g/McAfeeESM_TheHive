#!/usr/bin/python3

#Author : Oğuz ALBAŞ
#Date   : 25.05.2020
#Version: 1.0
#Description: McAfee SIEM Open Case to TheHive API

# Copyright: GPLv3 (http://gplv3.fsf.org)
# Fell free to use the code, but please share the changes you've made

# Todo: open_case.py -t IOC_Saldırısı_Tespit_Edilmiştir. -d IOC_adresine_giden_zararli_tespit_edilmiştir -s 2
# And mcafee siem remote commands are: open_case.py -[$Rule_Message] -d [$Description] -s [$Severity]

import requests
import json
import sys
import argparse

        
parser = argparse.ArgumentParser()

parser.add_argument("-t", "--title", required=True, type=str, help="Case Adını giriniz")
parser.add_argument("-d", "--description", required=True, type=str, help="Açıklama giriniz")
parser.add_argument("-s", "--severity", required=True, type=int, help="Severity giriniz")

url = "http://35.223.199.75:9000/api/case"


args = parser.parse_args()


payload = json.dumps({
  "title": (args.title),
  "description": (args.description),
  "severity": (args.severity),
  "tlp": 3,
  "tags": [
    "oto",
    "siem_log_cek"
  ]
})

#Cookie alanına token girilmesi gerekmektedir.
#Token elde etmek için api/login post isteği yapılmalıdır.

headers = {
  'Content-Type': 'application/json',
  'Cookie': 'THEHIVE-SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImF1dGhDb250ZXh0Ijoie1widXNlcklkXCI6XCJiYnNAYmJzLmNvbVwiLFwidXNlck5hbWVcIjpcImJic1wiLFwib3JnYW5pc2F0aW9uXCI6XCJ-NDExMlwiLFwicGVybWlzc2lvbnNcIjpbXCJtYW5hZ2VTaGFyZVwiLFwibWFuYWdlQW5hbHlzZVwiLFwibWFuYWdlVGFza1wiLFwibWFuYWdlQ2FzZVRlbXBsYXRlXCIsXCJtYW5hZ2VDYXNlXCIsXCJtYW5hZ2VVc2VyXCIsXCJtYW5hZ2VQcm9jZWR1cmVcIixcIm1hbmFnZVBhZ2VcIixcIm1hbmFnZU9ic2VydmFibGVcIixcIm1hbmFnZVRhZ1wiLFwibWFuYWdlQ29uZmlnXCIsXCJtYW5hZ2VBbGVydFwiLFwiYWNjZXNzVGhlSGl2ZUZTXCIsXCJtYW5hZ2VBY3Rpb25cIl19IiwiZXhwaXJlIjoiMTY0NTQ5MjMxODIwMiIsIndhcm5pbmciOiIxNjQ1NDkyMDE4MjAyIn0sIm5iZiI6MTY0NTQ4ODcxOCwiaWF0IjoxNjQ1NDg4NzE4fQ.D79qF29u7ZOD_csi361UzVCxmtIOE6EgRTXsZqGVohE'
}

response = requests.request("POST", url, headers=headers, data=payload)
case_id = response.json()['id']

url2 = "http://35.223.199.75:9000/api/case/"+(case_id)+"/artifact"

print(payload)

payload2 = json.dumps({
  "dataType": "source_ip",
  "ioc": True,
  "sighted": False,
  "ignoreSimilarity": False,
  "tlp": 2,
  "message": "ip nin incelenmesi",
  "tags": [],
  "data": [
    "3.3.3.3"
  ]
})

case_ioc = requests.request("POST", url2, headers=headers, data=payload2)

print(case_ioc.text)
print(response.text)

    