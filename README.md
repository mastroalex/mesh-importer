# Mesh converter
## Description
Mesh converter to import Comsol Multiphysics meshes into Mathematica.

## Instruction

1. Export the mesh from Comsol as `.mphtxt` 
2. Clone the repository

```shell
git clone https://github.com/mastroalex/mesh-importer.git
```

3. Run the `meshConversion.py` script

```shell
python meshConversion.py
```

The python script works with three different mode:
- Script without any arguments will open a GUI asking for the `mesh.mphtxt` file. The output path is set as `/meshOutput/`.
- Script with one argument accepts for the `mesh.mphtxt` file path.

```shell
python meshConversion.py <path/to/mesh/mesh.mphtxt>
```
- Script with two arguments accepts for both the `mesh.mphtxt` file path and the output path

```shell
python meshConversion.py <path/to/mesh/mesh.mphtxt> <output/path>
```

## Mathematica integration

It is possibile to integrate it directly into Mathematica using the `ExternalEvaluate[]` function.

```mathematica
ExternalEvaluate["Shell", "cd " <> NotebookDirectory[] <> "\n git clone \ https://github.com/mastroalex/mesh-importer.git "]
```
