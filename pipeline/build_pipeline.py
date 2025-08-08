from src.data_loader import AnimeDataLoader
from src.vector_store import VectorStoreBuilder
from config.path_config import INPUT_CSV_PATH
from utils.logger import get_logger
from utils.custom_exception import CustomException
from dotenv import load_dotenv

logger = get_logger(__name__)
load_dotenv()


def main():
    try:
        logger.info("Started the Builder Pipeline")
        data_loader = AnimeDataLoader(original_csv=INPUT_CSV_PATH, processed_csv="data/processed_anime.csv")
        processed_csv = data_loader.load_and_process()
        logger.info("CSV Anime Data loaded Successfully and Processed")
        
        vector_build = VectorStoreBuilder(file_path = processed_csv, persist_dir = "chroma_db")
        
        vector_build.build_and_save_vector_store()
        logger.info("Vector store built and saved to local successfully")
        
        logger.info("Completed the Builder Pipeline")
        
    except Exception as e:
        logger.error(f"Failed to get Execute the pipeline: {e}")
        raise CustomException("Error getting Execute the pipeline",e)
    
    
if __name__ == "__main__":
    main()