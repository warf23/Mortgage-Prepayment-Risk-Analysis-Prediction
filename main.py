from src.pipeline.Data_Cleaning_STAGE0 import Datacleaning

from src.pipeline.Features_Engineering_STAGE1 import FeaturesEngineering

from src.pipeline.Data_Ingestion_STAGE2 import DataIngestion


from src.exception import CustomException
from src.logger import logging
import sys
from src.components.Model_Trainner.Regression_Model.reg import Reg_ModelTrainer
from src.components.Model_Trainner.Classification_Model.clas import Classification_ModelTrainer


STAGE_NAME = " Data Cleaning "
try : 
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Datacleaning().initiate_data_cleaning()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    print(e)
    raise CustomException(e , sys )


STAGE_NAME = " Features Engineering "
try :
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    my_data =FeaturesEngineering().initiate_Features_Engineering()
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    
    raise CustomException(e , sys )

STAGE_NAME = " Data Ingestion "
try :
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from src.pipeline.Data_Ingestion_STAGE2 import DataIngestion
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion(my_data)
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    raise CustomException(e , sys )


STAGE_NAME = " Data Transformation "
try :
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from src.pipeline.Data_Transformation_STAGE3 import DataTransformation
    obj = DataTransformation()
    train_array_classification,test_array_classification,train_array_Regression, test_array_Regression, _ =obj.initiale_data_transormation(train_data,test_data)
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    raise CustomException(e , sys )

STAGE_NAME = " Regression Model Training "
try : 
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    Reg_ModelTrainer().initiate_model_trainer(train_array_Regression,test_array_Regression)
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    raise CustomException(e , sys )

STAGE_NAME = " Classification Model Training "
try :
    logging.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")

    Classification_ModelTrainer().initiate_model_trainer(train_array_classification , test_array_classification )
    logging.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e :
    raise CustomException(e , sys )



