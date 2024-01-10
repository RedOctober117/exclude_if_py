from pathlib import Path
import sys, re

def main():
    args = sys.argv[1:]
    # inputs = tuple(input('Enter terms to search for, separated by spaces: ').split(' '))
    pattern = '(?:' + '|'.join([ i for i in input('Enter terms to search for, separated by spaces: ').split(' ') ]) + ')'
    print(args)
    print(pattern)
    excludes = set()
    for path in args:
        cwd = Path(Path.home(), path)
        dig_path(cwd, excludes, pattern)
    print(excludes)

    with open('generated_excludes.txt', 'w') as exclude_txt:
        for line in excludes:
            print(line)
            exclude_txt.write(line.as_posix() + '\n')

def dig_path(cwd, excludes, pattern):
    print(f'Scanning {cwd}')
    try:
        to_be_excluded = [ Path('/', cwd.relative_to('/')) for i in cwd.iterdir() if re.match(pattern, i.name) != None ]
        if len(to_be_excluded) > 0:
            excludes.update(to_be_excluded)
        for subdir in [ i for i in cwd.iterdir() if i.is_dir() and i not in [i.name for i in to_be_excluded ] ]:
            dig_path(subdir, excludes, pattern)
    except: 
        print(f'ERROR: BROKEN AT {cwd.relative_to('/').as_posix()}')


if __name__ == '__main__':
    main()
