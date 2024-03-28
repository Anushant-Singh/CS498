from textblob import TextBlob

def analyze_sentiment_and_adjust_scores(entries):
    """
    Analyzes sentiment of each text in the list `entries`, initially scoring them based on their sentiment.
    Each entry in the list is a dictionary with keys 'text', 'location', and 'time'.
    After scoring, it adjusts the scores so that the lowest score is set to -25, the highest to 25, 
    with all other scores proportionally distributed within that range.
    
    Args:
    entries (list of dict): List of dictionaries, each containing 'text', 'location', and 'time'.
    
    Returns:
    list of dict: Each dictionary contains the original 'text', 'location', 'time', and the new 'adjusted_score'.
    """
    initial_scores = []
    for entry in entries:
        blob = TextBlob(entry['text'])
        polarity = blob.sentiment.polarity
        initial_scores.append(polarity)

    # Find the min and max in the initial scores for normalization
    min_initial_score = min(initial_scores)
    max_initial_score = max(initial_scores)
    
    for index, score in enumerate(initial_scores):
        if min_initial_score != max_initial_score:
            adjusted_score = -25 + (score - min_initial_score) * (50 / (max_initial_score - min_initial_score))
        else:
            adjusted_score = 0
        entries[index]['adjusted_score'] = adjusted_score
    
    return entries

# Example entries with text, location, and time
entries = [
    {"text": "I love this product, it's absolutely wonderful!", "location": "California", "time": "January 2024"},
    {"text": "This is the worst experience I've ever had.", "location": "New York", "time": "February 2024"},
    {"text": "It was okay, neither good nor bad.", "location": "Texas", "time": "March 2024"},
    {"text": "Absolutely fantastic! I couldn't be happier.", "location": "Florida", "time": "April 2024"},
    {"text": "Terrible, just terrible. I regret my purchase.", "location": "Illinois", "time": "May 2024"},
    {"text": "Meh, I've seen better. It's somewhat disappointing.", "location": "Pennsylvania", "time": "June 2024"},
    {"text": "A masterpiece, truly a joy to experience.", "location": "Ohio", "time": "July 2024"},
    {"text": "What a disaster, a complete waste of time.", "location": "Michigan", "time": "August 2024"},
    {"text": "It's decent, but I expected more.", "location": "Georgia", "time": "September 2024"},
    {"text": "Exceeded all my expectations, simply amazing.", "location": "North Carolina", "time": "October 2024"}
]

# Analyzing sentiment and adjusting scores
adjusted_entries = analyze_sentiment_and_adjust_scores(entries)
for entry in adjusted_entries:
    print(f"Text: {entry['text']}\nLocation: {entry['location']}\nTime: {entry['time']}\nAdjusted Score: {entry['adjusted_score']:.2f}\n")
