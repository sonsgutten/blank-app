import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner
from pymongo.mongo_client import MongoClient

qr_code = qrcode_scanner(key='qrcode_scanner')  
client = MongoClient(st.secrets["uri"])
db = client.MyData
collection = db['MyData']


if qr_code:
  st.write(qr_code)
  new_data={'qr':qr_code}
  collection.insert_one(new_data) 

