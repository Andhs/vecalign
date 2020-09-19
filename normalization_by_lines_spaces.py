import re
import argparse

def norm_spaces(output_file, input_files):
    output = []
    pattern = re.compile("^\s*$")
    for fin in input_files:
        lines = open(fin, 'r', encoding='utf-8-sig').readlines()
        for out_line in lines:
            # Removing empty lines and whitespace lines
            if not pattern.match(out_line):
                prepro = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", out_line.rstrip())
                output.append(re.sub('\s+',' ', prepro) + "\n")

    with open(output_file, "w", encoding='utf-8-sig') as fout:
        for line in output:
            fout.write(line)

def _main():
    parser = argparse.ArgumentParser('Create normalized text file for further prccessing.',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-i', '--inputs', type=str, nargs='+',
                        help='input text file(s).')

    parser.add_argument('-o', '--output', type=str,
                        help='output normalized text file')

    args = parser.parse_args()
    norm_spaces(output_file=args.output,
       input_files=args.inputs)


if __name__ == '__main__':
    _main()