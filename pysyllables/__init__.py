import os

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

def get_syllable_count(word):
    """If the dictionary contains the given word, returns the # of syllables in
    the word. Otherwise returns None."""
    return SYLLABLE_COUNTS.get(word.lower())

__all__ = ["get_syllable_count"]
