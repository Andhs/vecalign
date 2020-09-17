import re
with open("Test.txt", "r", encoding='utf-8-sig') as f:
    input = f.readlines()
    #p = re.compile(r"\w+(?:'\w+)*|[^\w\s]")
prepro_all = open("Test_prepro.txt", "w", encoding='utf-8-sig')
output_array = []
for i in input:
    prepro = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", i)
    prepro_all.write(prepro)
prepro_all.close()
