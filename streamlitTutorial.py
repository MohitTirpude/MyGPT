#include packages
import streamlit as st # frontend userinterface design 
import numpy as np # it is used for scientific calculations 
import pandas as pd # it is used for data analytics

st.title("Hello , streamlit")
st.write(":streamlit: This is your first streamlit app")
st.text("Lets go started ")
st.write("My name is Mohit Tirpude")

# conditional logic
name = st.text_input("Enter yor Name :")
if st.button("Greet"):
    st.success(f"Salute {name}")

#Displaying data and charts 
df = pd.DataFrame(np.random.randn(10, 2), columns=["A","B"])
st.line_chart(df)
st.bar_chart(df)

#File uploading and caching 
upload_file = st.file_uploader("Upload File", type="csv")
if upload_file:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

# all the userinterface of streamlit
st.header("this is a header")
st.subheader("This is a subheader")  
st.markdown("**Bold**, *Italic*, [Link](https://www.datablist.com/)") 
st.text_area("Write your message")
st.number_input("pick a number", min_value=0, max_value=100)
st.slider("choose a range",0, 100)
st.selectbox("Select a fruit",["Apple","banana","Mango"])
st.multiselect("choose toppings",["cheese","capsicum","Olives"])
st.radio("Pick one", ["Option A", "Option B" ])
st.checkbox("I agree terms and conditions")

# form code 
with st.form("Login Form"):
    username = st.text_input("username")
    password = st.text_input("password", type="password")
    submitted = st.form_submit_button("Login")

    if submitted:
        st.success(f"Welcome, {username}")
#        
#Check radio button
option = st.radio("Choose View", ["Show chart", "Show Table"])
if option == "Show chart":
    st.write("Chart would be appear here")
else:
    st.write("Table would be appear here")

if st.checkbox("Show details"):
    st.info("Here are now details")

#Media layout and advance widget
st.sidebar.title("New chart")
st.image("http://www.adventurouskate.com/wp-content/uploads/2012/03/029.jpg")
st.video("https://youtu.be/BSJa1UytM8w?list=RDBSJa1UytM8w")