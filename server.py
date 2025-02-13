''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

# pylint: disable=W0718

#Initiate the flask app
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args.get('textToAnalyze')
    try:
        sentiment_dict = sentiment_analyzer(text)
        return (f"The given text has been identified as {sentiment_dict['label']} "
                + "with a score of {sentiment_dict['score']}.")
    except Exception:
        return "Invalid input! Try again."


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")


if __name__ == "__main__":
    # This functions executes the flask app and deploys it on localhost:5000
    app.run(port=5000, debug=True)
