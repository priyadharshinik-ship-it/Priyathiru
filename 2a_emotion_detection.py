"""
Emotion Detection Application using Watson NLP Library

This application uses IBM Watson's Natural Language Processing (NLP) library
to detect and analyze emotions in text input.
"""

import requests
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

# Watson NLP Emotion Detection Function
def detect_emotion(text):
    """
    Detects emotions in the given text using Watson NLP library.
    
    Args:
        text (str): The input text to analyze for emotions
        
    Returns:
        dict: A dictionary containing emotion scores (sadness, joy, fear, disgust, anger)
    """
    
    # Initialize Watson NLP Emotion Detection
    nlu = NaturalLanguageUnderstandingV1(
        version='2021-08-01',
        iam_apikey='YOUR_WATSON_API_KEY',
        service_url='YOUR_WATSON_SERVICE_URL'
    )
    
    try:
        # Call Watson NLP Emotion Detection
        response = nlu.analyze(
            text=text,
            features=Features(emotion=EmotionOptions())
        ).get_result()
        
        # Extract emotion scores
        emotions = response['emotion']['document']['emotion']
        
        return emotions
    
    except Exception as e:
        print(f"Error in emotion detection: {str(e)}")
        return None


def analyze_emotions(text):
    """
    Analyzes emotions and returns formatted results.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Formatted emotion analysis results
    """
    
    emotions = detect_emotion(text)
    
    if emotions is None:
        return {"status": "error", "message": "Failed to detect emotions"}
    
    # Sort emotions by intensity
    sorted_emotions = sorted(emotions.items(), key=lambda x: x[1], reverse=True)
    dominant_emotion = sorted_emotions[0][0]
    
    result = {
        "status": "success",
        "text": text,
        "emotions": emotions,
        "dominant_emotion": dominant_emotion,
        "emotion_scores": dict(sorted_emotions)
    }
    
    return result


# Main Application
if __name__ == "__main__":
    
    # Test samples
    test_texts = [
        "I am feeling very happy and excited about this new opportunity!",
        "This is absolutely terrible and makes me very angry.",
        "I'm so sad and disappointed with the results.",
        "I'm afraid of what might happen next.",
        "This is disgusting and unacceptable."
    ]
    
    print("=" * 60)
    print("EMOTION DETECTION APPLICATION - WATSON NLP")
    print("=" * 60)
    
    for text in test_texts:
        print(f"\nAnalyzing: {text}")
        print("-" * 60)
        
        result = analyze_emotions(text)
        
        if result["status"] == "success":
            print(f"Dominant Emotion: {result['dominant_emotion'].upper()}")
            print("\nEmotion Scores:")
            for emotion, score in result['emotion_scores']:
                print(f"  {emotion:12} : {score:.4f}")
        else:
            print(f"Error: {result['message']}")
        
        print()
    
    print("=" * 60)
    print("Emotion Detection Complete")
    print("=" * 60)
