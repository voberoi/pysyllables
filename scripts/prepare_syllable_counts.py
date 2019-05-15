#!/usr/bin/env python3

import sys
import codecs

def main():
    syllable_counts = {}
    filepath = sys.argv[1]
    lines = codecs.open(filepath, encoding="iso-8859-1").read().split("\n")
    
    for line in lines:
        if line.startswith(";;;") or len(line) == 0 or line.isspace():
            continue

        word, phonemes = line.split(maxsplit=1)
        word = word.lower()
        syllable_count = 0
        for phoneme in phonemes.split():
            if phoneme[-1].isdigit():
                syllable_count += 1
        syllable_counts[word] = syllable_count

    for word in sorted(syllable_counts.keys()):
        syllable_count = syllable_counts[word]
        print(word + " " + str(syllable_count))

if __name__ == "__main__":
    main()
