# Import the requests library to handle HTTP requests
import requests
# Import the json library to manipulate json objects
import json

def emotion_detector(text_to_analyse):
    ''' Function named emotion_detector that takes a string input (text_to_analyse)
        and uses Watson AI to analyze the text.'''
     # URL of the emotion analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Set the headers required for the API request
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=header)
    # Format response to a JSON object
    formatted_response = json.loads(response.text)
    # Extract required set of emotions and creat dictionary with values
    anger_score = formatted_response['emotionPredictions'][0]['emotion']['anger']
    disgust_score = formatted_response['emotionPredictions'][0]['emotion']['disgust']
    fear_score = formatted_response['emotionPredictions'][0]['emotion']['fear']
    joy_score = formatted_response['emotionPredictions'][0]['emotion']['joy']
    sadness_score = formatted_response['emotionPredictions'][0]['emotion']['sadness']
    final_response = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    # Find dominant emotion which is emotion with the highest score
    dominant_emotion = max(zip(final_response.values(), final_response.keys()))[1]
    # Append dominant_emotion to new response format
    final_response['dominant_emotion'] = dominant_emotion
    # Return the response text from the API
    return final_response
    