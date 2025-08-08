from src.vector_store import VectorStoreBuilder
from src.recomender import AnimeRecommender
from config.config import MODEL_NAME, GROQ_API_KEY
from utils.logger import get_logger
from utils.custom_exception import CustomException
import sys

logger = get_logger(__name__)


class AnimeRecommenderPipeline:
    def __init__(self, persist_dir: str = "chroma_db"):
        try: 
            logger.info("Initializing Anime Recommender Pipeline")
            
            vector_build = VectorStoreBuilder(file_path="", persist_dir=persist_dir)
            logger.info("Vector store built and saved to local")
            
            retriver = vector_build.load_vector_store().as_retriever()
            logger.info("Vector store loaded")
            
            self.recommender = AnimeRecommender(retriever=retriver, api_key=GROQ_API_KEY, model_name=MODEL_NAME)
            logger.info("Pipeline Anime Recommender initialized")
            
        except Exception as e:
            logger.error(f"Failed to get initialize Anime Recommender Pipeline: {e}")
            raise CustomException("Error initializing Anime Recommender Pipeline",e)
        
    def recommend(self, query: str):
        try:
            logger.info(f"Getting recommendations for query: {query}")
            
            recomendation  = self.recommender.get_recommendations(query=query)
            logger.info(f"Recommendations obtained: {recomendation}")
            
            return recomendation
        
        except Exception as e:
            logger.error(f"Failed to get recommendations: {e}")
            raise CustomException("Error getting recommendations",e)
        
        