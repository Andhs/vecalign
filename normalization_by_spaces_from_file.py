import re
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, mainloop

sourcename = askopenfilename(title="Open TXT file for normalization", filetypes=[("TXT files", "*.txt")])
with open(sourcename, "r", encoding='utf-8-sig') as f:
    input = f.readlines()
    #p = re.compile(r"\w+(?:'\w+)*|[^\w\s]")
prepro_all = open(sourcename[:-4] + "_prepro.txt", "w", encoding='utf-8-sig')
output_array = []
pattern = re.compile("^\s*$")
for i in input:
    # Пропускаем пустые строки и строки из пробелов, не пишем их в файл после обработки
    if not pattern.match(i):
        prepro = re.sub(r"([\w/'+$\s-]+|[^\w/'+$\s-]+)\s*", r"\1 ", i.rstrip())
        prepro_all.write(re.sub('\s+',' ', prepro) + "\n")

prepro_all.close()

tkinter.messagebox.showinfo("Title", "Success!")

mainloop()