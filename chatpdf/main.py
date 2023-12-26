from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores.chroma import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.retrievers.multi_query import MultiQueryRetriever
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

loader = PyPDFLoader("chatpdf/unsu/unsu.pdf")
pages = loader.load_and_split()
load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100, # 쪼개는 글자 단위
    chunk_overlap = 20, 
    length_function = len,
    is_separator_regex = False
)

texts = text_splitter.split_documents(pages)

#Embedding
embeddings_model = OpenAIEmbeddings()

# Chroma.from_documents 시 onnxruntime not found 에러 발생
# https://learn.microsoft.com/ko-kr/cpp/windows/latest-supported-vc-redist?view=msvc-170#visual-studio-2015-2017-2019-and-2022
# 위 링크에서 Visual C++ 설치하여 해결
# load it tnto Chroma
db = Chroma.from_documents(texts, embeddings_model)

# Question
question = "아내가 먹고 싶어하는 음식은 뭐야?"
llm = ChatOpenAI(temperature=0) # temperature가 0에 가까울수록 일관적인 답변을 1에 가까울수록 창의적인 답변을 한다.
# retriever_from_llm = MultiQueryRetriever.from_llm(
#     retriever=db.as_retriever(), llm=llm
# )

# docs = retriever_from_llm.get_relevant_documents(question) # 관련된 문서를 가져옴
# print(len(docs))
# print(docs)

qa_chain = RetrievalQA.from_chain_type(llm, retriever=db.as_retriever())
result = qa_chain({"query": question})
print(result)
# print(texts[1])