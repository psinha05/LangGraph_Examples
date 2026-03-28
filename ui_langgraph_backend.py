
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver


load_dotenv()


llm = ChatOpenAI(model='gpt-4o-mini')

class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]


def chat_node(state: ChatState):

    messages = state['messages']
    response = llm.invoke(messages)
    
    return {"messages": response}

# inMemory
checkpointer = InMemorySaver() 


# add the nodes and edges
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)
graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)
 

# compile the flow of the graph
chatbot = graph.compile(checkpointer=checkpointer)

# run the graph
# chatbot