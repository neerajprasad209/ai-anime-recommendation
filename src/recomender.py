from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq
from src.prompt_template import get_anime_prompt
from utils.custom_exception import CustomException
from utils.logger import get_logger
import sys

logger = get_logger(__name__)

class AnimeRecommender:
    def __init__(self, retriever, api_key: str, model_name: str):
        self.llm = ChatGroq(api_key=api_key, model_name=model_name, temperature=0)
        
        self.prompt = get_anime_prompt()
        
        self.qa_chain = RetrievalQA.from_chain_type(
                                                    llm=self.llm,
                                                    chain_type="stuff",
                                                    retriever=retriever,
                                                    return_source_documents=True,
                                                    chain_type_kwargs={"prompt": self.prompt}
                                                )
        
    def get_recommendations(self, query:str):
        """Getting ther recommendations

        Args:
            query (str): Query

        Returns: 
            str: Recommendations
        """
        try:
            logger.info(f"Getting recommendations for query: {query}")
            
            results = self.qa_chain.invoke({"query": query})
            return results['result']
        
        except Exception as e:
            logger.error(f"Error getting recommendations: {e}")
            raise CustomException(e, sys)