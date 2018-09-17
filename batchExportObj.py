#!/usr/bin/env python

import os, subprocess, argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', '-p', help = "path to a folder containing .blend files", type = str)
parser.add_argument('--scale', help = "amount to scale the geometry by", type = float, default = 1)
args = parser.parse_args()

for file in os.listdir(args.path):
    nameExt = os.path.splitext(file)
    if nameExt[1] == ".blend":
        sourcePath = os.path.join(args.path, file)
        outputPath = os.path.join(args.path, "objFiles", nameExt[0] + ".obj")
        bashCommand = "/Applications/Blender/blender.app/Contents/MacOS/blender --background {source} --python exportObj.py -- {dest} {scale}".format(source = sourcePath, dest = outputPath, scale = args.scale)
        subprocess.check_call(bashCommand.split())
