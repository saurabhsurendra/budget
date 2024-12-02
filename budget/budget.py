# -*- coding: utf-8 -*-

import streamlit as st

from infrastructure.db import get_connection
from infrastructure.constants import PAGE_HOME, PAGE_BUDGET

from page.budget_item import run_page as page_budget_run_page



def show_menu():
    with st.sidebar:
        if st.button("Home", use_container_width=True,
                     type=("primary" if st.session_state["page"] == PAGE_HOME else "secondary")):
            st.session_state["page"] = PAGE_HOME
            st.rerun()
        elif st.button("Budget", use_container_width=True,
                     type=("primary" if st.session_state["page"] == PAGE_BUDGET else "secondary")):
            st.session_state["page"] = PAGE_BUDGET
            st.rerun()
    
if "page" not in st.session_state:
    st.session_state["page"] = PAGE_HOME

st.set_page_config(layout="wide")
show_menu()

if st.session_state["page"] == PAGE_BUDGET:
    page_budget_run_page()