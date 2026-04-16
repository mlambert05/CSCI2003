import streamlit as st
import pandas as pd
import mysql.connector



st.title("Hello, Streamlit!")
st.write("this is my first streamlit app")

# Database connection configuration
db_config = {
    'user': 'Madelyn',
    'password': 'Nagito',
    'host': 'localhost',  # or '127.0.0.1'
    'database': 'my_streamlit_app',
}

# Create a connection to the database
#cnx = mysql.connector.connect(db_config)

def get_data():
    query = "SELECT * FROM your_table;"
    cursor = cnx.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    columns = cursor.column_names
    cursor.close()
    return pd.DataFrame(result, columns=columns)

    st.title("MySQL Data Viewer")

# Retrieve data from the database
data = get_data()

# Display data in a table
st.subheader("Data from MySQL Database")
st.dataframe(data)

cnx.close()

