from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI

load_dotenv()

llm = OpenAI()
chat_model = ChatOpenAI()

llm.predict('hi!')

chat_model.predict("hi!")