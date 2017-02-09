#!/bin/sh -
function test {
    echo "----TESTS----"
    cat allo.txt
    depot=$1; shift
    if [[ -f $depot ]]; then
      [[ $detruire ]] || erreur "Blah blah blah"
    fi
}
test
