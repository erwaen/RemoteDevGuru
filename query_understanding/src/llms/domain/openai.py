import pathlib
import openai
import pandas as pd
from src.config.manager import settings
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from openai.embeddings_utils import get_embedding, cosine_similarity

openai.api_key = settings.OPENAI_KEY
ROOT_DIR: pathlib.Path = pathlib.Path(__file__).parent.parent.parent.parent.resolve()
class BaseOpenAi():
    doc_dir = f"{ROOT_DIR}/documentos/"
    def getSimiliarText():
        pass
    def embedding():
        pass



class OpenAiDomain(BaseOpenAi):
    
    def __init__(self) -> None:
        pass

    def getSimiliarText(self, message: str, result_number = 2):
        # Utilizamos pickle para mantener toda la metadata del archivo
        # beneficia, porque mantiene el tipo de dato  de las columnas originales
        # El tipo de dato en numpy 
        datos: pd.DataFrame = pd.read_pickle(f'{self.doc_dir}emb.pk')
        
        busqueda_embed = get_embedding(message, engine="text-embedding-ada-002")
        datos["Similitud"] = datos['Embedding'].apply(lambda x: cosine_similarity(x, busqueda_embed))
        datos = datos.sort_values("Similitud", ascending=False)
        # return datos.iloc[:result_number][["texto", "Similitud", "Embedding"]]
        print(datos.iloc[:result_number]["texto"].values)
        
        return datos.iloc[:result_number]["texto"].values.tolist()
    
    # def embed_text(path="texto.csv"):
    #     conocimiento_df = pd.read_csv(path)
    #     conocimiento_df['Embedding'] = conocimiento_df['texto'].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002'))
    #     conocimiento_df.to_csv('embeddings.csv')
    #     return conocimiento_df

    def embedding(self) :
        loader = PyPDFLoader(f"{self.doc_dir}/remote-work-paraguay.pdf")
        # dividimos en paginas 
        pages = loader.load_and_split()

        # Un elemento por cada página
        # return pages[3].page_content
        
        # Divide las paginas en parrafos de {chunk_size} caracteres
        # en caso de que identifique el salto de linea junto con un punto final, tambien lo separa
        split = CharacterTextSplitter(chunk_size=300, separator = '.\n')
        
        # ejecuta la funcion que divide las paginas en parrafos
        textos = split.split_documents(pages) # Lista de textos
        # print(textos[4].page_content)
        # Extraemos la parte de page_content de cada texto y lo pasamos a un dataframe
        textos = [str(i.page_content) for i in textos] #Lista de parrafos
        parrafos = pd.DataFrame(textos, columns=["texto"])
        # print(parrafos)

        parrafos['Embedding'] = parrafos["texto"].apply(lambda x: get_embedding(x, engine='text-embedding-ada-002')) # Nueva columna con los embeddings de los parrafos
        
        # parrafos.to_csv(f'{self.doc_dir}REMOTE.csv')
        parrafos.to_pickle(f'{self.doc_dir}emb.pk')

        return parrafos