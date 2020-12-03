#!/bin/bash

HUGO_DIR=".hugo"
SCRIPT_PATH="$( cd "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
ROOT_PATH="${SCRIPT_PATH}/../.."
HUGO_PATH="${ROOT_PATH}/${HUGO_DIR}"
CONFIG_FILE_PATH="${HUGO_PATH}/config/config.toml"
CONTENT_PATH="${HUGO_PATH}/content"

cd "${ROOT_PATH}"
hugo \
    --config="${CONFIG_FILE_PATH}" \
    --contentDir="${CONTENT_PATH}" \
    --destination="${ROOT_PATH}"
