from langchain.chains import LLMChain
import re 
import random
from langchain_huggingface import HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    max_length=128,
    temperature=0.7,
    huggingfacehub_api_token='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',
)
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
def generate_restaurant_name_and_items(cuisine):
    # chain 1: Restaurant Name
    prompt_template_name=PromptTemplate(
        input_variable=["cuisine"],
         template="I want to open a restaurant for {cuisine} food. Give me comma seperated list of restaurant names.")
    name_chain=LLMChain(llm=llm,prompt=prompt_template_name, output_key="Restaurant_name")
    
    #Chain 2: Menu Item
    prompt_template_item=PromptTemplate(
        input_variable=["Restaurant_name"],
        template="Suggest some meanu items for {Restaurant_name} food.")
    fooditem_chain=LLMChain(llm=llm,prompt=prompt_template_item,output_key="Menu_Item")
    from langchain.chains import SequentialChain
    chain=SequentialChain(
        chains=[name_chain,fooditem_chain],
        input_variables=["cuisine"],
        output_variables=["Restaurant_name","Menu_Item"])
    response= chain({'cuisine':cuisine})
    regex = re.compile(r'(?<=\d\.).*')
    names = response['Restaurant_name']
    names_list = regex.findall(names)
    rest=random.choice(names_list)
    
    names1 = response["Menu_Item"]
    names_list1 = regex.findall(names1)
    return rest,names_list1