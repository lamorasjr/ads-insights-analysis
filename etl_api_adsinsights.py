import pandas as pd
import requests
import json
import configparser

parser = configparser.ConfigParser()
parser.read("config.conf")

access_token = parser.get("metaads_config", "token")
adaccount_id = parser.get("metaads_config", "adaccount_id")

base_url = "https://graph.facebook.com/v18.0/"

endpoint = f"{adaccount_id}/insights"

api_url = base_url + endpoint

headers = {"Authorization": "Bearer " + access_token}

params = {
      "time_range" : "{'since':'2023-10-01','until':'2023-10-31'}",
      "time_increment" : "1",
      "level" : "ad",
      "fields" : "account_id,campaign_id,adset_id,ad_id,date_start,date_stop,spend,account_currency,reach,impressions,frequency,inline_link_clicks,clicks,inline_post_engagement,actions"
  }

try:
  response = requests.get(api_url, headers=headers, params=params)
  content = json.loads(response.text)

except:
  print('Falha na solicitação:', response.status_code)

print(content["data"][0])