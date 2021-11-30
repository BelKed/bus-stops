import tkinter

canvas = tkinter.Canvas(bg="#282c34", width=800, height=100)
canvas.pack()

f = open("zastavky.txt", "r", encoding="Windows-1250")
lines = f.readlines()
text = lines[0].strip() + " "

i = 1
text_element = 0
x, y = 400, 50


def draw():
    global text, text_element

    canvas.delete(text_element)
    text_element = canvas.create_text(x, y, text=text, fill="#32b1d3", font=("JetBrains Mono", 30))
    p = text[0]
    text = text[1:]
    text = text + p


def keypress(_):
    global lines, text, i

    text = lines[i].strip() + " "

    if (text == lines[-1].strip() + " "):
        text += "| KONEČNÁ ZASTÁVKA "
    else:
        i += 1


canvas.bind_all("<Key>", keypress)

while True:
    draw()
    canvas.after(200)
    canvas.update()