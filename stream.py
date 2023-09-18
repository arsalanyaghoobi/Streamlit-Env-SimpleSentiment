import asyncio
import streamlit as st
import pandas as pd
import sqlite3
from Sentiment import sentiment


def create_table():
    conn = sqlite3.connect('record.db')
    cursor = conn.cursor()
    create_table_query = '''
    CREATE TABLE IF NOT EXISTS table_name (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        emotion TEXT,
        sentence TEXT
    );
    '''
    cursor.execute(create_table_query)
    conn.commit()
    cursor.close()
    conn.close()

def insert_data(result, inputData):
    conn = sqlite3.connect('record.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO table_name (emotion, sentence) VALUES (?, ?)", (result, inputData))
    conn.commit()
    cursor.close()
    conn.close()

def get_data():
    conn = sqlite3.connect('record.db')
    cursor = conn.cursor()
    cursor.execute("SELECT emotion, sentence FROM table_name")
    rows = cursor.fetchall()
    df = pd.DataFrame(rows, columns=['Emotion', 'Sentence'])
    cursor.close()
    conn.close()
    return df

async def body_config():
    st.set_page_config(page_title="Reilans Corporation", page_icon=":guardsman:", layout="centered")
    st.header("Reilans Corporation")
    st.subheader("We are the number one AI company in the world")
    st.title("Sentiment Analysis")
    inputData = st.text_input(label="Enter text:")
    if len(inputData) > 0:
        result = sentiment(inputData)
        create_table()
        insert_data(result, inputData)

    st.title("Sentiment Analysis Results")
    df = get_data()
    st.table(df)

    if st.button("Delete the data base"):
        emptyDatabaseCache2()


    link = 'https://www.linkedin.com/in/arsalan-yaghoubi-766911119/'
    text = 'FOR OTHER SERVICES CLICK HERE '
    st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none; color:Red; font-size:15px;">{text}</a>', unsafe_allow_html=True)

    bottom_container_style = """
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: gray;
        text-align: center;
        padding: 20px;
    """
    bottom_container = st.container()
    bottom_container.markdown("<div style='" + bottom_container_style + "'>Call Reilans Corporation at +1-781-520-3534</div>", unsafe_allow_html=True)


def emptyDatabaseCache2():
    conn = sqlite3.connect('record.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM table_name;")
    conn.commit()
    conn.close()


if __name__ == '__main__':
    asyncio.run(body_config())

