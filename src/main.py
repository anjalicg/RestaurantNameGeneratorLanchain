import streamlit as st
from util import generate_restaurant_name_and_items
from dotenv import load_dotenv
st.title("Restaurant Name Generator")
cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Mexican", "Arabic", "French"))

load_dotenv()

if cuisine:
    response = generate_restaurant_name_and_items(cuisine)
    st.header(response["restaurant_name"].strip())
    menu_items = response["menu_items"].strip().split(",")
    print(f"menu_items = {menu_items}")
    print(f"menu_items = {type(menu_items)}")
    st.write("**Menu items**")
    for item in menu_items:
        print(f"DEBUG = {item}")
        if len(item.strip()) > 0:
            st.write(item.strip())



