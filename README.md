
LangGraph Project


📌 Overview

This project demonstrates the implementation of LangGraph using both closed-source APIs and open APIs (Hugging Face API). It provides a full-featured environment 
for experimenting with LLMs, workflows, chatbots, and RAG (Retrieval-Augmented Generation) while supporting persistence, streaming, and UI integration.

This repository is designed for both learning purposes and practical LLM-based applications.

🎯 Key Implementations:


| Feature                     | Description                                                |
| --------------------------- | ---------------------------------------------------------- |
| **LLM Example**             | Demonstrates the use of large language models in LangGraph |
| **LLM Workflow**            | Structured pipelines for LLM calls                         |
| **Prompt Chaining**         | Chaining prompts for improved responses                    |
| **Conditional Workflow**    | Executes workflow based on dynamic conditions              |
| **Parallel Workflow**       | Run multiple LLM tasks concurrently                        |
| **Chatbot Example**         | Interactive chatbot implementation                         |
| **In-memory Chat Storage**  | Stores conversations temporarily in RAM                    |
| **Persistent Chat Storage** | Saves conversations to a database                          |
| **Chatbot Resume**          | Resume previous conversations                              |
| **Streaming Responses**     | Real-time streaming from LLMs                              |
| **RAG Implementation**      | Retrieval-Augmented Generation queries                     |
| **Tool Integration**        | Incorporates external tools with LangGraph workflows       |
| **UI Integration**          | Interactive interface using Streamlit                      |


🗂 Project Structure:
Here’s the recommended structure for your LangGraph project:
LangGraph_Project/
│
├── README.md                  # Project documentation
├── .gitignore                 # Git ignore file
├── requirements.txt           # Python dependencies
├── env/                       # Virtual environment (ignored in git)
├── .env                       # API keys and secrets (ignored in git)
│
├── data/                      # Optional datasets
│   └── chat_history.db        # Persistent chat storage
│
├── langgraph_examples/        # LLM examples
│   ├── llm_example.py
│   ├── workflow_example.py
│   ├── prompt_chaining.py
│   ├── conditional_workflow.py
│   └── parallel_workflow.py
│
├── chatbot/                   # Chatbot implementations
│   ├── chatbot_main.py
│   ├── streaming_chat.py
│   ├── resume_chat.py
│   └── db_utils.py
│
├── rag/                       # Retrieval-Augmented Generation
│   └── rag_query.py
│
├── tools/                     # External tools integration
│   └── tool_examples.py
│
└── ui/                        # Streamlit UI integration
    ├── app.py
    └── streamlit_components/


🔗 Workflow Diagram

+--------------------+       +------------------+       +------------------+
| LLM Examples       | --->  | LLM Workflows    | --->  | Prompt Chaining  |
+--------------------+       +------------------+       +------------------+
                                   |
                                   v
                          +------------------+
                          | Conditional Flow |
                          +------------------+
                                   |
                                   v
                          +------------------+
                          | Parallel Flow    |
                          +------------------+
                                   |
                                   v
                          +------------------+
                          | Chatbot Example  |
                          +------------------+
                                   |
                +------------------+------------------+
                |                                     |
        +------------------+                   +------------------+
        | In-memory RAM    |                   | Persistent DB    |
        | Chat Storage     |                   | Storage          |
        +------------------+                   +------------------+
                |
                v
        +------------------+
        | Chatbot Resume   |
        +------------------+
                |
                v
        +------------------+
        | Streaming Output |
        +------------------+
                |
                v
        +------------------+
        | RAG Queries      |
        +------------------+
                |
                v
        +------------------+
        | Tool Integration |
        +------------------+
                |
                v
        +------------------+
        | Streamlit UI     |
        +------------------+

        

⚡ Setup Instructions

1). Clone the repo:

    git clone https://github.com/username/LangGraph_Project.git
    cd LangGraph_Project

2). Create and activate the virtual environment 

python -m venv env
# Activate env:
# Windows
env\Scripts\activate
# macOS/Linux
source env/bin/activate

3). Install dependencies
  pip install -r requirements.txt

4). Add your API keys
   # Create a .env file (ignored in git) and add:

  HUGGINGFACE_API_KEY=<your_key_here>

5). Run Streamlit UI
 streamlit run ui/app.py

🔧 Usage
Explore LLM examples in langgraph_examples/
Test chatbot functionality in chatbot/
Experiment with RAG in rag/
Integrate tools in tools/
Run the interactive UI with Streamlit

💡 Notes
.env and virtual environment folder (env/) are ignored via .gitignore.
Use requirements.txt to install all dependencies.
Keep sensitive keys secret; never upload .env to GitHub.
Database files for persistent chat storage are in data/.


# Brief Details about the key concepts that used for the LangGraph Projects:

| #  | Feature                          | Description                                                                                                  |
| -- | -------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| 1  | **LLM Example**                  | Demonstrates how to initialize and interact with large language models, providing simple input-output tests. |
| 2  | **LLM Workflow**                 | Structured pipelines for multiple LLM calls, automating sequential tasks efficiently.                        |
| 3  | **Prompt Chaining**              | Connects outputs of one LLM call to the next, enabling complex multi-step prompt sequences.                  |
| 4  | **Conditional Workflow**         | Executes workflow branches based on dynamic conditions for flexible decision-making.                         |
| 5  | **Parallel Workflow**            | Runs multiple LLM tasks concurrently to save time and process multiple inputs simultaneously.                |
| 6  | **Chatbot Example**              | Interactive chatbot implementation showcasing real-time conversation handling with LangGraph.                |
| 7  | **In-memory Chat Storage**       | Temporarily stores conversations in RAM for immediate access during interactions.                            |
| 8  | **Persistent Chat Storage**      | Saves chat history to a database for long-term storage and retrieval.                                        |
| 9  | **Chatbot Resume Functionality** | Resumes previous conversations from persistent storage for seamless user experience.                         |
| 10 | **Streaming in LangGraph**       | Supports real-time streaming of LLM responses so users see outputs as they are generated.                    |
| 11 | **RAG Implementation**           | Retrieval-Augmented Generation combining LLMs with external knowledge sources for accurate queries.          |
| 12 | **Tool Integration**             | Incorporates external tools or APIs into workflows to extend LLM capabilities.                               |
| 13 | **UI Integration**               | Uses Streamlit to provide an interactive interface for testing LLMs, workflows, and chatbots.                |
