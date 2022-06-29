from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import matplotlib.pyplot as plit
import json

api_key = open('9bac03f9f1d1dc4b5cf06c47b0550cc36a71afe54e43330c8bc7f7802c126d70','r').read()

company = "FB"
years = 2

income_statement = requests.get(f"https://financialmodelingprep.com/api/v3/income-statement/{company}?limit={years}apikey={api_key}")

income_statement = income_statement.json()

print(income_statement)

