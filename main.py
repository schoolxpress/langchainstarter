import os
import langchain
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), override=True)

def main(country):
    prompt_template = PromptTemplate.from_template("Tell me a joke about {country}")
    formatted_prompt = prompt_template.format(country=country)

    #define your LLM
    llm = ChatOpenAI(openai_api_key=os.environ['OPENAI_API_KEY'], temperature=1)

    #run my chain prediction
    result = llm.predict(text=formatted_prompt)
    print(result)

def main2(question, language):
    #IN THIS EXAMPLE WE SHALL CREATE A PROMPT TEMPLATE AND PASS IN MULITPLE VARIABLES
    prompt_template_2 = PromptTemplate(input_variables=["question", "language"], template="""
         You are a vehicle mechanic, give responses to the following/ 
        question: {question}. Do not use technical words, give easy/
        to understand responses. Your response should be in {language}
    """)
    formatted_prompt_2 = prompt_template_2.format(question=question, language=language)
    llm = ChatOpenAI(temperature=1)

    output = llm.predict(text=formatted_prompt_2)
    print(output)




if __name__ == "__main__":
    #main(country="USA")
    main2(question="How do i replace my flat tire?", language="English")
