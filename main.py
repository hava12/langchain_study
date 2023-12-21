from dotenv import load_dotenv

load_dotenv()

from langchain.llms import OpenAI
llm = OpenAI()
result = llm.predict('hi!')
print(result)

# from langchain.chat_models import ChatOpenAI
# chat_model = ChatOpenAI()
# chat_model.predict("hi!")