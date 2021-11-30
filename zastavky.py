import tkinter

canvas = tkinter.Canvas(bg="blue", width=800, height=100)
canvas.pack()

f = open("zastavky.txt", "r", encoding="Windows-1250")
text = f.readline().strip() + " "

print(text)

text_element = 0
x, y = 400, 50


def draw():
    global text, text_element

    canvas.delete(text_element)
    text_element = canvas.create_text(x, y, text=text, fill="yellow", font="Arial 30")
    p = text[0]
    text = text[1:]
    text = text + p


def keypress(_):
    global text
    text = f.readline().strip() + " "


canvas.bind_all("<Key>", keypress)

while True:
    draw()
    canvas.after(200)
    canvas.update()