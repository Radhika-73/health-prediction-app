import streamlit as st
import sqlite3
import pandas as pd

from database import create_table
from predictor import predict_health

create_table()

conn = sqlite3.connect("health.db", check_same_thread=False)
cursor = conn.cursor()

st.title("Health Prediction Application")

menu = [
    "Add Patient",
    "View Patients",
    "Update Patient",
    "Delete Patient"
]

choice = st.sidebar.selectbox("Menu", menu)

# Adding Patient Details

if choice == "Add Patient":

    st.subheader("Add Patient")

    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    email = st.text_input("Email")

    glucose = st.number_input("Glucose", min_value=0.0)
    haemoglobin = st.number_input("Haemoglobin", min_value=0.0)
    cholesterol = st.number_input("Cholesterol", min_value=0.0)

    if st.button("Save"):

        remarks = predict_health(
            glucose,
            haemoglobin,
            cholesterol
        )

        cursor.execute("""
        INSERT INTO patients
        (name,dob,email,glucose,haemoglobin,cholesterol,remarks)
        VALUES (?,?,?,?,?,?,?)
        """,
        (
            name,
            str(dob),
            email,
            glucose,
            haemoglobin,
            cholesterol,
            remarks
        ))

        conn.commit()

        st.success("Patient Added Successfully")
        st.write("Prediction:", remarks)

# View details

elif choice == "View Patients":

    st.subheader("All Patients")

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    st.dataframe(df)

# Update Details

elif choice == "Update Patient":

    st.subheader("Update Patient")

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    st.dataframe(df)

    patient_id = st.number_input(
        "Enter Patient ID",
        min_value=1,
        step=1
    )

    if st.button("Load Patient"):

        cursor.execute(
            "SELECT * FROM patients WHERE id=?",
            (patient_id,)
        )

        patient = cursor.fetchone()

        if patient:

            st.session_state.patient = patient

        else:
            st.error("Patient Not Found")

    if "patient" in st.session_state:

        patient = st.session_state.patient

        new_name = st.text_input(
            "Name",
            patient[1]
        )

        new_email = st.text_input(
            "Email",
            patient[3]
        )

        new_glucose = st.number_input(
            "Glucose",
            value=float(patient[4])
        )

        new_haemoglobin = st.number_input(
            "Haemoglobin",
            value=float(patient[5])
        )

        new_cholesterol = st.number_input(
            "Cholesterol",
            value=float(patient[6])
        )

        if st.button("Update Record"):

            remarks = predict_health(
                new_glucose,
                new_haemoglobin,
                new_cholesterol
            )

            cursor.execute("""
            UPDATE patients
            SET name=?,
                email=?,
                glucose=?,
                haemoglobin=?,
                cholesterol=?,
                remarks=?
            WHERE id=?
            """,
            (
                new_name,
                new_email,
                new_glucose,
                new_haemoglobin,
                new_cholesterol,
                remarks,
                patient[0]
            ))

            conn.commit()

            st.success("Patient Updated Successfully")

# Delete Details

elif choice == "Delete Patient":

    st.subheader("Delete Patient")

    df = pd.read_sql_query(
        "SELECT * FROM patients",
        conn
    )

    st.dataframe(df)

    patient_id = st.number_input(
        "Enter Patient ID to Delete",
        min_value=1,
        step=1
    )

    if st.button("Delete"):

        cursor.execute(
            "DELETE FROM patients WHERE id=?",
            (patient_id,)
        )

        conn.commit()

        st.success("Patient Deleted Successfully")