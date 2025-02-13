# Task Extraction from Text

This Python project uses Natural Language Processing (NLP) techniques to automatically extract tasks from text. It identifies task-related sentences and extracts relevant entities (people or subjects) associated with those tasks.

## Features

- Task identification using POS (Part of Speech) tagging
- Entity extraction for task assignments
- Support for various task sentence structures
- Simple and easy-to-use interface

## Requirements

- Python 3.11
- NLTK library

## Installation

1. Clone this repository
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. The script will automatically download required NLTK resources on first run

## Usage

```python
from main1 import extract_tasks

# Example text
text = """Priya is at home. Her mother reminded her that she must clean the room before guests arrive. 
Later, she will go shopping with her friends."""

# Extract tasks from the text
tasks = extract_tasks(text)

# Print the extracted tasks
for task in tasks:
    print(f"Task: {task['task_sentence']}")
    print(f"Entity: {task['entity']}\n")
```

### Example Output:
```
🔹 Extracted Tasks:
✅ Task: she must clean the room before guests arrive.
   - Entity: she

✅ Task: she will go shopping with her friends.
   - Entity: she
```

## How It Works

1. **Text Preprocessing**: The text is tokenized into sentences and words, and POS tagging is applied.
2. **Task Identification**: Sentences are analyzed for task-like structures using POS patterns.
3. **Entity Extraction**: The system identifies the subject (person or entity) associated with each task.

## Notes

- The system uses NLTK's POS tagger to identify sentence structures
- Entity extraction focuses on proper nouns, nouns, and pronouns
- The project is designed to be easily extendable for additional features