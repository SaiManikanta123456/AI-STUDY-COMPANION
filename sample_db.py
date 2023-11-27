import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/BookStore")  # Replace with your MongoDB connection URI
# mongodb://localhost:27017
# Access the database and collection
db = client.BookStore  # Replace 'db_name' with your database name
collection = db.Books  # Replace 'collection_name' with your collection name

# Streamlit App
st.title("MongoDB & Streamlit Example")

# Fetch data from MongoDB and display in Streamlit
data_from_mongo = collection.find({"Author":"Sri Sri"})  # Replace this with your query
for data in data_from_mongo:
    st.write(data)  # Display fetched data in Streamlit
