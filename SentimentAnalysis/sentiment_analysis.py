"""
This module is used to analyze the sentiment of a given text.
"""

import requests


URL = (
    "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/"
    + "NlpService/SentimentPredict"
)
HEADERS = {
    "grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"
}
INPUT_JSON = {"raw_document": {"text": None}}


def sentiment_analyzer(text_to_analyse: str) -> dict:
    """
    Analyze the sentiment of a given text.
    """

    url = URL
    headers = HEADERS

    # depp copy of the json object INPUT_JSON
    myobj = INPUT_JSON.copy()
    myobj["raw_document"]["text"] = text_to_analyse

    response = requests.post(url, json=myobj, headers=headers, timeout=10)
    response.raise_for_status()

    print(response.status_code)
    return {
        "label": response.json()["documentSentiment"]["label"],
        "score": response.json()["documentSentiment"]["score"],
    }
