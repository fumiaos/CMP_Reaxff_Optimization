from pathlib import Path
def merge_xyz(folder: Path = Path('.'),
              outfile: str = 'total.xyz') -> None:
    xyz_files = sorted(folder.glob('*.xyz'))
    if not xyz_files:
        print('no .xyz format file in this directory')
        return
    with open(folder / outfile, 'wb') as fout:
        for f in xyz_files:
            fout.write(f.read_bytes())
            print(f'merging: {f}')
    print(f'done -> {outfile}')
if __name__ == '__main__':
    merge_xyz()