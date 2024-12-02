# -*- coding: utf-8 -*-

import streamlit as st

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

@st.cache_resource
def get_connection():
    uri = st.secrets["mongo_secret"]["url"]
    client = MongoClient(uri, server_api=ServerApi('1'))
    return client["budgetapp"]
