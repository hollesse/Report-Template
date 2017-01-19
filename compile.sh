#!/usr/bin/env bash
#Run the Script from the folder you are in...
CURRENT_DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )

xelatex "$CURRENT_DIR/main.tex"
RETVAL="$?"
if [[ "${RETVAL}" -ne 0 ]] ; then
    echo "First xelatex run failed"
    exit ${RETVAL}
fi

biber "$CURRENT_DIR/main"
RETVAL="$?"
if [[ "${RETVAL}" -ne 0 ]] ; then
    echo "biber run failed"
    exit ${RETVAL}
fi

xelatex "$CURRENT_DIR/main.tex"
RETVAL="$?"
if [[ "${RETVAL}" -ne 0 ]] ; then
    echo "Second xelatex run failed"
    exit ${RETVAL}
fi

xelatex "$CURRENT_DIR/main.tex"
RETVAL="$?"
if [[ "${RETVAL}" -ne 0 ]] ; then
    echo "Third xelatex run failed"
    exit ${RETVAL}
fi

echo "PDF Compile: Success"
exit 0