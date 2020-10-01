#!/bin/bash
#
# export.sh
#
# export the codelab to the right directory

# Get markdown file name
codelab_markdown_filename=`ls *.md`
codelab_dir=`basename $codelab_markdown_filename .md`
rm -fr $codelab_dir

claat export -ga UA-3921398-10 -o ../../codelabs/ $codelab_markdown_filename
