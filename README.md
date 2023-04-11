# EMOTION BASED PARENTS NOTIFICATION SYSTEM

In this emotion based parents notification system, we send notifications to the parents, when there children call recording are found to be sad. so that the parents can help in giving emotional support to there children. 

1. Analysing of model.ipynb

To analyse the recording, we must first find which is the best model to find the emotion of the person through audio file. To find that, we go through some of the models and they are

1. MLP classifier
2. Long short term memory(LSTM)
3. CNN(Convolution neural network)

In the end, we found that LSTM has more accuracy that any other model which is 99.98% accuracy. Even though we got better accuracy, we go through took a type of sad data from the TESS dataset and we check whether it really predicts the emotion and if we can get the notification from "Pushbullet" app or not(Last cell).

2. Implementation in real time(realtime.py)

Since we found that LSTM is the best model in predicting the person emotion from audio, we have downloaded the model and we have recorded the audio(until we press "q"). once we have recorded we have used the same model which we specified above to predict the output and if the model says it's a sad audio. we have used Pushbullet API key to send notification to the parent mobile.

Note:- for the training purpose, we have used RAVDESS(Ryerson Audio-Visual Database of Emotional Speech and Song) and TESS(Toronto emotional speech set).
