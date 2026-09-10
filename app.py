import streamlit as st
from pipeline import DataIngestionAndRetrivalPipeline
@st.cache_resource
def get_pipeline():
    data_pipeline=DataIngestionAndRetrivalPipeline()
    db= data_pipeline.run_ingestion_pipeline()
    return data_pipeline, db

class App:
  

    def run(self):
        data_pipeline,db= get_pipeline()

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for message in st.session_state.messages:
            with st.chat_message(message.get("role")):
                st.write(message.get("content"))

        query=st.chat_input("ask something:")
        if query:

            with st.chat_message("user"):
                st.write(query)
            st.session_state.messages.append({"role":"user", "content":query})

            answer= data_pipeline.run_retrival_pipeline(query,db)
    
            with st.chat_message("assistant"):
                st.write(answer)
            st.session_state.messages.append({"role":"assistant", "content":answer})




app= App()
app.run()