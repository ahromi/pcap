import requests
from pprint import pprint
import json

rget = requests.get('https://mentor.corp.google.com/apps/eve/fusion?pr=GLOBAL_REVIEW_2&id=com.hypnoticowl.prime&sub=151')
pprint(rget.text)