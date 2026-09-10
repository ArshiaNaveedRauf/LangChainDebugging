from src.data.data_loader import DataLoader
from src.data.data_chunking import Chunking
from src.data.data_embedder import Embedder
from src.data.vector_data_db import VectorDatabase
from src.retrival.query_retrival import QueryRetrival
from src.retrival.rag import Rag
from config import data_path
from config import chunk_size
from config import chunk_overlap
from config import top_k



class DataIngestionAndRetrivalPipeline:
    def __init__(self):
        self.data_loader= DataLoader(data_path)
        self.data_chunker= Chunking(chunk_size,chunk_overlap)
        self.data_embedder= Embedder()
        self.database= VectorDatabase()
        self.retrival= QueryRetrival()
        self.augmentation= Rag()


    def run_ingestion_pipeline(self):
        collection = self.database.create_collection()
        if collection.count()>0:
            return collection
        documents = self.data_loader.load_data()
        chunks= self.data_chunker.documents_chunker(documents)
        embeddings= self.data_embedder.embedding_visualizer(chunks=[ chunk.page_content for chunk in chunks])
        db= self.database.collect_vectors(embeddings,chunks)
        return db

    def run_retrival_pipeline(self,query,db):
        retrived_docs=self.retrival.search_vector_db(db,query,top_k)
        print(retrived_docs["documents"][0])
        answer= self.augmentation.prompt_engineering(retrived_docs,query)
        return answer
        


    
        