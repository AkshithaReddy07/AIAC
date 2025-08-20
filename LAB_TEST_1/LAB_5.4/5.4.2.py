import re
from collections import Counter

def preprocess_text(text):
    # Lowercase and remove non-alphabetic characters
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    return text

def simple_sentiment_analysis(text, positive_words, negative_words):
    words = preprocess_text(text).split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

def detect_and_handle_bias(text, bias_words):
    words = preprocess_text(text).split()
    bias_found = [word for word in words if word in bias_words]
    if bias_found:
        print("Warning: Potential bias detected in the input text:", ', '.join(set(bias_found)))
        # Optionally, remove bias words for fairer analysis
        words = [word for word in words if word not in bias_words]
        return ' '.join(words)
    return ' '.join(words)

def main():
    # Example word lists (in practice, use more comprehensive lists)
    positive_words = {"good", "happy", "excellent", "fortunate", "correct", "superior", "love", "great", "positive"}
    negative_words = {"bad", "sad", "poor", "unfortunate", "wrong", "inferior", "hate", "terrible", "negative"}
    # Example bias words (could be expanded based on domain)
    bias_words = {"always", "never", "everyone", "nobody", "obviously", "clearly"}

    print("Sentiment Analysis Tool (with Bias Detection)")
    user_input = input("Enter text for sentiment analysis: ")

    # Detect and handle bias
    processed_text = detect_and_handle_bias(user_input, bias_words)

    # Sentiment analysis
    sentiment = simple_sentiment_analysis(processed_text, positive_words, negative_words)
    print("Sentiment:", sentiment)

    print("\nEthical Notice:")
    print("1. This tool uses simple word lists and may not capture all nuances of sentiment or bias.")
    print("2. Bias detection is based on a small set of potentially loaded words; real-world bias is more complex.")
    print("3. For critical applications, use advanced models and regularly audit for fairness and bias.")

if __name__ == "__main__":
    main()
