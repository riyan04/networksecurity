import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation

from networksecurity.exception import CustomException
from networksecurity.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig, DataValidationConfig

if __name__ == "__main__":
    try:
        training_pipeling_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeling_config)
        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Initiate data ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        logging.info("Data initiation completed")
        print(data_ingestion_artifact)
        
        data_validation_config = DataValidationConfig(training_pipeling_config)
        data_validation = DataValidation(data_ingestion_artifact, data_validation_config)

        logging.info("Initiate the data validation")

        data_validation_artifact = data_validation.initiate_data_validation()

        logging.info("Data validation completed")

        print("\n\n")

        print(data_validation_artifact)
        
    except Exception as e:
        raise CustomException(e, sys)