from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_core.tools import tool
from langgraph.graph import StateGraph, START
from typing import Annotated, TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, BaseMessage
from langgraph.prebuilt import ToolNode, tools_condition

# from langchain_community.embeddings import HuggingFaceEmbeddings
#from langchain_huggingface import HuggingFaceEmbeddings
#from langchain_huggingface import HuggingFaceEndpoint
import os


load_dotenv()

# model
llm = ChatOpenAI()
#llm = HuggingFaceEndpoint(
 #   repo_id="mistralai/Mistral-7B-Instruct-v0.2",
  #  huggingfacehub_api_token=os.environ.get("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"),
   # temperature=0
#)



# load the document
loader = PyPDFLoader("Hands_On_ML.pdf")
docs = loader.load()

# print(len(docs))      # 126

# to break the doc in chunk
splitter = RecursiveCharacterTextSplitter(chunk_size= 300, chunk_overlap = 60)
chunks = splitter.split_documents(docs)

# print(len(chunks))    # 585

# Embedding Models
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')
#embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = FAISS.from_documents(chunks, embeddings)
# print(vector_store)

# from verctor db returns the top 4 most similar chunks('k': 4)
retriever = vector_store.as_retriever(search_type= 'similarity', search_kwargs= {'k':2})

# add the tool from the query

@tool
def rag_tool(query):

    """
    Retrieve relevant information from the pdf document.
    Use this tool when the user asks factual / conceptual questions
    that might be answered from the stored documents.
    """
    result = retriever.invoke(query)

    context = [doc.page_content for doc in result]
    metadata = [doc.metadata for doc in result]

    return {
        'query': query,
        'context': context,
        'metadata': metadata
    }

# tool binding
tools = [rag_tool]
llm_tool = llm.bind_tools(tools)


# for langraph message
class ChatState(TypedDict):
    messages : Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages = state['messages']
    response = llm_tool.invoke(messages)

    return {'message': [response]}

# ToolNode is a prebuilt LangGraph node that detect tool calling from LLM
tool_node = ToolNode(tools)

# prepare the graph
graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)
graph.add_node('tools', tool_node)

graph.add_edge(START, 'chat_node')
graph.add_conditional_edges('chat_node', tools_condition)
graph.add_edge('tools', 'chat_node')

chat = graph.compile()

response = chat.invoke({"messages": [HumanMessage(
                content=("Using the pdf notes, explain about the Gini in Decision Tree"))]}
                     )

print(response['messages'][-1].content)