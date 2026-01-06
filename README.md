# JAX-REAXFF Tools with cp2k Data

This repository contains format conversion scripts and original datasets built on top of the [JAX-REAXFF](https://github.com/cagrikymk/JAX-ReaxFF#) project.

## What’s Inside

- `scripts/`: Python scripts to convert XYZ → REAXFF input format
- `data/`: Original training datasets (cauculated by using cp2k(https://www.cp2k.org/) cp2k input file writing by multiwfn（http://sobereva.com/multiwfn/）)

## Quick start

```bash
python run.py --input data/stru.xyz --output example
