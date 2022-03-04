import requests
import json

url = "http://35.223.199.75:9000/api/case/~430128/artifact"

payload = json.dumps({
  "dataType": "signature_id",
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
headers = {
  'Authorization': 'Basic YmJzOmJicw==',
  'Content-Type': 'application/json',
  'Cookie': 'THEHIVE-SESSION=eyJhbGciOiJIUzI1NiJ9.eyJkYXRhIjp7ImF1dGhDb250ZXh0Ijoie1widXNlcklkXCI6XCJiYnNAYmJzLmNvbVwiLFwidXNlck5hbWVcIjpcImJic1wiLFwib3JnYW5pc2F0aW9uXCI6XCJ-NDExMlwiLFwicGVybWlzc2lvbnNcIjpbXCJtYW5hZ2VTaGFyZVwiLFwibWFuYWdlQW5hbHlzZVwiLFwibWFuYWdlVGFza1wiLFwibWFuYWdlQ2FzZVRlbXBsYXRlXCIsXCJtYW5hZ2VDYXNlXCIsXCJtYW5hZ2VVc2VyXCIsXCJtYW5hZ2VQcm9jZWR1cmVcIixcIm1hbmFnZVBhZ2VcIixcIm1hbmFnZU9ic2VydmFibGVcIixcIm1hbmFnZVRhZ1wiLFwibWFuYWdlQ29uZmlnXCIsXCJtYW5hZ2VBbGVydFwiLFwiYWNjZXNzVGhlSGl2ZUZTXCIsXCJtYW5hZ2VBY3Rpb25cIl19IiwiZXhwaXJlIjoiMTY0NTQ5MjMxODIwMiIsIndhcm5pbmciOiIxNjQ1NDkyMDE4MjAyIn0sIm5iZiI6MTY0NTQ4ODcxOCwiaWF0IjoxNjQ1NDg4NzE4fQ.D79qF29u7ZOD_csi361UzVCxmtIOE6EgRTXsZqGVohE'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
