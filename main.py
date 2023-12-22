from dotenv import load_dotenv

load_dotenv()

content = "hi"

# from langchain.llms import OpenAI
# llm = OpenAI()
# result = llm.predict(content)
# print(result)


from langchain.chat_models import ChatOpenAI
chat_model = ChatOpenAI()
result = chat_model.predict(content)
print(result)