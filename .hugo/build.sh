#!/bin/bash

SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
ROOT_PATH="${SCRIPT_PATH}/.."

cd "${ROOT_PATH}"
hugo \
    --config="${SCRIPT_PATH}/config.toml" \
    --contentDir="${SCRIPT_PATH}/content/" \
    --destination="${SCRIPT_PATH}/../"
