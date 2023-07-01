import tkinter

window=tkinter.Tk()
result_label =tkinter.Label()
window.title("Python tkinter")
window.minsize(width=300,height=150)

def bmi_calculator(bmi):
    if(bmi<=16):
        result_label.config(text="Severe thinnes")
    elif(bmi>16and bmi<=17):
        result_label.config(text="Moderate thinnes")
    elif (bmi > 17 and bmi <= 18.5):
        result_label.config(text="Mild thinnes")
    elif (bmi > 18.5 and bmi <= 25):
        result_label.config(text="Normal")
    elif (bmi > 25 and bmi <= 30):
        result_label.config(text="overweight")
    elif (bmi > 30 and bmi <= 35):
        result_label.config(text="obese 1")
    elif (bmi > 35 and bmi <= 40):
        result_label.config(text="obese 2")
    elif (bmi > 40):
        result_label.config(text="obese 3")


def calculator():
    weight=Enter_your_weight_entry.get()
    height=Enter_your_height_entry.get()

    if weight =="" or height=="":
        result_label.config(text="Enter both weight and height")
    else:
        try:
            bmi = float(weight) / float(height) / 100 ** 2
            bmi_calculator(bmi)
        except:
            result_label.config(text="Enter a valid number")


Enter_your_weight_label = tkinter.Label(
    text="Enter your weight (kg)"
)
Enter_your_weight_entry=tkinter.Entry(
    width=30
)
Enter_your_height_label = tkinter.Label(
    text="Enter your height (cm)"
)
Enter_your_height_entry=tkinter.Entry(
    width=30
)
finish_button=tkinter.Button(
    text="calculate",
    command=calculator()
)

Enter_your_weight_label.pack()
Enter_your_weight_entry.pack()
Enter_your_height_label.pack()
Enter_your_height_entry.pack()
finish_button.pack()
result_label.pack()
tkinter.mainloop()

