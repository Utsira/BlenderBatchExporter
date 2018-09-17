#!/bin/sh
source_ext=".blend"
source_files="$1/*$source_ext"
output_root="$1/objFiles"

mkdir -p $output_root

for file in $source_files
do
    name=$(basename $file $source_ext)
    echo "Processing $name"
    output_file="$output_root/$name.obj"
    /Applications/Blender/blender.app/Contents/MacOS/blender --background $file --python exportObj.py -- $output_file 0.01
done
