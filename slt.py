import streamlit as st
from app import generate_restaurant_name_and_items


st.title("Restaurant Name Generator")
cuisine=st.sidebar.selectbox("Pick a cuisine",("Indian","Italian","Mexican","Arabic","American"))



if cuisine:
    rest,names_list1 = generate_restaurant_name_and_items(cuisine)
    st.header(rest)
    menu_item=names_list1
    st.write("**Menu Items**")
    for item in menu_item:
        st.write("-",item)