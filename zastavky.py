import tkinter

i = 1
characters = 20
text_element = text_pos = 0
x, y = characters * 10, 50

canvas = tkinter.Canvas(bg="#282c34", width=characters * 20, height=100)
canvas.pack()

f = open("zastavky.txt", "r", encoding="Windows-1250")
lines = f.readlines()
line = lines[0].strip() + " "

canvas.create_text(x, y, text="░" * characters, fill="#185566", font=("JetBrains Mono", 30))


def draw():
    global line, text_element, text_pos

    text = line[text_pos:text_pos + characters].ljust(characters)

    canvas.delete(text_element)
    text_element = canvas.create_text(x, y, text=text, fill="#32b1d3", font=("JetBrains Mono", 30))

    if text_pos == 0:
        canvas.update()
        canvas.after(300)

    text_pos += 1

    if text_pos > len(line):
        text_pos = 0


def keypress(_):
    global lines, line, i, text_pos

    line = lines[i].strip() + " "
    text_pos = 0

    if (line == lines[-1].strip() + " "):
        line += "| KONEČNÁ ZASTÁVKA "
    else:
        i += 1


canvas.bind_all("<Key>", keypress)

while True:
    draw()
    canvas.after(200)
    canvas.update()