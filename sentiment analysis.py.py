# Importing necessary libraries
from nltk.sentiment import SentimentIntensityAnalyzer

# Initialize SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

# Function to perform sentiment analysis
def analyze_sentiment(text):
    # Get sentiment scores for the text
    sentiment_score = sia.polarity_scores(text)
    
    # Determine sentiment based on compound score
    compound_score = sentiment_score['compound']
    
    if compound_score >= 0.05:
        sentiment = 'Positive'
    elif compound_score <= -0.05:
        sentiment = 'Negative'
    else:
        sentiment = 'Neutral'
    
    return sentiment, sentiment_score

# Example usage
if __name__ == "__main__":
    text = input("Enter text for sentiment analysis: ")
    
    sentiment, sentiment_score = analyze_sentiment(text)
    
    print(f"Sentiment: {sentiment}")
    print(f"Sentiment Scores: {sentiment_score}")
