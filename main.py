import os
import warnings
from typing import Dict
from llama_cpp import Llama


from openfabric_pysdk.utility import SchemaUtil

from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText

from openfabric_pysdk.context import Ray, State
from openfabric_pysdk.loader import ConfigClass

llm = Llama(
    model_path="llama-2-7b-chat.Q3_K_S.gguf",
    n_gpu_layers=1, # Uncomment to use GPU acceleration
    seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)

############################################################
# Callback function called on update config
############################################################
def config(configuration: Dict[str, ConfigClass], state: State):
    # TODO Add code here
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: Ray, state: State) -> SimpleText:

    output = []

    for text in request.text:

        llm_output = llm(
        f"You are scientific chatbot. ## USER: {text} A: ",
        max_tokens=32,
        stop=["Q:", "\n",],
        echo=False
    )
        output.append(llm_output["choices"][0]["text"])


    return SchemaUtil.create(SimpleText(), dict(text=output))
