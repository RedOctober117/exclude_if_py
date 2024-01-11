from pathlib import Path
import sys, re

def main():
    args = sys.argv[1:]

    pattern = re.compile('(?:' + '|'.join([ re.escape(i) for i in input('Enter terms to search for, separated by spaces: ').split(' ') ]) + ')')
    print(f'Searching {args} for {pattern.pattern}')
    excludes = set()

    for path in args:
        cwd = Path(Path.home(), path)
        dig_path(cwd, excludes, pattern)

    write_excludes(Path.cwd(), 'generated_excludes.txt', excludes)


def write_excludes(cwd, file, excludes):
    print(f'Writing to \'{file}\'')
    with open(file, 'w') as exclude_txt:
        for line in excludes:
            exclude_txt.write(line.as_posix() + '\n')
    print(f'File writen at {Path(cwd, file)}')

def dig_path(cwd, excludes, pattern):
    try:
        anchored_path = Path(cwd.root, cwd)
        for item in cwd.iterdir():
            if pattern.match(item.name) != None:
                excludes.add(anchored_path)
                break
        for subdir in [ i for i in cwd.iterdir() if i.is_dir() and anchored_path not in excludes ]:
            dig_path(subdir, excludes, pattern)
    except: 
        print(f'ERROR: BROKEN AT {anchored_path.as_posix()}')


if __name__ == '__main__':
    main()
