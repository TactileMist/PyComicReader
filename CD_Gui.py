__author__ = 'Alexis'

from tkinter import *
from tkinter import filedialog
import io
from PIL import Image, ImageTk
import zipfile

class ComicDisplay():
    def __init__(self, master):
        frame = Frame(master)
        frame.pack(fill='both', expand=1)
        self.parent = master
        self.fname = ""
        self.label = Label(frame, bg="brown", height=800)
        # self.current_zip_file = filedialog.askopenfilename(filetypes=[(zip, "*.zip")])
        # self.current_zip_file = "C:\\Users\\Alexis\\Dropbox\\Photos.zip"
        self.current_zip_file = ""
        self.image_list = ["C:\\Users\\Alexis\\Dropbox\\rome_photo.jpg"]
        self.current_image_number = 0
        self.pil_image = self.acquire_image(None, self.image_list[self.current_image_number])
        self.tk_image = ImageTk.PhotoImage(self.pil_image)
        self.parent.title(self.fname)

        # self.label = Label(frame, image=self.tk_image, bg="brown", height=500)
        self.label.configure(image=self.tk_image)
        self.label.focus_set()
        self.label.bind("<Configure>", self.image_resizing)
        self.label.bind("<Left>", self.get_last_image)
        self.label.bind("<Right>", self.get_next_image)
        self.label.bind("o", self.open_new_file)
        self.label.bind("<Button-1>", self.get_next_image)
        self.label.pack(padx=5, pady=5, fill='both', expand=1)

    def acquire_image_list(self, zip_file):
        image_list = []
        with zipfile.ZipFile(zip_file, "r") as myFile:
            for filename in myFile.namelist():
                if ".jpg" in filename.lower() or ".jpeg" in filename.lower() or ".png" in filename.lower():
                    image_list.append(filename)
        image_list.sort()
        return image_list

    def acquire_image(self, zip_file, image_file):
        if zip_file is None:
            pil_image = Image.open(image_file)
            pil_image = self.image_sizer(pil_image)
        else:
            with zipfile.ZipFile(zip_file, "r") as myFile:
                self.fname = image_file
                image_bytes = myFile.read(image_file)
                data_stream = io.BytesIO(image_bytes)
                pil_image = Image.open(data_stream)
                pil_image = self.image_sizer(pil_image)
        return pil_image

    def image_sizer(self, image_file, window_size=800):
        w, h = image_file.size
        if w > h:
            image_file_height = int(h*(window_size/w))
            image_file = image_file.resize((window_size, image_file_height), Image.LANCZOS)
        else:
            image_file_width = int(w*(window_size/h))
            image_file = image_file.resize((image_file_width, window_size), Image.LANCZOS)
        return image_file

    def image_resizing(self, event):
        new_height = self.parent.winfo_height() - 14
        new_size_image = self.image_sizer(self.pil_image, new_height)
        self.tk_image = ImageTk.PhotoImage(new_size_image)
        self.label.configure(image=self.tk_image)

    def open_new_file(self, event):
        self.current_zip_file = filedialog.askopenfilename(filetypes=[("Comic Book File", "*.cbz *.zip"), ("Zip File", "*.zip")], initialdir="C:\\Users\\Alexis\\Dropbox\\")
        if len(self.current_zip_file) == 0:
            pass
        else:
            self.image_list = self.acquire_image_list(self.current_zip_file)
            self.current_image_number = 0
            self.update_image()

    def get_next_image(self, event):
        if len(self.current_zip_file) == 0:
            pass
        else:
            if self.current_image_number >= len(self.image_list)-1:
                self.current_image_number = 0
            else:
                self.current_image_number += 1
            self.update_image()

    def get_last_image(self, event):
        if self.current_image_number == 0:
            self.current_image_number = len(self.image_list)-1
        else:
            self.current_image_number -= 1
        self.update_image()

    def update_image(self):
        self.fname = self.image_list[self.current_image_number]
        self.pil_image = self.acquire_image(self.current_zip_file, self.image_list[self.current_image_number])
        self.tk_image = ImageTk.PhotoImage(self.pil_image)
        self.parent.title(self.fname)
        self.image_resizing(None)




root = Tk()
app = ComicDisplay(root)
root.mainloop()