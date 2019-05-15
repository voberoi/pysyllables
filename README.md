# pysyllables

An in-memory syllable count dictionary for North American English derived from 
the CMU Pronouncing Dictionary.

```
>>> from pysyllables import get_syllable_count
>>> get_syllable_count("fabulous")
3
>>> get_syllable_count("word-that-doesn't-exist")
None
```

## Where do these syllable counts come from?

From the [CMU Pronouncing Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict),
an open-source machine-readable pronunciation dictionary for North American English
that contains over 134,000 words and their pronunciations.

By counting the number of lexical stress markers in each word's pronunciation, we can
compute the # of syllables in each word. This library ships with a file that maps each
word to a syllable count in [pysyllables/syllable-counts.txt](pysyllables/syllable-counts.txt)

## How does one generate [pysyllables/syllable-counts.txt](pysyllables/syllable-counts.txt)?

[scripts/download_syllable_counts.sh](scripts/download_syllable_counts.sh) downloads
the CMU Pronouncing Dictionary, computes each word's syllable count, and emits.
[pysyllables/syllable-counts.txt](pysyllables/syllable-counts.txt).

Should there be a new version of the CMU Pronouncing Dictionary, update the source in
scripts/download_syllable_counts.sh](scripts/download_syllable_counts.sh).

## Contributing

Questions & contributions welcome -- please open an issue or, even better, a PR!
