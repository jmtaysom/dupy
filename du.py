from pathlib import Path
from os.path import getsize, join
from os import walk


def format_file_size(p, block_size, h=''):
    """
    Iterate through all sub directories and format the file size
    for all children in each directory. Opperates in similar fashion
    to du --apparent-size
    :param p: filepath like object
    :param block_size: the size of the block either as an int
    :param h: If it is meant to be human readable append the unit of
              measurement.
    :return: A list of all the formated lines
    """
    path = Path(p)
    output = []
    for f in find_children(path):
        size = int(round(children_size(f)/block_size))
        output.append(f'{str(size)+h:<10} {f.absolute()}')
    return output

def children_size(p):
    """
    For a given directory find the summed file size of all files in
    all sub directories
    :param p: filepath like object
    :return: total file size in Bytes
    """
    size = 0
    for root, dirs, files in walk(p):
        for f in files:
            size += getsize(join(root, f))
    return size


def find_children(p, children=None):
    """
    Take a given file path and find all sub directories recursively
    :param p: filepath like object
    :param children: a list of subdirectories that will be searched next
    :return: the original directory and all sub directories in a list
    """
    if children is None:
        children = []
    if p.is_dir():
        children.append(p)
        for child in p.iterdir():
            find_children(child, children=children)
    return children


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='estimate file space usage',
        conflict_handler='resolve'
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-b',
        dest='block_size',
        action="store_const",
        const=1,
        help='set the block size as 1 byte'
    )
    group.add_argument(
        '-k',
        dest='block_size',
        action="store_const",
        const=1024,
        help='set the block size as 1 kilobyte'
    )
    group.add_argument(
        '-m',
        dest='block_size',
        action="store_const",
        const=1024**2,
        help='set the block size as 1 megabyte'
    )
    group.add_argument(
        '-g',
        dest='block_size',
        action="store_const",
        const=1024**3,
        help='set the block size as 1 gigabyte'
    )
    parser.add_argument('-h', action='store_true', help='format the response to be human readable')
    parser.add_argument('path', default='.', nargs='?', help='the parent path to be analyzed')

    args = parser.parse_args()
    if args.block_size is None:
        args.block_size = 1024
    readable_dict = {1: 'B', 1024: 'K', 1024**2: 'M', 1024**3: 'G'}
    if args.h:
        args.h = readable_dict[args.block_size]
    else:
        args.h = ''
    output = format_file_size(args.path, args.block_size, args.h)
    for line in output:
        print(line)
