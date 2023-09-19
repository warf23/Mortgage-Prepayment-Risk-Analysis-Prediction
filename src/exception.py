
# Create a Custom exception class for handling errors in the program 

import sys # import sys module 

# function to get the error message details
def error_message_details(error , error_detail : sys ): 
    
    _,_,exc_tb = error_detail.exc_info() # get the exception traceback object
    
    file_name = exc_tb.tb_frame.f_code.co_filename # get the file name where the error occured 
    
    error_message = f"the error in file name --->|| {file_name} || \n the line number of the error --->|||| {exc_tb.tb_lineno}|||| \n the error message ---> ||||{error}||||"
    
    
    return error_message 


# custom exception class 
class CustomException(Exception): # inherit from Exception class 
    
    def __init__(self , error_message , error_detail : sys ):
        
        super().__init__(error_detail) # call the super class constructor 
        
        self.error_message = error_message_details(error_message , error_detail)
        
        # print the error message 
        def __str__(self):
            
            return self.error_message
        
        
        
    
    