from dotenv import load_dotenv

load_dotenv()

content = "고양이"

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict(content + "에 대한 시를 써줘")
# print(result)


from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
result = chat_model.predict(content + "에 대한 시를 써줘")
print(result)

import streamlit as st

st.title('인공지능 시인')