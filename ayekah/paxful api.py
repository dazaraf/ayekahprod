# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:09:39 2020

@author: Alain Rosen
"""
import pandas as pd
import json
import requests
from datetime import datetime, timedelta
import csv
from matplotlib import pyplot as plt
import urllib
from urllib.parse import urlencode
import yfinance as yf
import time
import hmac
from hashlib import sha256



API_URL = "https://paxful.com/data/trades?sincetype=date&since=1577836800&page=2"
API_KEY = "AlNFwzOtUMaJqIBcAYWxD0mCX2IgqB3H"
API_SECRET = "lgRB8TOGleC15xc1SdPmM1o4fFX5wljk"
nonce = int(time.time())

payload = {"apikey": API_KEY, "nonce": nonce}
payload = urlencode(sorted(payload.items()))
apiseal = hmac.new(API_SECRET.encode(), payload.encode(), sha256).hexdigest()
data_with_apiseal = payload + "&apiseal=" + apiseal
headers = {"Accept": "application/json", "Content-Type": "text/plain"}
resp = requests.get(API_URL, data=data_with_apiseal, headers=headers)
data = list(eval(resp.content))
df = pd.DataFrame(data)
df['date'] = df['date'].astype(int)