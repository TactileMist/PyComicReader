__author__ = 'Alexis'
import io
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import zipfile

# my_zip_file = filedialog.askopenfilename()
my_zip_file = "C:\\Users\\Alexis\\Dropbox\\Robyn_H_11774_4d5.zip"



# with zipfile.ZipFile("C:\\Users\\Alexis\\Documents\\Comics\\Main Library\\Orc Stain\\Orc Stain 01 (2010) (Minutemen-DTs).cbz", "r") as myFile:

# with zipfile.ZipFile(my_zip_file, "r") as myFile:
myFile = zipfile.ZipFile(my_zip_file, "r")
print(myFile.namelist()[5])
image_bytes = myFile.read(myFile.namelist()[5])
fname = myFile.namelist()[5]

root = tk.Tk()

data_stream = io.BytesIO(image_bytes)
pil_image = Image.open(data_stream)

w, h = pil_image.size

sf = "{} ({}x{})".format(fname, w, h)
root.title(sf)

if w > h:
    pil_img_height = int(h*(500/w))
    pil_image = pil_image.resize((500, pil_img_height), Image.ANTIALIAS)
else:
    pil_img_width = int(w*(500/h))
    pil_image = pil_image.resize((pil_img_width, 500), Image.ANTIALIAS)

tk_image = ImageTk.PhotoImage(pil_image)

if w > h:
    img_height = h*(500/w)
    label = tk.Label(root, image=tk_image, bg="brown", width=500, height=img_height)
else:
    img_width = w*(500/h)
    label = tk.Label(root, image=tk_image, bg="brown", height=500, width=img_width)
label.pack(padx=5, pady=5, fill='both', expand=1)

root.mainloop()