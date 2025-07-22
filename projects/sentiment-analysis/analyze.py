import sys
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
text = " ".join(sys.argv[1:]) if len(sys.argv) > 1 else "I love AI!"
score = analyzer.polarity_scores(text)

print(f"Positive: {score['pos']:.3f}, Negative: {score['neg']:.3f}, Neutral: {score['neu']:.3f}, Compound: {score['compound']:.3f}")
