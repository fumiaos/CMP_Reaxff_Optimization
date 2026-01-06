# JAX-REAXFF Tools with cp2k Data

This repository contains format conversion scripts and original datasets built on top of the [JAX-REAXFF](https://github.com/cagrikymk/JAX-ReaxFF#) project.

## What’s Inside

Python scripts to convert XYZ → REAXFF input format
- `data/`: Original training datasets
- (data was get by using cp2k(https://www.cp2k.org/); cp2k input file by using multiwfn（http://sobereva.com/multiwfn/）)

## Quick start

```bash
python run.py --input data/stru.xyz --output example
