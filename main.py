from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME= 'Data Ingestion Stage'
try:
    logger.info(f'stage {STAGE_NAME} started')
    data_ingestion=DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'stage {STAGE_NAME} completed  \nx=======================x')
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME_1= 'Data Validation Stage'
try:
    logger.info(f'stage {STAGE_NAME_1} started')
    data_Validation=DataValidationTrainingPipeline()
    data_Validation.main()
    logger.info(f'stage {STAGE_NAME_1} completed  \nx=======================x')
except Exception as e:
    logger.exception(e)
    raise e