from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationPipeline
from src.textSummarizer.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline
from src.textSummarizer.pipeline.stage_05_model_evaluation import ModelEvaluationTrainingPipeline
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



STAGE_NAME_2= 'Data Transformation Stage'
try:
    logger.info(f'stage {STAGE_NAME_2} started')
    data_Transformation= DataTransformationPipeline()
    data_Transformation.main()
    logger.info(f'stage {STAGE_NAME_2} completed  \nx=======================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_3= 'Model Trainer Stage'
try:
    logger.info(f'stage {STAGE_NAME_3} started')
    model_trainer= ModelTrainerTrainingPipeline()
    model_trainer.main()
    logger.info(f'stage {STAGE_NAME_3} completed  \nx=======================x')
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME_4= 'Model Evaluation Stage'
try:
    logger.info(f'stage {STAGE_NAME_4} started')
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation .main()
    logger.info(f'stage {STAGE_NAME_4} completed  \nx=======================x')
except Exception as e:
    logger.exception(e)
    raise e