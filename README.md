# Final_Intership_TechnoLabs_END_TO_END_Mortgage_Risk 💡💡💡 



This repository contains the code and resources for deploying a machine learning project end-to-end. The project is implemented using Python 3.10.

##   Setting up the Environment

To set up the required environment, follow these steps:

1. Install Anaconda or Miniconda, if not already installed.

2. Create a virtual environment using the following command:

   ```bash
   conda create -p Intershipvenv python==3.10.9 -y
   ```

   This command creates a virtual environment named `venv` with Python version 3.10.9

3. Activate the virtual environment:

   ```bash
   conda activate Intershipvenv
   ```

   This command activates the `Intershipvenv` virtual environment.



   
## Ignoring Virtual Environment

To avoid including your virtual environment in version control, create a `.gitignore` file in the root directory of your project if it doesn't already exist. Then, add the following line to the `.gitignore` file:

```plaintext
/venv/
```

## Dependencies

To install the project dependencies, run the following command:

```bash
pip install -r requirements.txt
```

This command will install all the required packages and libraries listed in the `requirements.txt` file.

## Usage

To use this project, follow these steps:

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/warf23/Final_Intership_Technocolabs_Softwares_END_TO_END_Mortgage_Risk.git
   ```
   
2. Change to the project directory:

   ```bash
   cd Final_Intership_Technocolabs_Softwares_END_TO_END_Mortgage_Risk
   ```
3.  Run the Python Application: Execute the following command to run the web application:
   ```bash
   python application.py
   ```

# Running ON AWS EC2  
https://github.com/warf23/Final_Intership_Technocolabs_Softwares_END_TO_END_Mortgage_Risk/assets/54336050/b7f54d28-6f6c-4bf2-a402-afe0f7d77963
# Project Overview 🏡📊









## Project Name
Mortgage Prepayment Risk Analysis

## Project Description 📝
The Mortgage Prepayment Risk Analysis project is aimed at developing a comprehensive tool to assess and predict the risk of prepayment associated with mortgage loans. Prepayment risk refers to the likelihood that borrowers will pay off their mortgage loans before the scheduled maturity date, typically through refinancing or early repayment.

## Purpose of the Project 🎯
The primary purpose of this project is to provide valuable insights into prepayment risk for mortgage lenders, financial institutions, and investors in mortgage-backed securities (MBS). Understanding and accurately predicting prepayment risk is crucial for making informed lending decisions, managing investments, and optimizing mortgage portfolio performance.

## Key Objectives 🌟
- Develop a predictive model: Create a robust machine learning algorithm that leverages historical mortgage data to predict the likelihood and timing of mortgage prepayments.
- User-friendly interface: Design a user-friendly web application that allows users to input loan and borrower information, obtain prepayment risk assessments, and make data-driven decisions.
- Risk mitigation: Assist mortgage lenders and investors in identifying high-risk loans, optimizing portfolios, and implementing risk mitigation strategies.

## Target Audience 🎯👥
This project's target audience includes:
- Mortgage Lenders: Banks, credit unions, and lending institutions seeking to assess and manage the prepayment risk associated with their mortgage portfolios.
- Investors: Individuals and organizations investing in mortgage-backed securities (MBS) who want to make informed investment decisions.
- Financial Analysts: Professionals in the finance industry looking for a tool to analyze prepayment risk and its impact on mortgage-related investments.
- Homebuyers: Potential homebuyers interested in understanding the factors that influence mortgage prepayment and refinancing decisions.

## Expected Outcomes 📈🔍
The Mortgage Prepayment Risk Analysis project aims to provide a practical and data-driven solution for assessing and managing prepayment risk in mortgage lending and investment. By offering a user-friendly web application and predictive model, users can make informed decisions to optimize their mortgage portfolios and reduce financial exposure to prepayment risk.

## Project Structure 
```
📁 artifacts
   └── preprocessor.joblib
   └── 📁 Models
      └── 📁 [Private Folders]

📁 src
   └── 📁 components
       └── 📁 data_cleaning
       └── 📁 Data_Preprocessor
       └── 📁 FeaturesEngineering
       └── 📁 Data_Ingestion
       └── 📁 Model_Trainer
   └── 📁 config
       └── 📄 entity_config.py
   └── 📁 Pipeline
       └── 📄 Data_Cleaning_STAGE0.py
       └── 📄 Features_Engineering_STAGE1.py
       └── 📄 Data_Ingestion_STAGE2.py
       └── 📄 Data_Transformation_STAGE3.py
       └── 📄 Models_Trainer_STAGE4.py
       └── 📄 predict_pipeline_STAGE_FINAL.py
   └── 📁 exception.py
   └── 📁 logger.py
   └── 📁 utils.py
📁 static
📁 templates
📄 .gitignore
📄 README.md
📄 application.py
📄 main.py
📄 requirements.txt
📄 sample_test.py
📄 setup.py
```
### Description of files 

`artifacts`: This directory contains artifacts related to your project, including the preprocessor.joblib file. It may also include subdirectories for model-related files in the Models folder.

`src`: This is the main source code directory.

`components`: This directory contains subdirectories for various components of your project, such as data cleaning, data preprocessing, feature engineering, data ingestion, and model training.
config: This directory contains configuration files for your project, such as entity_config.py.

`Pipeline`: This directory holds scripts related to the different stages of your data processing pipeline, from data cleaning to model training and prediction.

`exception.py`: This file likely contains custom exception classes for handling errors and exceptions in your project.

`logger.py`: This file may contain code for setting up and managing logging in your project.

`utils.py`: This file likely contains utility functions and helper code used throughout your project.

`static and templates`: These directories are typically used for web applications and may contain static files like stylesheets, images, and HTML templates.

`.gitignore`: This file specifies which files and directories should be ignored by Git version control.

`README.md`: The README file that provides an overview of your project, usage instructions, and other important information.

`application.py` and `main.py`: These files likely contain the main application logic for running your web application.

`requirements.txt`: This file lists the project dependencies and their versions.

`sample_test.py`: This file may contain sample tests for your project.

`setup.py`: A setup file that can be used for packaging and distributing your project.




## Contact

For any questions or inquiries, please feel free to reach out to me via email at [simo.agrat1@gmail.com](mailto:simo.agrat1@gmail.com) 
or connect with me on [LinkedIn](https://www.linkedin.com/in/mohammed-agrat/).
