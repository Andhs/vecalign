def mined_sentences(alignments, scores, src_file, tgt_file, src_file_lines, tgt_file_lines):
    with open(src_file, encoding='utf-8-sig') as source:
        source_lines_prep = source.readlines()
    with open(tgt_file, encoding='utf-8-sig') as target:
        target_lines_prep = target.readlines()
    with open(src_file_lines, encoding='utf-8-sig') as source:
        source_lines = source.readlines()
    with open(tgt_file_lines, encoding='utf-8-sig') as target:
        target_lines = target.readlines()
    mined_source_prep = open(src_file + "_mined.txt", "w", encoding='utf-8-sig')
    mined_target_prep = open(tgt_file + "_mined.txt", "w", encoding='utf-8-sig')
    mined_source = open(src_file + "_mined_lines.txt", "w", encoding='utf-8-sig')
    mined_target = open(tgt_file + "_mined_lines.txt", "w", encoding='utf-8-sig')

    for i in range(len(alignments)):
        if scores[i] > 0.1:
            for j in range(len(alignments[i][0])):
                mined_source_prep.write(source_lines_prep[alignments[i][0][j]].strip("\n"))
                mined_source.write(source_lines[alignments[i][0][j]].strip("\n"))
            mined_source_prep.write("\n")
            mined_source.write("\n")
            for k in range(len(alignments[i][1])):
                mined_target_prep.write(target_lines_prep[alignments[i][1][k]].strip("\n"))
                mined_target.write(target_lines[alignments[i][1][k]].strip("\n"))
            mined_target_prep.write("\n")
            mined_target.write("\n")
            
    mined_source_prep.close()
    mined_target_prep.close()
    mined_source.close()
    mined_target.close()