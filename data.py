import mysql.connector
import pandas as pd
import streamlit as st

def format_heure(dataframe):
    dataframe['heure'] = pd.to_timedelta(dataframe['heure']).apply(lambda x: f"{x.components.hours}:{x.components.minutes:02d}:{x.components.seconds:02d}")
    return dataframe

@st.cache_data
def get_data(query):
    # Connection à la BDD
    mydb = mysql.connector.connect(host="localhost", port="3307", user="client", password="example", database="breizhibus")
    # Le curseur permet d'intéragir avec la BDD
    db=mydb.cursor()

    db.execute(query)
    dataframe = pd.DataFrame(db.fetchall(), columns = [i[0] for i in db.description])

    db.close()
    mydb.close()

    return dataframe