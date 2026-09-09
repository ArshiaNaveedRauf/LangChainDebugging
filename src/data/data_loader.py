from langchain_community.document_loaders import (
    PyPDFLoader,
    Docx2txtLoader,
    UnstructuredPowerPointLoader,
    TextLoader
)
import os

class DataLoader:
    loader_map={
                ".pdf":PyPDFLoader,
                ".docx":Docx2txtLoader,
                ".pptx":UnstructuredPowerPointLoader,
                ".txt":TextLoader
                }
    def __init__(self,data_path):
        self.data_path= data_path
        

    def load_data(self):
        docs=[]
        for path in self.data_path:
            ext= os.path.splitext(path)[1].lower()
            loader_class= self.loader_map.get(ext)

            loader= loader_class(path)
            doc= loader.load()
            docs.extend(doc)
        return docs
    
    def print_data(self):
        documents=self.load_data()
        for doc in documents:
                print(doc.page_content)
                print(doc.metadata)






      

        



   

    


    