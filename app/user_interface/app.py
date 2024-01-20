# app/user_interface/app.py
from flask import Flask, render_template
from ..streaming_engine import StreamingEngine
from ..query_processor import QueryProcessor
from ..analytics_engine import AnalyticsEngine

app = Flask(__name__)
streaming_engine = StreamingEngine()
query_processor = QueryProcessor(streaming_engine)
analytics_engine = AnalyticsEngine()

@app.route('/')
def index():
    # Implement rendering logic for the user interface.
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

