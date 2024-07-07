from langchain_community.llms import ollama
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.prompts import ChatPromptTemplate
from langchain.prompts import FewShotChatMessagePromptTemplate
from langchain_community.document_loaders import WebBaseLoader

llm = ollama.Ollama(
    base_url='http://localhost:11434',
    model='openhermes',
    temperature=0.9,
    callback_manager=CallbackManager([StreamingStdOutCallbackHandler()])
)

from langchain.memory import ChatMessageHistory
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

chat_messages = ChatMessageHistory()
chat_messages.add_user_message('Can you translate I love programming in French')
chat_messages.add_ai_message("J'adore la programmation")
memory = ConversationBufferMemory(chat_memory=chat_messages)
conversation_chain = ConversationChain(llm=llm, memory=memory)


conversation_chain.predict(input="what was my previous question ?")
