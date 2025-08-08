from langchain.text_splitter import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_community.document_loaders.csv_loader import CSVLoader
from config.config import MODEL_NAME, HUGGINGFACE_API_KEY, EMBEDDING_MODEL_NAME
from utils.custom_exception import CustomException
from utils.logger import get_logger
from dotenv import load_dotenv
import sys

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)

logger = get_logger(__name__)

class VectorStoreBuilder:
    """
    Class for building and saving vector store
    
    
    """
    def __init__(self, file_path, persist_dir: str = "chroma_db"):
        self.file_path = file_path
        self.persist_dir = persist_dir
        self.embeddings = embeddings
        
    
    def build_and_save_vector_store(self):
        """Building the vector store and saving it to local

        Raises:
            CustomException: Error building and saving vector store
        """
        try:
            logger.info("Building and saving vector store...")
            text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
            loader = CSVLoader(file_path=self.file_path, encoding="utf-8", metadata_columns=[])
            documents = loader.load()
            texts = text_splitter.split_documents(documents)
            
            db = Chroma.from_documents(texts, self.embeddings, persist_directory=self.persist_dir)
            db.persist()
            logger.info(f"Vector store built and saved to:{self.persist_dir}")
        
        except Exception as e:
            logger.error(f"Error building and saving vector store: {e}")
            raise CustomException(e, sys)
    
    def load_vector_store(self):
        try:
            logger.info("Loading vector store...")
            db = Chroma(persist_directory=self.persist_dir, embedding_function=self.embeddings)
            return db
        except Exception as e:
            logger.error(f"Error loading vector store: {e}")
            raise CustomException(e, sys)