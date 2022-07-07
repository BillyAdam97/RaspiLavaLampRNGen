from tkinter import *
import hashlib
import random
from picamera import PiCamera
import PIL.Image
import PIL.ImageTk


def take_img(cam_2):
    cam_2.capture('image.jpg', resize=(300,200))
    pic = PIL.ImageTk.PhotoImage(PIL.Image.open('image.jpg'))
    return pic

def read_bytes():
    with open('image.jpg', 'rb') as img:
        f = img.read()
        b = bytearray(f)
    return list(b)

def hash_seed(result):
    r2 = []
    for i in range(len(result)):
        if i%3==0:
            r2.append(result[i])
    b = bytearray(r2)
    hashed = hashlib.sha1(b).hexdigest()
    return hashed

def create_num(hashed, low, high):
    random.seed(hashed)
    return random.randint(low,high)

def generate(cam_1):
    _min = e1.get()
    _max = e2.get()
    a = take_img(cam_1)
    im = Label(root, image=a)
    im.image = a
    im.place(relx=0.75,rely=0.2, anchor='ne')
    bytearr = read_bytes()
    hashed_num = hash_seed(bytearr)
    num = create_num(hashed_num, int(_min), int(_max))
    hashing.config(text=f'{hashed_num}')
    ans.config(text=f'{num}')

root = Tk()
root.title("LavaLamp Random Number Generator")
root.geometry('1050x350')
cam = PiCamera()
l1 = Label(root, text="Min:")
e1 = Entry(root, width=10)
l2 = Label(root, text="Max:")
e2 = Entry(root, width=10)
l3 = Label(root, text="Source Image:")
l3.place(relx=0.6, rely=0.1, anchor='ne')
num_label = Label(root, text="Number:")
num_label.place(relx=0.14, rely=0.5, anchor='ne')
submit = Button(root, text='Generate', padx=10, pady=6, command=lambda: generate(cam))
ans = Label(root, text='', font=('Helvetica', 28))
ans.place(relx=0.2, rely=0.5, anchor='ne')
hash_label = Label(root, text='Hash seed:')
hashing = Label(root, text='')
hash_label.place(relx=0.14, rely=0.4, anchor='ne')
hashing.place(relx=0.5, rely=0.4, anchor='ne')
l1.place(relx=0.1, rely=0.1, anchor='ne')
l2.place(relx=0.1, rely=0.2, anchor='ne')
e1.place(relx=0.3, rely=0.1, anchor='ne')
e2.place(relx=0.3, rely=0.2, anchor='ne')

submit.place(relx=0.3, rely=0.3, anchor='ne')

root.mainloop()
