"""
Emotion Detection Module

This module provides emotion detection functionality using Watson NLP API.
"""

import requests


def emotion_detector(text_to_analyze):
    """
    Analyzes the emotion in the provided text using Watson NLP Emotion Predict API.

    Args:
        text_to_analyze (str): The text to analyze for emotions

    Returns:
        str: The text response from the Watson NLP API
    """
    # Watson NLP API endpoint
    url = ('https://sn-watson-emotion.labs.skills.network/v1/'
           'watson.runtime.nlp.v1/NlpService/EmotionPredict')

    # Headers required for the API
    headers = {
        "grpc-metadata-mm-model-id":
            "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON format
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the POST request to Watson NLP API with timeout
    response = requests.post(url, json=input_json, headers=headers,
                             timeout=10)

    # Return the text attribute of the response
    return response.text
