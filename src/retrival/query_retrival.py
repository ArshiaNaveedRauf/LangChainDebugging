from src.data.data_embedder import Embedder
class QueryRetrival:

    def __init__(self):
        self.embedder= Embedder()

    def query_embedder(self,query):
        embedded_query= self.embedder.embedding_generator([query])
        return embedded_query[0]

    def search_vector_db(self,db,query,top_k):
        embedded_query = self.query_embedder(query)
        retrived_docs= db.query(
            query_embeddings=[embedded_query.tolist()],
            n_results=top_k
        )
        return retrived_docs

    
    
    


        
