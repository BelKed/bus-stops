import tkinter

pl = tkinter.Canvas(bg='blue', width=800, height=100)
pl.pack()

su = open('zastavky.txt', 'r')
veta = su.readline().strip() + ' '

print(veta)

ve = 0
x, y = 400, 50


def rotuj():
    global ve, veta

    pl.delete(ve)
    ve = pl.create_text(x, y, text=veta, fill='yellow', font='Arial 30')

    p = veta[0]
    veta = veta[1:]
    veta = veta + p


def citaj(event):
    global veta
    veta = su.readline().strip() + ' '


pl.bind_all('<Key>', citaj)

while True:
    rotuj()
    pl.after(200)
    pl.update()