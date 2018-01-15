#!/bin/bash
set -eu

GREEN='\033[0;32m'
NC='\033[0m'

PELICAN_OUTPUT_DIR=.pelican.prod

_green() {
    echo -e "${GREEN}$@...${NC}"
}

build() {
    _green "Building"
    bin/build.sh $PELICAN_OUTPUT_DIR publishconf.py
}

deploy() {
    _green "rsyncing code"
    aws s3 sync --delete $PELICAN_OUTPUT_DIR/ s3://www.polecat.io/
}

main() {
    build
    deploy
    bin/invalidate.sh /index.html
}

main "$@"
