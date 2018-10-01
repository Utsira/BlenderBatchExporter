#!/usr/local/bin/python3

import os, subprocess, argparse

parser = argparse.ArgumentParser()
optional = parser._action_groups.pop()
required = parser.add_argument_group('required arguments')
required.add_argument('--input', '-i', help = "path to a folder containing .blend files", required = True, type = str)
required.add_argument('--output', '-o', help = "path to the folder to output converted files to.", required = True, type = str)
optional.add_argument('--blender', '-b', help = "path to the Blender command line tool. Defaults to /Applications/Blender/blender.app/Contents/MacOS/blender", type = str, default = '/Applications/Blender/blender.app/Contents/MacOS/blender')
optional.add_argument('--scale', help = "amount to scale the geometry by", type = float, default = 1)
parser._action_groups.append(optional)
args = parser.parse_args()

for file in os.listdir(args.input):
    nameExt = os.path.splitext(file)
    if nameExt[1] == ".blend":
        sourcePath = os.path.join(args.input, file)
        outputPath = os.path.join(args.output, nameExt[0] + ".obj")
        bashCommand = f'{args.blender} --background {sourcePath} --python exportObj.py -- {outputPath} {args.scale}'
        subprocess.check_call(bashCommand.split())
