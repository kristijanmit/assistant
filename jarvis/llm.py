from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatMessagePromptTemplate
from jarvis.config import template

model = OllamaLLM(model="dolphin-llama3")
prompt = ChatMessagePromptTemplate.from_template(template, role="user")

def get_llm_response(context, user_input):
    formatted_prompt = prompt.format(context=context, question=user_input)
    prompt_text = str(formatted_prompt)

    result = model.invoke(prompt_text)
    return result
