# models/conversation.py file
import os
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
#from langchain.chains import LLMChain
import logging
from langchain_ollama.llms import OllamaLLM

# Setup logging
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "application.log"),
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


def get_conversation_chain():
    # Initialize Groq LLM
    #llm = OllamaLLM(model="llama3.1:8b", api_key = "api_key")
    llm = ChatGroq(api_key= st.secrets["Groq_API"], model_name="llama-3.3-70b-specdec")

    # Initialize memory
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history"
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are EduMentor AI, an expert educational assistant designed to support learners in their studies. Your purpose is to assist with a variety of educational tasks, including generating concise study notes, creating short-answer quizzes, explaining concepts in a clear and structured manner, and offering interactive learning activities like educational games. Respond to user queries with accurate, well-organized, and easy-to-understand information tailored to the context of the request."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}")
    ])

    # Initialize conversation chain
    conversation = LLMChain(
        llm=llm,
        prompt=prompt,
        memory=memory,
        verbose=True
    )

    return conversation
