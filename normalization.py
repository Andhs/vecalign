import re

def norm_lines(output_file, input_file):
    output = []
    pattern = re.compile("^\s*$")
    with open(input_file, "r", encoding='utf-8-sig') as fin:
        lines = fin.readlines()
    for out_line in lines:
        # Removing empty lines and whitespace lines
        if not pattern.match(out_line):
            output.append(out_line)

    with open(output_file, "w", encoding='utf-8-sig') as fout:
        for line in output:
            fout.write(line)

def norm_spaces(output_file, input_file):
    output = []
    with open(input_file, "r", encoding='utf-8-sig') as fin:
        lines = fin.readlines()
    for out_line in lines:
        prepro = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", out_line.rstrip())
        output.append(re.sub('\s+',' ', prepro) + "\n")

    with open(output_file, "w", encoding='utf-8-sig') as fout:
        for line in output[:-1]:
            fout.write(line)
        fout.write(output[-1])
