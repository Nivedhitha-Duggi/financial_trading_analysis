# financial_trading_analysis
# Financial Trading Analysis

Financial Trading Analysis is a real-time analytics engine designed for analyzing streaming market data in the context of financial trading. This project utilizes Python, Flask, and various libraries for streaming data processing, B-tree-based indexing, query execution, and integration of analytics algorithms.


## 1. Installation

To run the project locally, follow these steps:

git clone https://github.com/your-username/financial-trading-analysis.git

cd financial-trading-analysis

python -m venv venv

source venv/bin/activate 


# On Windows, use venv\Scripts\activate
pip install -r requirements.txt


2. Usage
Running the Streaming Engine

cd app/user_interface
python app.py

Visit http://localhost:5000 in your web browser to interact with the user interface.

3. Project Structure
   
The project follows the following structure:

    • app/
   
        ◦ streaming_engine.py: Implementation of the streaming engine.
   
        ◦ query_processor.py: Logic for executing queries on streaming data.
   
        ◦ analytics_engine.py: Integration of analytics algorithms.
   
        ◦ user_interface/
   
            ▪ app.py: Flask application for the user interface.
   
            ▪ templates/: HTML templates for the user interface.
   
    • requirements.txt: List of project dependencies.

