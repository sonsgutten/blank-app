import streamlit as st  
from streamlit_qrcode_scanner import qrcode_scanner
from pymongo.mongo_client import MongoClient
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities import (CredentialsError,
                                               ForgotError,
                                               Hasher,
                                               LoginError,
                                               RegisterError,
                                               ResetError,
                                               UpdateError)

# Loading config file
with open('config.yaml', 'r', encoding='utf-8') as file:
    config = yaml.load(file, Loader=SafeLoader)


# Creating the authenticator object
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days']
)

# Creating a guest login button
try:
    authenticator.experimental_guest_login('Login with Google', provider='google',
                                            oauth2=st.session_state["oauth2"])
    authenticator.experimental_guest_login('Login with Microsoft', provider='microsoft',
                                            oauth2=config['oauth2'])
except LoginError as e:
    st.error(e)

# Authenticating user
if st.session_state['authentication_status']:
    authenticator.logout()
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
    qr_code = qrcode_scanner(key='qrcode_scanner')  


    if qr_code:
      st.write(qr_code)

    if st.button('UpdateDB'):
      client = MongoClient(st.secrets["uri"])
      db = client.MyData
      collection = db['MyData']
      new_data = {'desc': 'desc','name': 'username','qr':qr_code}
      collection.insert_one(new_data) 




elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')




# Saving config file
with open('config.yaml', 'w', encoding='utf-8') as file:
    yaml.dump(config, file, default_flow_style=False)













qr_code = qrcode_scanner(key='qrcode_scanner')  












if qr_code:
  st.write(qr_code)

if st.button('UpdateDB'):
  client = MongoClient(st.secrets["uri"])
  db = client.MyData
  collection = db['MyData']
  new_data = {'desc': 'desc','name': 'username','qr':qr_code}
  collection.insert_one(new_data) 
