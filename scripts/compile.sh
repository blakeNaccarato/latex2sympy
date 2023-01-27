#!/bin/sh

# Get relative path of the root directory of the project
rdir=`git rev-parse --git-dir`
rel_path="$(dirname "$rdir")"
# Change to that path and run the file
cd $rel_path

# generate parser files
java -jar antlr-4.11.1-complete.jar -Dlanguage=Cpp -package latex2sympy -o gen PS.g4
# format parser files
# autopep8 --in-place gen/*.py
