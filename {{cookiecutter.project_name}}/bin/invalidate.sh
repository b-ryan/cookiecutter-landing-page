#!/bin/bash
set -eu
if [[ $# != 1 ]]; then
    echo >&1 "Usage: $0 space-separated-paths"
    exit 1
fi
DIST="{{cookiecutter.cloudfront_id}}"
if [[ -z $DIST ]]; then
    exit
fi
response=$(aws cloudfront create-invalidation --distribution-id $DIST --paths "$1")
id=$(jq -r '.Invalidation.Id' <<<"$response")
while true; do
    status_response=$(aws cloudfront get-invalidation --distribution-id $DIST --id "$id")
    status_=$(jq -r '.Invalidation.Status' <<<"$status_response")
    echo "$status_"
    if [[ $status_ != InProgress ]]; then
        break
    fi
    sleep 5
done
