import pandas as pd
from utils.logger import get_logger

logger = get_logger(__name__)

class AnimeDataLoader:
    def __init__(self, original_csv, processed_csv):
        self.original_csv = original_csv
        self.processed_csv = processed_csv
        
    def load_and_process(self):
        """Loading the original data and processing it to create a combined column for search

        Raises:
            ValueError: Raises if required columns are missing

        Returns:
            csv: Returns the processed csv
        """
        try:
            # Load and process data
            logger.info(f"Loading and processing data from: {self.original_csv}")
            df = pd.read_csv(self.original_csv, encoding='utf-8', on_bad_lines='skip').dropna() # Drop rows with missing values
            required_columns = {'Name','Genres','sypnopsis'} # Define required columns
            
            # Check if all required columns are present
            missing_columns = required_columns - set(df.columns)
            if missing_columns:
                raise ValueError(f"Missing columns: {', '.join(missing_columns)}") # Check if all required columns are present
            
            df['combined_info'] = (
                "Title: " + df['Name'] + " Overview: " + df['sypnopsis'] + " Genres: " + df['Genres'] # Combine columns
            )
            
            df[['combined_info']].to_csv(self.processed_csv, index=False, encoding='utf-8')     # Save processed data
            logger.info(f"Processed data saved to: {self.processed_csv}")
            
            return self.processed_csv
            
        
        except Exception as e:
            logger.error("Error loading and processing data: %s", str(e))
            raise e