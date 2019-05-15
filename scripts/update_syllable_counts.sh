#!/usr/bin/env sh

curl https://raw.githubusercontent.com/Alexir/CMUdict/master/cmudict-0.7b > /tmp/cmudict-0.7b
./scripts/prepare_syllable_counts.py /tmp/cmudict-0.7b > pysyllables/syllable-counts.txt
