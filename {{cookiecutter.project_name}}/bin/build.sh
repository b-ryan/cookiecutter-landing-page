#!/bin/bash
set -eu
pelican \
    --delete-output-directory \
    --theme theme/ \
    --output "$1" \
    --settings "$2" \
    content/ # NB: the slash at the end is important!
