import sys
import os
from typing import Optional
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from pydantic import BaseModel, Field
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser
#from langchain_experimental.llms.ollama_functions import OllamaFunctions


class Immobile(BaseModel):
    Comune: str = Field(
        default=None, description="Il comune in cui si trova l'immobile"
    )
    Indirizzo: str = Field(
        default=None, description="via, piazza o altro in cui si trova l'immobile"
    )
    Vani: float = Field(
        default=None, description="nuemro di vani che compongono l'immobile"
    )
    Locali: int = Field(
        default=None, description="numero di locali abitali dell'immobile, come camere da letto, soggiorni,sale"
    )
    Mq: float = Field(
        default=None, description="superficie in metri quadrati dell'immobile"
    )
    Bagni: int = Field(
        default=None, description="numero di bagni dell'immobile"
    )
    Piano: int = Field(
        default=None, description="a che piano si trova l'immobile"
    )
    PostiAuto: int = Field(
        default=None, description="numero di posti auto o garage"
    )
    NumProcedura: str = Field(
        default=None, description="Numero di proceura dell'avviso giudiziario"
    )
    Lotto: str= Field(
        default=None, description="Numero di lotto dell'immobile"
    )

parser = JsonOutputParser(schema=Immobile)
system = open(sys.argv[1], 'r').read()
prompt = PromptTemplate(
    template="Sei un estrattore di dati di immobili\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions(), "system": system},
)
model = ChatOllama(model="llama3.2:3b-instruct-q4_0", context_length=50000, temperature=0, format="json")
#structured_llm = model.with_structured_output(parser)
chain = prompt | model | parser
text = "Procedura 21/2024. Lotto 1. Appartamento monolocale sito a Mazzano via Giuseppe Mazzini 21 al secondo piano. 50 mq  Un bagno, un posto auto."
#prompt = prompt_template.invoke({"text": text})
#text = open(sys.argv[2], 'r').read()
print(chain.invoke({"query": text}))
