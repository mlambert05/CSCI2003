import streamlit as st
import mysql.connector

# Function to get a connection from Streamlit's secrets
@st.cache_resource
def get_connection():
    return mysql.connector.connect(st.secrets["mysql"])

cnx = get_connection()
import streamlit as st

def create_record():
    st.subheader("Add a New Record")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0, max_value=150)
    position = st.text_input("Position")
    if st.button("Add Record"):
        if name and position:
            query = "INSERT INTO employees (name, age, position) VALUES (%s, %s, %s)"
            values = (name, age, position)
            cursor = cnx.cursor()
            try:
                cursor.execute(query, values)
                cnx.commit()
                st.success("Record added successfully")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
            finally:
                cursor.close()
        else:
            st.warning("Please fill out all fields")

def read_records_pandas():
    st.subheader("View Records (Using Pandas)")
    query = "SELECT * FROM employees"
    try:
        data = pd.read_sql(query, cnx)
        st.dataframe(data)
    except mysql.connector.Error as err:
        st.error(f"Error: {err}")

def update_record():
    st.subheader("Update a Record")
    # Fetch existing records for selection
    cursor = cnx.cursor()
    cursor.execute("SELECT id, name FROM employees")
    records = cursor.fetchall()
    cursor.close()
    record_dict = {f"{id} - {name}": id for id, name in records}
    selected_record = st.selectbox("Select a record to update", list(record_dict.keys()))
    if selected_record:
        record_id = record_dict[selected_record]
        # Fetch current details
        cursor = cnx.cursor()
        cursor.execute("SELECT name, age, position FROM employees WHERE id = %s", (record_id,))
        result = cursor.fetchone()
        cursor.close()
        name, age, position = result
        # Input fields with current values
        new_name = st.text_input("Name", value=name)
        new_age = st.number_input("Age", min_value=0, max_value=150, value=age)
        new_position = st.text_input("Position", value=position)
        if st.button("Update Record"):
            query = "UPDATE employees SET name = %s, age = %s, position = %s WHERE id = %s"
            values = (new_name, new_age, new_position, record_id)
            cursor = cnx.cursor()
            try:
                cursor.execute(query, values)
                cnx.commit()
                st.success("Record updated successfully")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
            finally:
                cursor.close()

def delete_record():
    st.subheader("Delete a Record")
    # Fetch existing records for selection
    cursor = cnx.cursor()
    cursor.execute("SELECT id, name FROM employees")
    records = cursor.fetchall()
    cursor.close()
    record_dict = {f"{id} - {name}": id for id, name in records}
    selected_record = st.selectbox("Select a record to delete", list(record_dict.keys()))
    if selected_record:
        record_id = record_dict[selected_record]
        if st.button("Delete Record"):
            query = "DELETE FROM employees WHERE id = %s"
            cursor = cnx.cursor()
            try:
                cursor.execute(query, (record_id,))
                cnx.commit()
                st.warning("Record deleted")
            except mysql.connector.Error as err:
                st.error(f"Error: {err}")
            finally:
                cursor.close()
def main():
    st.title("CRUD Operations with Streamlit and MySQL")

    menu = ["Create", "Read (Pandas)", "Read (No Pandas)", "Update", "Delete"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Create":
        create_record()
    elif choice == "Read (Pandas)":
        read_records_pandas()
    elif choice == "Read (No Pandas)":
        read_records_no_pandas()
    elif choice == "Update":
        update_record()
    elif choice == "Delete":
        delete_record()
    else:
        st.subheader("Welcome to the CRUD app")

if __name__ == '__main__':
    main()

cnx.close()