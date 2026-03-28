
from langgraph.graph import StateGraph, MessagesState, START, END
from langchain_openai import ChatOpenAI
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver
#from langgraph.checkpoint.sqlite import SqliteSaver
import sqlite3



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
# now checkpointer connects with Sqllitesaver
con = sqlite3.connect(database= 'chat.db', check_same_thread= False)

#checkpointer = SqliteSaver(conn=con)

# add the nodes and edges
graph = StateGraph(ChatState)
graph.add_node("chat_node", chat_node)

graph.add_edge(START, "chat_node")
graph.add_edge("chat_node", END)
 

# compile the flow of the graph
chatbot = graph.compile(checkpointer=checkpointer)




# function for retrieve all the unique threads using the chats, checkpointer has all the checkpts within an threads

#def retrieve_unique_threads():
 #   all_unique_threads = set()
  #  for chkpt in checkpointer.list(None):
   #     all_unique_threads.add(chkpt.config['configurable']['thread_id'])

    #return list(all_unique_threads)


# config for thread
#CONFIG = {'configurable': {'thread_id':'thread-1'}}

# run the graph
#chatbot

# test locally the sqlite db
#response = chatbot.invoke({'messages': [HumanMessage(content='what is capital of Bihar')]},
 #              config= CONFIG).

#print(response.content)

