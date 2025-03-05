import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class CVRagPipeline:
    def __init__(self):
        self.docs = []
        self.db = None
        self.chain = None
        
    def load_documents(self, directory="cvs"):
        # Load all markdown files
        for filename in os.listdir(directory):
            if filename.endswith(".md"):
                file_path = os.path.join(directory, filename)
                loader = TextLoader(file_path, encoding='utf-8')
                self.docs.extend(loader.load())
                
        # Split documents
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200
        )
        return text_splitter.split_documents(self.docs)

    def initialize_rag(self):
        # Create vector store
        splits = self.load_documents()
        embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
        self.db = FAISS.from_documents(splits, embeddings)
        
        # Initialize LLM and memory
        llm = ChatOpenAI(
            model="gpt-4-turbo-preview",
            temperature=0.7
        )
        
        memory = ConversationBufferMemory(
            memory_key="chat_history",
            return_messages=True
        )
        
        # Create conversation chain
        self.chain = ConversationalRetrievalChain.from_llm(
            llm=llm,
            retriever=self.db.as_retriever(search_kwargs={"k": 3}),
            memory=memory,
            verbose=True
        )
        
    def query(self, question: str) -> str:
        if not self.chain:
            raise Exception("Pipeline not initialized. Call initialize_rag() first.")
        return self.chain.run(question)

def main():
    st.title("Chat with Claudia's CV")
    
    # Initialize RAG pipeline
    if "rag_pipeline" not in st.session_state:
        rag_pipeline = CVRagPipeline()
        rag_pipeline.initialize_rag()
        st.session_state.rag_pipeline = rag_pipeline
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Chat input
    if prompt := st.chat_input("Ask me anything about Claudia"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.chat_message("assistant"):
            response = st.session_state.rag_pipeline.query(prompt)
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
