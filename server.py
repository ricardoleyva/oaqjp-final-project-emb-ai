''' Executing this function initiates the application of emotion detection
    to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package:
from flask import Flask, render_template, request
# Import the emotion_detector function from the package created:
from EmotionDetection.emotion_detection import emotion_detector
# Initiate the flask app:
app = Flask("Emotion Detector")

# Create decorator for the application calling function
@app.route("/emotionDetector")
def sent_analyzer():
        ''' This code receives the text from the HTML interface and 
        runs emotion detection over it using emotion_detector()
        function. The output returnedis a dictionary with all
        emotions, its score and at last the dominant_emotion.
    '''
    # Save value of arguments from GET request
    text_to_analyze = request.args.get('textToAnalyze')
    # Run emotion_detector function with value from GET request
    response = emotion_detector(text_to_analyze)
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']
    # Return formatted string
    res_0 = "For the given statement, the system response is "
    res_1 = f"'anger': {anger}, 'disgust':{disgust}, 'fear':{fear}, "
    res_2 = f"'joy': {joy}, 'sadness':{sadness}. "
    res_3 = f"The dominant emotion is:<b>{dominant_emotion}</b>."
    return res_0 + res_1 + res_2 + res_3

# Create decorator for index
@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

# Code to deploy app
if __name__ == "__main__":
    #This functions executes the flask app and deploys it on localhost:5000
    app.run(host="0.0.0.0", port=5000)