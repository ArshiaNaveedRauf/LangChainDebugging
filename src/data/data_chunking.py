from langchain_text_splitters import RecursiveCharacterTextSplitter

class Chunking:
    def __init__(self,chunk_size,chunk_overlap):
        self.splitter= RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=['\n\n','\n','.',' ','']
        )

    def documents_chunker(self,documents):
        split_docs= self.splitter.split_documents(documents)
        return split_docs
    


