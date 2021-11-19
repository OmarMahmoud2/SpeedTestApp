from tkinter import *
from PIL import Image
from tkinter import messagebox



with open('txt.txt', 'r') as file:
    data = file.readlines()
    lines = ''
    for line in data[:5]:
        lines += line
seconds = 61
def start():

    top = Toplevel()
    top.title('Testing')
    top.minsize(300, 400)
    top.config(padx=20, pady=20)
    var = StringVar()
    # messagebox.showinfo('Notice', 'I have intentionally hidden the time for you \n to focus on typing. \n Good Luck ')
    text = Label(top, padx=20, pady=20, bd=5, height=12, font=('times', 18, 'bold'), justify=LEFT, anchor='w',
                 textvariable=var)
    text.grid(column=1, row=1)
    var.set(lines)
    words = Text(top, width=50, height=6, spacing3=8, bd=2, font=('times', 18, 'bold'), relief=RAISED, pady=10)
    words.grid(column=1, row=2)
    def grap():
        answer = words.get('1.0', END)
        answer = answer.lower()
        messagebox.showinfo('Time Over', 'One minute has elapsed')
        question = lines.lower().split(' ')
        answer = answer.split(' ')
        counter= 0
        for word in answer:
            if word in question:
                counter += 1
        messagebox.showinfo('Results', f"You're results are {counter} word per minute.")
        top.destroy()
    def test():
        minute = Label(top, text= f'Test Started \n GO', font=('times', 35, 'bold'), fg='red')
        minute.grid(column=1,row=0)
        btn3.config(state='disabled')
        def timeer():
            global seconds
            seconds -= 1
            minute.config(text=seconds)
            minute.after(1000, timeer)
        timeer()
        top.after(60000, grap)
    btn3 = Button(top, text="Start the Test", command=test, relief=RAISED, padx=20, pady=20)
    btn3.grid(column=1, row=4, padx=20, pady=10)

root = Tk()
root.title('Typing Speed Test')
root.minsize(600,300)
root.config(padx=40, pady=40)

label = Label(root, text='Welcome to the Typing Speed Test App', font=('Georgia', 20, 'italic'))
label.grid(column=1, row=0)

canvas = Canvas(root, height=300, width= 350, background='teal')
canvas.grid(column=1, row=1)
img = Image.open('logo.png').convert('RGBA').resize((300,220))
img.save('logo1.png', quality=95)
logo = PhotoImage(file='logo1.png')
image= canvas.create_image(175, 175, image=logo)

label1 = Label(root, text="Let's see how fast of a typist \n Are you?", font=('Georgia', 20, 'italic'))
label1.grid(column=1, row=2)

copyr = Label(root, text="@2021 Omar Mahmoud", font=('Georgia', 10, 'italic'))
copyr.grid(column=1, row=5, pady=50)

btn1 = Button(root, text="Take the Test", command=start, relief=RAISED, padx=20, pady=20)
btn1.grid(column=2, row=4, padx=20, pady=20)

btn2 = Button(root, text="Exit the App", command=root.destroy, relief=RAISED, padx=20, pady=20)
btn2.grid(column=0, row=4, padx=20, pady=20)


root.mainloop()

#2021 @Omar Mahmoud