# Batch Blender export

Exports a folder full of Blender files to OBJ format. Defaults: selected object only, triangulate faces, export normals and UVs, Y-Up

### Usage 

```
batchExportObj.py [-h] --input INPUT --output OUTPUT [--scale SCALE]

required arguments:
  --input INPUT, -i INPUT
                        path to a folder containing .blend files
  --output OUTPUT, -o OUTPUT
                        path to the folder to output converted files to.

optional arguments:
  -h, --help            show this help message and exit
  --scale SCALE         amount to scale the geometry by
```

### Example

`./batchExportObj.py --input ../Blender/lopoly --output ../ARModeller/LoPoly --scale 0.02`
