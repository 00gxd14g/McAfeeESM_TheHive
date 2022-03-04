import sys
import getpass
import requests
import time
import logging
import json
import os

from argparse import ArgumentParser, RawTextHelpFormatter
from datetime import datetime, timedelta

base_url = 'soc.mcafee.com'

title = 'McAfee EDR Python API'

usage = """python mvision_edr_threats.py -R <REGION> -U <USERNAME> -P <PASSWORD> -D <DETAILS> -L <MAX RESULTS> -S <SYSLOG IP> -SP <SYSLOG PORT>"""
parser = ArgumentParser(description=title, usage=usage, formatter_class=RawTextHelpFormatter)

parser.add_argument('--user', '-U',
                        required=True, type=str,
                        help='MVISION EDR Username')

parser.add_argument('--password', '-P',
                        required=False, type=str,
                        help='MVISION EDR Password')

parser.add_argument('--limit', '-L',
                        required=True, type=int,
                        help='Maximum number of returned items')

args = parser.parse_args()


request = requests.Session()

user = args.user
pw = args.password
creds = (user, pw)
limit = args.limit

pattern = '%Y-%m-%dT%H:%M:%S.%fZ'
cache_fname = 'cache.log'
if os.path.isfile(cache_fname):
    cache = open(cache_fname, 'r')
    last_detection = datetime.strptime(cache.read(), '%Y-%m-%dT%H:%M:%SZ')
    now = datetime.astimezone(datetime.now())
    hours = int(str(now)[-5:].split(':')[0])
    minutes = int(str(now)[-5:].split(':')[1])

    last_pulled = (last_detection + timedelta(hours=hours, minutes=minutes, seconds=1)).strftime(pattern)
            #logger.debug('Cache exists. Last detection date UTC: {0}'.format(last_detection))
            #logger.debug('Pulling newest threats from: {0}'.format(last_pulled))
    cache.close()

    last_check = (last_detection + timedelta(seconds=1)).strftime(pattern)

else:
    #logger.debug('Cache does not exists. Pulling data from last 7 days.')
    last_pulled = (datetime.now() - timedelta(days=7)).strftime(pattern)
    last_check = (datetime.now() - timedelta(days=7)).strftime(pattern)

    limit = args.limit
    


def auth():  
        res = request.get('https://api.' +base_url + '/identity/v1/login', auth=creds)
        if res.ok:
                token = res.json()['AuthorizationToken']
                request.headers = {'Authorization': 'Bearer {}'.format(token)}
                #print('Authenticated',token)
                #logger.debug('Successfully authenticated')
        else:
                #logger.error('Error in edr.auth(). Error: {0} - {1}'
                 #                 .format(str(res.status_code), res.text))
            sys.exit()
            
def get_threats():
    epoch_before = int(time.mktime(time.strptime(last_pulled, pattern)))
    filter = {}
    severities = ["s0", "s1", "s2", "s3", "s4", "s5"]
    filter['severities'] = severities
    
    res = request.get(
                'https://api.{0}/ft/api/v2/ft/threats?sort=-lastDetected&filter={1}&from={2}&limit={3}'
                .format(base_url, json.dumps(filter), str(epoch_before * 1000), str(limit)))
    if res.ok:
        threats = res.json()
        #print(threats)
        #logger.debug('Successfully retrieved threats')
        for threat in threats['threats']:
            detections = threat['name']
            print(detections)
            
            
            
            
auth()
get_threats()