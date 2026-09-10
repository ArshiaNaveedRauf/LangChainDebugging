from pipeline import DataIngestionAndRetrivalPipeline
from config import top_k

def test_retrieval():
    pipeline = DataIngestionAndRetrivalPipeline()

    db = pipeline.run_ingestion_pipeline()

    query = "What is LangChain?"

    retrived_docs = pipeline.retrival.search_vector_db(
        db,
        query,
        top_k
    )

    assert retrived_docs is not None
