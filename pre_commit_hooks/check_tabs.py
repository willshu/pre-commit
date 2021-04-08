import argparse, sys
from typing import Optional
from typing import Sequence

def replace_tabs_with_spaces(line, num_spaces=4):
    newline = line.replace('\t', (' ')*num_spaces)
    return newline

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    parser.add_argument('fix-tabs', nargs='1', type=bool, help='Replaced tabs with spaces')
    parser.add_argument('spaces', nargs='1', type=int, help='Number of spaces to replace tabs')
    args = parser.parse_args(argv)
    for filename in args.filenames:
        with open(filename, mode="r") as file:
            line_num = int(0)
            errors = ""
            list_of_lines = file.readlines()
            for num, line in enumerate(list_of_lines):
                if '\t' in line:
                    error = f"Tab found in {filename} on line {line_num} \n"
                    errors += error
                    if args.fix_tabs == True:
                        with open(filename, mode="w") as file:
                            list_of_lines[num] = replace_tabs_with_spaces(line, num_spaces=args.spaces)
                line_num += 1
            if errors:
                print(errors)
                return 1
            else:
                return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))