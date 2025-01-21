import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner
from pymongo.mongo_client import MongoClient

qr_code = qrcode_scanner(key='qrcode_scanner')  


if qr_code:
  st.write(qr_code)

if st.button('UpdateDB'):
  client = MongoClient(st.secrets["uri"])
  db = client.MyData
  collection = db['MyData']
  new_data = {'desc': 'desc','name': 'username','qr':qr_code}
  collection.insert_one(new_data) 