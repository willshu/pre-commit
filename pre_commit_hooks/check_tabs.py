import argparse
from typing import Optional
from typing import Sequence

def replace_tabs_with_spaces(line, num_spaces=4):
    newline = line.replace('\t', (' ')*num_spaces)
    return newline

def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*', help='Filenames to check.')
    args = parser.parse_args(argv)
    retval = 0
    for filename in args.filenames:
        with open(filename, mode="r") as file:
            line_num = int(0)
            errors = ""
            list_of_lines = file.readlines()
            for num, line in enumerate(list_of_lines):
                if '\t' in line:
                    error = f"Tab found in line {line_num} \n"
                    errors += error
                    list_of_lines[num] = replace_tabs_with_spaces(line)
                line_num += 1
            if errors:
                print(errors)
                return 1
            else:
                return retval

if __name__ == "__main__":
    exit(main())