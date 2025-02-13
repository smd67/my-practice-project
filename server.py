''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
# Import the sentiment_analyzer function from the package created: TODO
from flask import Flask, render_template, request
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : TODO
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    # TODO
    text = request.args.get("text")
    sentiment_dict = sentiment_analyzer(text)
    return f"Sentiment is {sentiment_dict['label']} with a confidence score of {sentiment_dict['score']}"


@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    #TODO
    return render_template("index.html")

if __name__ == "__main__":
    ''' 
    This functions executes the flask app and deploys it on localhost:5000
    '''
    #TODO
    app.run(port=5000, debug=True)
