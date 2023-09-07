# Health Insurance Cost Predictor

## Overview

The Health Insurance Cost Predictor is a Python application that uses Decision Tree Regression and Streamlit to help users estimate their health insurance costs. This project provides a user-friendly interface for inputting personal and health-related information, which is then used to predict insurance costs based on historical data and a Tuned Decision Tree Regression model.

### Prediction Page
![uplord2](https://github.com/rashmi0852/Heath_insurance_cost_predictor/assets/141851759/890cd545-9b05-44d8-b1ed-a6d1b0085027)

### Explore Page
![uplord4](https://github.com/rashmi0852/Heath_insurance_cost_predictor/assets/141851759/a294bb21-7dde-42f4-b439-142bba25d0f0)



## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Application](#running-the-application)
  - [Input Parameters](#input-parameters)
  - [Viewing Predictions](#viewing-predictions)
- [Data](#data)
- [Model](#model)
- [Contributing](#contributing)


## Getting Started

### Prerequisites

Before running the Health Insurance Cost Predictor, ensure you have the following prerequisites installed:

- Python 3.6 or higher
- pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```shell
   git clone https://github.com/yourusername/health-insurance-cost-predictor.git
   ```

2. Navigate to the project directory:

   ```shell
   cd health-insurance-cost-predictor
   ```

3. Install the required Python packages:

   ```shell
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

To start the Health Insurance Cost Predictor, run the following command in your terminal:

```shell
streamlit run webapp.py
```

This will launch a local web application, and you can access it through your web browser at `http://localhost:8501`.

### Input Parameters

The application will prompt you to enter various input parameters, including:

- Age
- Gender
- BMI (Body Mass Index)
- Number of children/dependents
- Smoking status
- Region

You can enter your information, and the application will use these inputs to predict your health insurance costs.

### Viewing Predictions

Once you've entered your information, click the "Predict" button, and the application will display the estimated health insurance cost based on the Decision Tree Regression model. You can also explore the predicted cost changes by adjusting the input parameters.

## Data

The Health Insurance Cost Predictor uses a dataset containing historical health insurance cost data. The dataset is included in the project under the `data` directory.

## Model

The core of this application is a Decision Tree Regression model trained on the provided data. The model is responsible for making predictions based on the input parameters.

## Contributing

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please create a GitHub issue or submit a pull request.



Thank you for using the Health Insurance Cost Predictor! We hope this tool helps you estimate your health insurance costs more effectively. If you have any questions or feedback, please don't hesitate to reach out.
rshmrnjnnayak@gmail.com
