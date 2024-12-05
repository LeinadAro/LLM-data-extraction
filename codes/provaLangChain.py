import sys
import os
import json
from typing import Optional, Any, List
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from pydantic import BaseModel, Field, ConfigDict
from langchain_ollama.llms import OllamaLLM
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import JsonOutputParser, PydanticOutputParser
#from langchain_experimental.llms.ollama_functions import OllamaFunctions


class Immobile(BaseModel):
    model_config = ConfigDict(strict=True)

    Comune: Any = Field(
        description="Il comune in cui si trova l'immobile", deafualt=None
    )
    Indirizzo: Any = Field(
        description="via, piazza o altro in cui si trova l'immobile", deafualt=None
    )
    Vani: Any = Field(
         description="nuemro di vani che compongono l'immobile", deafualt=None
    )
    Locali: Any = Field(
        description="numero di locali abitali dell'immobile, come camere da letto, soggiorni,sale", deafualt=None
    )
    Mq: Any = Field(
        description="superficie in metri quadrati dell'immobile", deafualt=None
    )
    Bagni: Any = Field(
        description="numero di bagni dell'immobile", deafualt=None
    )
    Piano: Any = Field(
        description="a che piano si trova l'immobile", deafualt=None
    )
    PostiAuto: Any = Field(
        description="numero di posti auto o garage", deafualt=None
    )
    NumProcedura: Any = Field(
         description="Numero di proceura dell'avviso giudiziario", deafualt=None
    )
    Lotto: Any = Field(
         description="Numero di lotto dell'immobile", deafualt=None
    )

class ImmobileList(BaseModel):
    title: str = Field(description="ImmobileList")
    description: str = Field(description="lista di immobili")
    immobili: List[Immobile]

immobile_schema = json.dumps(ImmobileList.model_json_schema())
#parser = PydanticOutputParser(pydantic_object = Immobile)
parser = JsonOutputParser(schema = ImmobileList.model_json_schema())
system = open(sys.argv[1], 'r').read()
prompt = PromptTemplate(
    template="{system}\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions(), "system": system},
)
model = ChatOllama(model="qwen2.5:7b-instruct-q8_0", context_length=50000, temperature=0)
#model = model.with_structured_output(schema = immobile_schema)
chain = prompt | model | parser
#text = "Procedura 21/2024. Lotto 1. Appartamento monolocale sito a Mazzano via Giuseppe Mazzini 21 al secondo piano. 50 mq  Un bagno, un posto auto."
#prompt = prompt_template.invoke({"text": text})
text = open(sys.argv[2], 'r').read()
print(chain.invoke({"query": text}))
