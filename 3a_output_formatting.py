"""
Emotion Detection Application with Output Formatting
Modified emotion_detector function with correct output format

This is an enhanced version of the emotion detection application
that includes proper output formatting for emotion detection results.
"""

import requests
import json
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions


# Modified Watson NLP Emotion Detection Function with Output Formatting
def detect_emotion(text):
    """
    Detects emotions in the given text using Watson NLP library.
    Returns properly formatted output with emotion scores.
    
    Args:
        text (str): The input text to analyze for emotions
        
    Returns:
        dict: A properly formatted dictionary containing emotion scores and metadata
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
        
        # Format output with proper structure
        formatted_output = {
            "status": "success",
            "input_text": text,
            "emotion_detection": {
                "sadness": round(emotions.get('sadness', 0), 4),
                "joy": round(emotions.get('joy', 0), 4),
                "fear": round(emotions.get('fear', 0), 4),
                "disgust": round(emotions.get('disgust', 0), 4),
                "anger": round(emotions.get('anger', 0), 4)
            },
            "dominant_emotion": max(emotions, key=emotions.get),
            "confidence_score": round(max(emotions.values()), 4)
        }
        
        return formatted_output
    
    except Exception as e:
        print(f"Error in emotion detection: {str(e)}")
        return {
            "status": "error",
            "error_message": str(e),
            "input_text": text
        }


def format_emotion_output(emotion_result):
    """
    Formats the emotion detection output in a readable format.
    
    Args:
        emotion_result (dict): The emotion detection result dictionary
        
    Returns:
        str: Formatted string representation of emotion results
    """
    
    if emotion_result.get("status") == "error":
        return f"Error: {emotion_result.get('error_message')}"
    
    output_lines = []
    output_lines.append("=" * 70)
    output_lines.append("EMOTION DETECTION RESULTS")
    output_lines.append("=" * 70)
    output_lines.append(f"\nInput Text: {emotion_result['input_text']}")
    output_lines.append(f"\nDominant Emotion: {emotion_result['dominant_emotion'].upper()}")
    output_lines.append(f"Confidence Score: {emotion_result['confidence_score']}")
    output_lines.append("\nEmotion Scores:")
    output_lines.append("-" * 70)
    
    for emotion, score in emotion_result['emotion_detection'].items():
        bar_length = int(score * 30)
        bar = "█" * bar_length + "░" * (30 - bar_length)
        output_lines.append(f"  {emotion:10} : {score:.4f} | {bar}")
    
    output_lines.append("=" * 70)
    
    return "\n".join(output_lines)


def analyze_emotions(text):
    """
    Analyzes emotions and returns properly formatted results.
    
    Args:
        text (str): Input text to analyze
        
    Returns:
        dict: Formatted emotion analysis results with correct output structure
    """
    
    emotion_result = detect_emotion(text)
    return emotion_result


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
    
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "EMOTION DETECTION APPLICATION v2.0" + " " * 19 + "║")
    print("║" + " " * 18 + "Watson NLP - Output Formatting" + " " * 20 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
    
    for idx, text in enumerate(test_texts, 1):
        result = analyze_emotions(text)
        formatted_output = format_emotion_output(result)
        print(formatted_output)
        print("\n")
    
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 20 + "✓ EMOTION DETECTION COMPLETE" + " " * 21 + "║")
    print("║" + " " * 15 + "All texts analyzed with proper formatting" + " " * 12 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
