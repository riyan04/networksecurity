import sys

from networksecurity.components.data_ingestion import DataIngestion

from networksecurity.exception import CustomException
from networksecurity.logger import logging

from networksecurity.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig

if __name__ == "__main__":
    try:
        training_pipeling_config = TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_pipeling_config)
        data_ingestion = DataIngestion(data_ingestion_config)

        logging.info("Initiate data ingestion")

        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()

        print(data_ingestion_artifact)
    except Exception as e:
        raise CustomException(e, sys)