import os
import re
from num2words import num2words

def __load_syllable_counts():
    filepath = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "syllable-counts.txt"
    )

    syllable_counts = {}

    with open(filepath) as f:
        for line in f:
            word, count = line.split()
            count = int(count)
            syllable_counts[word] = count

    return syllable_counts

SYLLABLE_COUNTS = __load_syllable_counts()

def sanitize_string(message):
    """
    Sanitizes the string by removing newlines, multiple whitespaces, and punctuation.
    Converts integers to words (1 -> "one", etc.)
    """
    # Remove all punctuation and other noise
    message = re.sub(r"[^\w]+", " ", message)

    # Replace all irregular or repeating whitespace characters with a single spaces
    message = re.sub(r"\s+", " ", message).lower().strip()

    # Convert all numbers to words
    message = re.sub(r"\d+", lambda match: num2words(int(match.group())), message)

    return message

def _build_line(input, start_index, length):
    """
    Builds a single Haiku line based on the entire input (which is a list of words in order).
    The starting index indicates which word we start at.
    The length indicates which line length we want to reach.
    If we pass the length, returns None, None.
    This is required because a valid Haiku doesn't just have 17 syllables, it also
    breaks them to 5,7,5 and so a sentence like "A solid masterpiece" won't work, since it
    must match exactly 5 without breaking apart words.
    """
    line = []
    current_index = start_index
    while get_syllable_count(" ".join(line)) < length:
        line.append(input[current_index])
        current_index += 1
    if get_syllable_count(" ".join(line)) > length: # We've gone over
        return None, None
    return line, current_index

def format_haiku(message):
    """
    Checks if the given string is a Haiku, and if it is, returns it
    in the proper haiku format (5-7-5).
    Otherwise returne None.
    """
    
    if get_syllable_count(message) != 17:
        return None

    words = sanitize_string(message).split(" ")
    first_line, end_index = _build_line(words, 0, 5)
    if not first_line:
        return None
    second_line, end_index = _build_line(words, end_index, 7)
    if not second_line:
        return None
    third_line, _ = _build_line(words, end_index, 5)
    if not third_line:
        return None
    
    return " ".join(first_line) + "\n" + " ".join(second_line) + "\n" + " ".join(third_line)

def get_syllable_count(message):
    """
    Counts the syllables in a given string.
    Sanitizes the string by removing newlines, multiple whitespaces, and punctuation.
    Converts integers to words (1 -> "one", etc.)
    Returns 0 if the string is empty, raises a KeyError if there's an unrecognized word.
    """
    message = sanitize_string(message)

    # Now split input into words
    words = message.split(" ")

    if not message:
        return 0
    
    total_syllables = 0
    for word in words:
        if word not in SYLLABLE_COUNTS:
            # Better fail loudly than silently
            raise KeyError(f"The word {word} was not found in the dictionary!")
        
        total_syllables += SYLLABLE_COUNTS[word]

    return total_syllables

__all__ = ["get_syllable_count"]
