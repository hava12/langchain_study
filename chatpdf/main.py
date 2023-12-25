from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

loader = PyPDFLoader("chatpdf/unsu/unsu.pdf")
pages = loader.load_and_split()

text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 100,
    chunk_overlap = 20,
    length_function = len,
    is_separator_regex = False
)

texts = text_splitter.split_documents(pages)

print(pages[1])