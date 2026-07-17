"""
EmotionDetection Package - Module Initialization
This __init__.py file imports and exposes the emotion detection application module.
"""

# Import the main emotion detection functions
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from watson_developer_cloud.natural_language_understanding_v1 import Features, EmotionOptions

# Import core functions from the emotion detection module
try:
    from .emotion_detection import (
        detect_emotion,
        analyze_emotions,
        format_emotion_output
    )
except ImportError:
    from emotion_detection import (
        detect_emotion,
        analyze_emotions,
        format_emotion_output
    )

# Define package metadata
__version__ = '2.0'
__author__ = 'Priyathiru'
__package_name__ = 'EmotionDetection'
__description__ = 'Watson NLP-based Emotion Detection Application'

# Define public API
__all__ = [
    'detect_emotion',
    'analyze_emotions',
    'format_emotion_output',
    'NaturalLanguageUnderstandingV1',
    'Features',
    'EmotionOptions'
]

# Package initialization message
def _package_info():
    """Returns package information."""
    return {
        'package_name': __package_name__,
        'version': __version__,
        'author': __author__,
        'description': __description__,
        'main_modules': __all__
    }

# Make package info accessible
package_info = _package_info()
