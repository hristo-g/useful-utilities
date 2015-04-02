#!/bin/bash

echo -e "[TTS]\n$(xsel)"

if [ -z "$1" ]
then
    espeak -s 150 -v en/en-us "$(xsel)" > /dev/null 2>&1
else
    if [ -z "$2" ]
    then
        echo "Writing TTS output to [${1}] ..."
        espeak -s 150 -v en/en-us "$(xsel)" --stdout | lame - "${1}"
    else
        echo "Writing [${1}] TTS output to [${2}] ..."
        espeak -s 150 -v en/en-us -f "${1}" --stdout | lame - "${2}"
    fi
fi

