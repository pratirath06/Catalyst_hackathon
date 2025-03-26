# models/conversation.py file
import os
from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain_groq import ChatGroq
from langchain.chains import LLMChain
import logging

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
    llm = ChatGroq(api_key="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", model_name="llama-3.3-70b-specdec")

    # Initialize memory
    memory = ConversationBufferMemory(
        return_messages=True,
        memory_key="chat_history"
    )

    # Create prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are EduMentor AI, an expert educational assistant. Assist with notes, quizzes, concept explanations, and more. The user is at Doctorate Educational level. Respond to queries accordingly."),
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