#!/bin/bash
for w in "$@"; do awk -F'\t' -v w="$w" '$2==w {print $2" | "$4" | "$6" | "$8}' /private/tmp/claude-501/-Users-riquochet-code/3bd24d67-84a6-491f-a780-8a0eb6efa512/scratchpad/wf12/lexicon_orrowen_full.tsv; done
