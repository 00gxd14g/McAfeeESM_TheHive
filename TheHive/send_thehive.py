#!/usr/bin/python3

#Author : 0gxd14g
#Date   : 25.05.2020
#Version: 1.1
#Copyright: GPLv3 (http://gplv3.fsf.org)
#Fell free to use the code, but please share the changes you've made

import requests
import json
import sys
import argparse

def main():
    
    args = parser.parse_args()
    url = "http://"+(args.thehiveip)+":9000/api/login"
    payload = json.dumps({
    "user":(args.username),
    "password":(args.password)
    })
    
    headers = {'Content-Type': 'application/json'}
    response = requests.request("POST", url, headers=headers, data=payload)
    cookie = response.headers['Set-Cookie']
    
    case_url = "http://"+(args.thehiveip)+":9000/api/case"
    
    payload = json.dumps({
    
    "title": (args.title),
    "description": (args.description),
    "severity": (args.severity),
    "tlp": 3,
    "tags": [
    "",
    ""
    ]
    })
    
    headers2 = {
    'Content-Type': 'application/json',
    'Cookie': cookie
    }
    
    open_case = requests.request("POST", case_url, headers=headers2, data=payload)
    
    case_id = open_case.json()['id']
    case_title = open_case.json()['title']
    
    url3 = "http://"+(args.thehiveip)+":9000/api/case/"+(case_id)+"/artifact"

    print(payload)

    payload2 = json.dumps({
    "dataType": "source_ip",
    "ioc": True,
    "sighted": False,
    "ignoreSimilarity": False,
    "tlp": 2,
    "message": "Alarm Source Address",
    "tags": [],
    "data": [
    "3.3.3.3"
  ]
    })

    case_ioc = requests.request("POST", url3, headers=headers2, data=payload2)
    print(case_ioc.text)
       
parser = argparse.ArgumentParser()

parser.add_argument("-thehiveip", "--thehiveip", help="The Hive IP", required=True)
parser.add_argument("-t", "--title", required=True, type=str, help="Case Title")
parser.add_argument("-d", "--description", required=True, type=str, help="Case Description")
parser.add_argument("-s", "--severity", required=True, type=int, help="Case Severity")
parser.add_argument("-u", "--username", required=True, type=str, help="TheHive Username")
parser.add_argument("-p", "--password", required=True, type=str, help="TheHive Password")
parser.add_argument("-i", "--ip", required=True, type=str, help="Alarm Source IP")

main()    
    

    
