#yo i made this  unique calculator
import tkinter as tk
root = tk.Tk()
root.title("Epic and Completely Unique Calculator")
root.geometry("350x500")
root.resizable(False,False)
display = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="ridge", justify="right")
display.pack(padx=10, pady=20, fill="x")
#all just root stuff ^


#define button press
def button_click(val):
    cur = display.get() #store the value in cur
    display.delete(0, tk.END) #clear current display
    display.insert(0, str(cur) + str(val)) #insert in the previous with the new one added

#clear display function
def clear_display():
    display.delete(0, tk.END)

#use try/except to check for errors and eval function to evaluate operation
def evaluate():
    try:
        result = eval(display.get())
        display.delete(0, tk.END) #clear current display
        display.insert(0, str(result)) #display result instead

    except Exception:
        display.delete(0, tk.END) #clear current display
        display.insert(0, "ERROR") #display error instead

#make the buttons
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', '=', '+')
]
for r, row in enumerate(buttons):
    frame = tk.Frame(root)
    frame.pack(expand = True, fill = "both")
    for c, char in enumerate(row):
        if char == '=':
            btn = tk.Button(frame, text=char, font=('Arial',18), bg="#C38EE6", fg="white", command=evaluate)
        else:
            btn = tk.Button(frame, text=char, font=('Arial',18), bg="#827C86", command=lambda ch=char:button_click(ch))
        btn.pack(side="left", expand=True, fill="both", padx=3, pady=3)
clear_button = tk.Button(root, text = "Clear", font=('Arial',18), bg="#EE7878", fg="white", command=clear_display)
clear_button.pack(expand=True, fill="both", padx=10, pady=10)

root.mainloop()


