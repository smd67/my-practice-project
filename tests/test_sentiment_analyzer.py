"""
Tests for the sentiment_analyzer module.
"""

import json
from unittest.mock import MagicMock, patch

from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

RESPONSE_JSON = json.loads(
    '{"documentSentiment":{"score":0.996586, "label":"SENT_POSITIVE", "mixed":false, '
    + '"sentimentMentions":[{"span":{"begin":0, "end":27, "text":"I love this new technology."},'
    + ' "sentimentprob":{"positive":0.9934198, "neutral":0.0030947884, '
    + '"negative":0.0034853641}}]}, '
    + '"targetedSentiments":{"targetedSentiments":{}, "producerId":'
    + '{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, '
    + '"producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
)


RESPONSE_NEGATIVE_JSON = json.loads(
    '{"documentSentiment":{"score":0.50, "label":"SENT_NEGATIVE", "mixed":false, '
    + '"sentimentMentions":[{"span":{"begin":0, "end":27, "text":"I hate this new technology."},'
    + ' "sentimentprob":{"positive":0.9934198, "neutral":0.0030947884, '
    + '"negative":0.0034853641}}]}, '
    + '"targetedSentiments":{"targetedSentiments":{}, "producerId":'
    + '{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, '
    + '"producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
)


RESPONSE_NEUTRAL_JSON = json.loads(
    '{"documentSentiment":{"score":0.75, "label":"SENT_NEUTRAL", "mixed":false, '
    + '"sentimentMentions":[{"span":{"begin":0, "end":27, "text":"I meh this new technology."},'
    + ' "sentimentprob":{"positive":0.9934198, "neutral":0.0030947884, '
    + '"negative":0.0034853641}}]}, '
    + '"targetedSentiments":{"targetedSentiments":{}, "producerId":'
    + '{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}, '
    + '"producerId":{"name":"Aggregated Sentiment Workflow", "version":"0.0.1"}}'
)

@patch("requests.post")
def test_sentiment_analyzer(mock_post):
    def mock_post_func(url, json, headers, timeout=10):
        retval = MagicMock()
        retval.json.return_value = RESPONSE_JSON
        retval.text = RESPONSE_JSON
        retval.status_code = 200
        return retval
    mock_post.side_effect = mock_post_func
    sentiment_dict = sentiment_analyzer("I love this new technology.")
    assert "label" in sentiment_dict.keys()
    assert "score" in sentiment_dict.keys()
    assert sentiment_dict["label"] == "SENT_POSITIVE"
    assert sentiment_dict["score"] == 0.996586

@patch("requests.post")
def test_sentiment_analyzer_neutral(mock_post):
    def mock_post_func(url, json, headers, timeout=10):
        retval = MagicMock()
        retval.json.return_value = RESPONSE_NEUTRAL_JSON
        retval.text = RESPONSE_NEUTRAL_JSON
        retval.status_code = 200
        return retval
    mock_post.side_effect = mock_post_func
    sentiment_dict = sentiment_analyzer("I meh this new technology.")
    assert "label" in sentiment_dict.keys()
    assert "score" in sentiment_dict.keys()
    assert sentiment_dict["label"] == "SENT_NEUTRAL"
    assert sentiment_dict["score"] == 0.75

@patch("requests.post")
def test_sentiment_analyzer_negative(mock_post):
    def mock_post_func(url, json, headers, timeout=10):
        retval = MagicMock()
        retval.json.return_value = RESPONSE_NEGATIVE_JSON
        retval.text = RESPONSE_NEGATIVE_JSON
        retval.status_code = 200
        return retval
    mock_post.side_effect = mock_post_func
    sentiment_dict = sentiment_analyzer("I hate this new technology.")
    assert "label" in sentiment_dict.keys()
    assert "score" in sentiment_dict.keys()
    assert sentiment_dict["label"] == "SENT_NEGATIVE"
    assert sentiment_dict["score"] == 0.50

@patch("requests.post")
def test_sentiment_analyzer_bad_status_code(mock_post):
    def mock_post_func(url, json, headers, timeout=10):
        retval = MagicMock()
        retval.json.return_value = RESPONSE_JSON
        retval.text = RESPONSE_JSON
        retval.status_code = 500
        retval.raise_for_status.side_effect = Exception("Bad status code")
        return retval
    mock_post.side_effect = mock_post_func
    try:
        sentiment_dict = sentiment_analyzer("I love this new technology.")
        assert False
    except Exception as e:
        assert str(e) == "Bad status code"
   