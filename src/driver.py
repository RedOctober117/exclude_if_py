from pathlib import Path
import sys

contain_matches = ['.git']

def main():
    args = sys.argv[1:]
    print(args)
    excludes = set()
    for path in args:
        cwd = Path(Path.home(), path)
        dig_path(cwd, excludes)
    print(excludes)

    with open('generated_excludes.txt', 'w') as exclude_txt:
        for line in excludes:
            print(line)
            exclude_txt.write(line + '\n')

def dig_path(cwd, excludes):
    print(f'Scanning {cwd}')
    try:
        to_be_excluded = [ Path('/', cwd.relative_to('/')).as_posix() for i in cwd.iterdir() if i.name == '.git' and i.is_dir() ]
        if len(to_be_excluded) > 0:
            excludes.update(to_be_excluded)
        for subdir in [ i for i in cwd.iterdir() if i.is_dir() ]:
            dig_path(subdir, excludes)
    except: 
        print(f'BROKEN AT {cwd.relative_to('/'.as_posix())}')


if __name__ == '__main__':
    main()
