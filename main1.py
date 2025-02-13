import nltk
import re
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

# Ensure all necessary NLTK resources are available
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('stopwords')
nltk.download('wordnet')

# Function to preprocess text (Tokenization + POS Tagging)
def preprocess_text(text):
    sentences = sent_tokenize(text)  # Sentence tokenization
    preprocessed = []
    for sent in sentences:
        words = word_tokenize(sent)  # Word tokenization
        filtered_words = [word.lower() for word in words if word.isalnum()]
        pos_tags = pos_tag(filtered_words)  # POS tagging
        preprocessed.append((sent, pos_tags))
    return preprocessed

# Function to check if a sentence contains a task
def is_task_sentence(pos_tags):
    for i in range(len(pos_tags) - 1):
        current_tag = pos_tags[i][1]
        next_tag = pos_tags[i+1][1] if i+1 < len(pos_tags) else None
        if current_tag in ['MD'] and next_tag in ['VB', 'VBP', 'VBZ', 'VBD']:
            return True
    for i in range(len(pos_tags) - 2):
        tag1 = pos_tags[i][1]
        tag2 = pos_tags[i+1][1] if i+1 < len(pos_tags) else None
        tag3 = pos_tags[i+2][1] if i+2 < len(pos_tags) else None
        if tag1 in ['VBZ', 'VBP', 'VBD'] and tag2 == 'TO' and tag3 in ['VB', 'VBP']:
            return True
    return False

# Function to extract entities (e.g., a person assigned a task)
def extract_entity(original_sentence):
    words = word_tokenize(original_sentence)
    pos_tags = pos_tag(words)
    for word, tag in pos_tags:
        if tag in ['NNP', 'NN', 'PRP']:  # Proper Nouns, Nouns, Pronouns
            return word
    return None

# Function to extract tasks from text
def extract_tasks(text):
    preprocessed = preprocess_text(text)
    tasks = []
    for original_sent, pos_tags in preprocessed:
        if is_task_sentence(pos_tags):
            entity = extract_entity(original_sent)
            tasks.append({
                'task_sentence': original_sent,
                'entity': entity
            })
    return tasks

# Example Usage
if __name__ == "__main__":
    text = """Priya is at home. Her mother reminded her that she must clean the room before guests arrive. Later, she will go shopping with her friends."""

    tasks = extract_tasks(text)

    print("\n🔹 Extracted Tasks:")
    for task in tasks:
        print(f"✅ Task: {task['task_sentence']}")
        print(f"   - Entity: {task['entity']}\n")
