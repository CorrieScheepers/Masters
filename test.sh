#!/usr/bin/env bash

# remove pdf if present
[ -f Document.pdf ] && rm Document.pdf || echo "continue without remove"

# test if pdf is removed, fail if still present
[ -f Document.pdf ] && exit 1 || echo "continue building pdf output"


# build pdf from source
pdflatex Document.tex

# exit successfully if pdf is present or with error if not present
[ -f Document.pdf ] && exit 0 || exit 1