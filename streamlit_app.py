import requests
import json
import pandas as pd

filing_url = "https://www.sec.gov/ix?doc=/Archives/edgar/data/1809519/000095017022002348/gdrx-20211231.htm"

xbrl_converter_api_endpoint = "https://api.sec-api.io/xbrl-to-json"

final_url = xbrl_converter_api_endpoint + "?htm-url=" + filing_url + "&token=" + api_key

response = requests.get(final_url)

xbrl_json = json.loads(response.text)

print(json.dumps(xbrl_json['StatementsOfIncome']['RevenueFromContractWithCustomerExcludingAssessedTax'][0:2], indent=1)) 
