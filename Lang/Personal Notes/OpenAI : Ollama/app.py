import os
from dotenv import load_dotenv

import streamlit as st
from pydantic import BaseModel, Field
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

# (Optional) LangSmith tracking — only set if present
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    if os.getenv("LANGCHAIN_PROJECT"):
        os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")


class AnswerSchema(BaseModel):
    answer: str = Field(description="Final answer to the user's question")
    context_used: str = Field(description="Short note on what context was used (1-2 lines)")
    confidence: float = Field(description="Confidence score between 0 and 1")


parser = PydanticOutputParser(pydantic_object=AnswerSchema)
format_instructions = parser.get_format_instructions()

prompt = ChatPromptTemplate.from_messages([
    ("system", 
     "You MUST output ONLY a JSON object that matches the schema. "
     "Do NOT output the schema. Do NOT add explanations. JSON only."),
    ("user",
     "Question: {question}\n\n"
     "{format_instructions}\n\n"
     "Return ONLY the JSON object with keys: answer, context_used, confidence.")
])

llm = Ollama(model="llama3")
chain = prompt | llm | parser


st.title("LangChain + Ollama + Pydantic Output")
question = st.text_input("Ask a question:")

if st.button("Run") and question:
    try:
        parsed = chain.invoke({
            "question": question,
            "format_instructions": format_instructions
        })

        st.subheader("Answer")
        st.write(parsed.answer)

        st.subheader("Context Used")
        st.write(parsed.context_used)

        st.subheader("Confidence")
        st.write(parsed.confidence)

    except Exception as e:
        st.error("Parser failed (model didn’t follow schema).")
        st.exception(e)
