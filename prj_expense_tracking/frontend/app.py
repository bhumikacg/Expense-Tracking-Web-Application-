import streamlit as st
from add_update_ui import add_update_tab
from analytics_ui import analytics_tab

st.title("Expense Tracking System")

tab1, tab2 = st.tabs(["Add/Update", "Analytics"])

with tab1:
    add_update_tab()

with tab2:
    analytics_tab()





# import streamlit as st
# from datetime import datetime
# import requests
#
# API_URL = "http://localhost:8000"
#
# st.title("Expense Tracking System")
# tab1, tab2 =st.tabs(["Add/Update", "Analysts"])
#
# with tab1:
#     selected_date = st.date_input("Enter Date",datetime(2024,8,1),label_visibility = "collapsed")
#     response = requests.get(f"{API_URL}/expenses/{selected_date}")
#     if response.status_code == 200:
#         existing_expenses = response.json()
#         st.write(existing_expenses)
#     else:
#         st.error("Failed to retrieve expenses")
#         existing_expenses =[]
#
#     categories = ["Rent","Food","Shopping","Entertainment","Other"]
#
#     with st.form(key = "expense_form"):
#         #Display column headers
#         col1, col2,col3 = st.columns(3)
#         with col1:
#             st.text("Amount")
#         with col2:
#             st.text("Category")
#         with col3:
#             st.text("Notes")
#
#         expenses = []
#
#         for i in range(5):
#             if i < len(existing_expenses):
#                 amount = existing_expenses[i]["amount"]
#                 category = existing_expenses[i]["category"]
#                 notes = existing_expenses[i]["notes"]
#             else:
#                 amount =0.0
#                 category = "Shopping"
#                 notes = ""
#
#             col1,col2,col3 = st.columns(3)
#             with col1:
#                 amount_input = st.number_input("Amount",min_value =0.0 ,step = 1.0 , value =amount,key = f"amount_{selected_date}_{i}",label_visibility ="collapsed")
#             with col2:
#                 category_input = st.selectbox(label = "Category", options = categories, index = categories.index(category),key =f"category_{selected_date}_{i}",label_visibility ="collapsed")
#
#             with col3:
#                 notes_input = st.text_input(label = "Notes",value=notes,key = f"notes_{selected_date}_{i}",label_visibility ="collapsed")
#
#             expenses.append({
#                 "amount": amount_input,
#                 "category": category_input,
#                 "notes": notes_input
#             })
#
#         submit_button = st.form_submit_button()
#         if submit_button:
#             filtered_expenses = [expense for expense in expenses if expense['amount']>0]
#             requests.post(f"{API_URL}/expenses/{selected_date}",json = filtered_expenses)
#             if response.status_code == 200:
#                 st.success("Expenses updated successfully!")
#             else :
#                 st.error("Failed to update expenses.")

######################################################################################################
#import pandas as pd

#part 1
# st.title("Expense Management System")
#
# expense_dt = st.date_input("Expense Date: ")
# if expense_dt:
#     st.write(f"Fetching expenses for {expense_dt}")

#part 2
#Text elements
# st.header("Streamlit Core Features")
# st.subheader("Text Elements")
# st.text("This is a simple text element.")
#
# #Data display
# st.subheader("Data Display")
# st.write("Here is a simple table:")
#
# df = pd.DataFrame({
#     "Date":["2024-08-01","2024-08-02","2024-08-03"],
#     "Amount":[250,134,340]
# })
# st.table(df)
# st.table({"Column 1":[1,2,3], "Column 2":[4,5,6]})
#
# #Charts
# st.subheader("Charts")
# st.line_chart([1, 2, 3, 4])
#
# #User Input
# st.subheader("User Input")
# value = st.slider("Select a value",0,100)
# st.write(f"Selected value:{value}")

#part 3
# st.title("Interactive Widgets Example")
#
# #Checkbox
# if st.checkbox("Show/Hide"):
#      st.write("Checkbox is checked!")
#
# #Selectbox
# option = st.selectbox("Select a number",[1,2,3,4])
# st.write(f"You selected:{option}")
#
# option = st.selectbox("Category",["Rent","Food"])
# st.write(f"You selected:{option}")
#
# # option = st.selectbox("Category",["Rent","Food"],label_visibility ="collapsed")
# # st.write(f"You selected:{option}")
#
#
# #Multiselect
# options = st.multiselect("Select multiple number",[1,2,3,4])
# st.write(f"You selected:{options}")

