from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import os
from langserve import add_routes
from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
model=ChatGroq(model= "llama-3.1-8b-instant", api_key=os.environ.get("GROQ_API_KEY"))

# Prompt templates
from langchain_core.prompts import ChatPromptTemplate
generic_template = "Translate the following text into {language}."
prompt = ChatPromptTemplate.from_messages([
    ("system", generic_template),
    ("human", "{text}") # This is the variable for the French text
])  

parser = StrOutputParser()

# chain
chain = prompt | model | parser

## App definition

app= FastAPI(title = "Langchain server",
             version = "1.0",
             description = "A simple API server")



add_routes (
    app ,
    chain,
    path = '/chain'
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app,host="localhost", port = 8000)

