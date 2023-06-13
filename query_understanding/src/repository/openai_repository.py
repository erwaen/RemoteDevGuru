"""Repository for a openai conexion"""

import pathlib

from src.api.dependencies.indice_mock import IndiceMock
from src.config.manager import settings

from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate, SystemMessagePromptTemplate, AIMessagePromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
# openai.api_key = settings.OPENAI_KEY
ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.resolve()
MODEL = "gpt-3.5-turbo"
class BaseLlmRepository():
    doc_dir = f"{ROOT_DIR}/documentos/"
    
    def get_direct(self, message: str, result_number: int = 5) -> list[str]:
        """Obtenemos todas las respuestas desde un servicio externo"""
        pass
    def get_chat_response(self, message: str, result_number: int = 5) -> list[str]:
        """Logica para la respuesta al chatbot """
        pass
    def get_back_indice(self, message: str):
        """Solicitamos al back indice los resultados"""
        pass
    def sugerence_questions(self, question: str) -> bool:
        pass


class OpenAiRepository(BaseLlmRepository):
    """Repositorio para la conexion con openAI"""

    def get_back_indice(self, message: str) -> list[str]:
        """Solicitamos datos del back indice"""
        
        return IndiceMock().result(mes=message)['response']
    
    def get_direct(self, message: str, result_number: int = 5) -> list[str]:
        # messages = [ {'role': 'system', 'content': message}]
        llm_openai = OpenAI(openai_api_key=settings.OPENAI_KEY)
        
        return [llm_openai(message)]

    def get_chat_response(self, message: str, result_number: int = 5) -> list[str]:
        # resp: list = self.get_coincidence_embedding(message=message, result_number=1).values.tolist()
        # is_remote_question = self.verify_remote_question(question=message)
        # is_remote_question = True
        resp = []
        
        data = self.chat_template_re(message=message)
        return data
    
    def chat_template_re(self, message):
        """
        ChatPromptTemplates
        AL igual que tenemos templates para modelos abiertos, LangChain tambien nos brinda templates para modelos de chat. Estos templates nos ayudan a darle la informacion a los modelos de chat en la manera en la que lo necesitan.

        Los elementos de estos templates son:

        Human: El texto que escribimos nosotros
        AI: El texto que responde el modelo
        System: El texto que se le envía al modelo para darle contexto de su funcionamiento
        """
        chatgpt = ChatOpenAI(openai_api_key=settings.OPENAI_KEY)
        
        prompt_temp_sistema = PromptTemplate(
            template="""
            Eres un asistente virtual que responde preguntas de manera muy breve y en español sobre trabajo remoto.
            contexto -> {data}
            """,
            input_variables=['data'],
        )

        template_sistema = SystemMessagePromptTemplate(prompt=prompt_temp_sistema)

        #Ahora para el humano
        prompt_temp_humano = PromptTemplate(template="{texto}", input_variables=["texto"])

        template_humano = HumanMessagePromptTemplate(prompt=prompt_temp_humano)
        
        chat_prompt = ChatPromptTemplate.from_messages([template_sistema, template_humano])

        # Este es el formato del prompt que acabamos de armar
        data_indice = str(self.get_back_indice(message=message))
        chat_promt_value = chat_prompt.format_prompt(data=data_indice,texto=message).to_messages()
        
        chat_resp = chatgpt(chat_promt_value)
        
        return [chat_resp.content]
   
    def sugerence_questions(self, question: str):
        from langchain.output_parsers import CommaSeparatedListOutputParser
        
        parser = CommaSeparatedListOutputParser()
        template = "Sugiereme 2 preguntas sobre trabajo remoto, teniendo en cuenta que la pregunta anterior fue-> {question}\n{parseo}"
        prompt_templ = PromptTemplate(input_variables=['question'],
                                        template= template,
                                        partial_variables={"parseo":parser.get_format_instructions()})


        prompt_value = prompt_templ.format(question=question)
        llm_openai = OpenAI(model_name = "text-davinci-003", openai_api_key=settings.OPENAI_KEY)
        respuesta = llm_openai(prompt_value)
        return parser.parse(respuesta)
   
    # def verify_remote_question(self, question:str) -> bool:
    #     from langchain.output_parsers.enum import EnumOutputParser
    #     from enum import Enum

    #     class Respuesta(Enum):
    #         SI = "si"
    #         NO = "no"
    #     parser = EnumOutputParser(enum=Respuesta)
    #     template = "Es sobre trabajo remoto esta pregunta -> {question}\m{parseo}"
    #     prompt_templ = PromptTemplate(input_variables=['question'],
    #                                   template= template,
    #                                   partial_variables={"parseo":parser.get_format_instructions()})


    #     prompt_value = prompt_templ.format(question=question)
    #     llm_openai = OpenAI(model_name = "text-davinci-003", openai_api_key=settings.OPENAI_KEY)
    #     respuesta = llm_openai(prompt_value)
    #     return parser.parse(respuesta).value
