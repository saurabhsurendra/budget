# -*- coding: utf-8 -*-

import streamlit as st
import pandas as pd

from infrastructure.db import get_connection

def format_indian_number(param):
    number = str(param)[::-1]
    # Add commas after the first three digits and then every two digits
    formatted_number = ",".join([number[:3]] + [number[i:i+2] for i in range(3, len(number), 2)])
    return param


def align_columns(dataframe):
    styled_df = dataframe.style.set_properties(
        subset=["Amount (Rs)"],  # Specify the column to style
        **{"text-align": "right"}  # Right-align text
    ).set_table_styles(
        [{"selector": "th", "props": [("text-align", "right")]}]  # Align header cells
    )
    return styled_df


def run_page():
    db = get_connection()
    budget_collection = db['budget_item']
    
    
    pipeline = [
        {
            "$group": {
                "_id": "$category",  # Group by category
                "total_amount": {"$sum": "$amount"}  # Sum the amounts
            }
        },
        {
            "$sort": {"_id": 1}  # Sort by category name
        }
    ]
    summary = list(budget_collection.aggregate(pipeline))
    grand_total = sum(item["total_amount"] for item in summary)
    
    
    formatted_summary = [{"Category": item["_id"], "Amount (Rs)": format_indian_number(item["total_amount"])} for item in summary]
    st.write(f"Grand total - {format_indian_number(grand_total)}")
    df = pd.DataFrame(formatted_summary)
    st.dataframe(df, use_container_width=True, hide_index=True)

    