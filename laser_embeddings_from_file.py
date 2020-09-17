from laserembeddings import Laser
import tkinter.messagebox
from tkinter.filedialog import askopenfilename, mainloop

laser = Laser()

sourcename = askopenfilename(title="Open TXT file for embeddings", filetypes=[("TXT files", "*.txt")])
with open(sourcename, "r", encoding='utf-8-sig') as f:
    input = f.readlines()
    
embed_result = open(sourcename[:-4] + ".emb", "wb")
#embed_result = open(sourcename[:-4] + ".emb", "w", encoding='utf-8-sig')

embeddings = laser.embed_sentences(input, lang='ru').tofile(embed_result)

#print(embeddings)

embed_result.close()

tkinter.messagebox.showinfo("Title", "Success!")

mainloop()