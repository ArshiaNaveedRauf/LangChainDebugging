from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os
class Rag:
    load_dotenv()
    def __init__(self):
        self.api_key= os.getenv("GroqAPIKey")
        self.llm= ChatGroq(groq_api_key=self.api_key,model_name= "openai/gpt-oss-120b",temperature=0.1,max_tokens=2000)

    def context(self,retrived_docs):
        context= "\n\n".join(retrived_docs["documents"][0] ) if retrived_docs else ""
        if not context:
            print("no relevent information to answer your question was found")

        return context

    def prompt_engineering(self,retrived_docs,query):
        context=self.context(retrived_docs)
        prompt=f""" use the following context to answer the question concisely
        Rules:
        1. do not use your own knowledge unless its to fill very small gaps.
        2. Do not make up information.
        3. If the answer cannot be found in the context, respond exactly:
        "I don't know based on the provided documents."
        4. you can reply to greetings with your own knowleage
        Context : {context}
        Question : {query}
        Answer : """

        response= self.llm.invoke([prompt])
        return response.content


        
