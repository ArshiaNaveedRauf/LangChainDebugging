from src.data.data_loader import DataLoader
from src.data.data_chunking import Chunking
from config import data_path
from config import chunk_size
from config import chunk_overlap



class DataIngestionPipeline:
    def __init__(self):
        self.data_loader= DataLoader(data_path)
        self.data_chunker= Chunking(chunk_size,chunk_overlap)


    def run_ingestion_pipeline(self):
        documents = self.data_loader.load_data()
        chunks= self.data_chunker.documents_chunker(documents)
        print(f"content {chunks[20].page_content[:300]} \n metadata: {chunks[20].metadata}")

        




    
        