def mined_sentences(alignments, scores, src_file, tgt_file, src_file_lines, tgt_file_lines):
    with open(src_file, encoding='utf-8-sig') as source:
        source_lines_prep = source.readlines()
    with open(tgt_file, encoding='utf-8-sig') as target:
        target_lines_prep = target.readlines()
    with open(src_file_lines, encoding='utf-8-sig') as source:
        source_lines = source.readlines()
    with open(tgt_file_lines, encoding='utf-8-sig') as target:
        target_lines = target.readlines()
    mined_source_prep = open(src_file[:-9] + "_mined.txt", "w", encoding='utf-8-sig')
    mined_target_prep = open(tgt_file[:-9] + "_mined.txt", "w", encoding='utf-8-sig')
    mined_source = open(src_file[:-9] + "_mined_lines.txt", "w", encoding='utf-8-sig')
    mined_target = open(tgt_file[:-9] + "_mined_lines.txt", "w", encoding='utf-8-sig')

    for i in range(len(alignments)):
        if scores[i] > 0.1:
            line_prep_source = " ".join(source_lines_prep[alignments[i][0]].strip("\n"))
            line_source = "   ".join(source_lines[alignments[i][0]].strip("\n"))
            mined_source_prep.write(line_prep_source)
            mined_source.write(line_source)
            if i < len(alignments)-1:
                mined_source_prep.write("\n")
                mined_source.write("\n")
            line_prep_target = " ".join(target_lines_prep[alignments[i][1]].strip("\n"))
            line_target = "   ".join(target_lines[alignments[i][1]].strip("\n"))
            mined_target_prep.write(line_prep_target)
            mined_target.write(line_target)
            if i < len(alignments)-1:
                mined_target_prep.write("\n")
                mined_target.write("\n")

    mined_source_prep.close()
    mined_target_prep.close()
    mined_source.close()
    mined_target.close()