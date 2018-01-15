#!/bin/bash
set -e

DIR=.pelican.dev
if [[ -d $DIR ]]; then
    rm -r $DIR
fi
mkdir $DIR

trap 'kill %1; kill %2' SIGINT

# NB: the slash at the end of content/ is important!
pelican --debug --autoreload \
    --theme theme/ \
    --output $DIR/ \
    --settings pelicanconf.py \
    content/ &

sleep 3 # to give the pelican command in the background some time to write its
        # noise

cat <<EOF
#######################################################################
#                  http://localhost:{{cookiecutter.port}}             #
#######################################################################
EOF

cd $DIR
python -m pelican.server {{cookiecutter.port}}
