#importing the required packages
import tkinter as tr
import time
window = tr.Tk()
window.title("DIGITAL CLOCK USING PYTHON")
def update_clock():
    #extracting the current time in hour,min and seconds
    hours = time.strftime("%I")
    minutes = time.strftime("%M")
    seconds = time.strftime("%S")
    am_or_pm = time.strftime("%p")
    time_text = hours + ":" + minutes + ":" + seconds + "" + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000,update_clock)

digital_clock_lbl  =  tr.Label(window, font="Helvetica 72 bold", text="00:00:00")
digital_clock_lbl.pack()

#calling function
update_clock()
#to run the tkinker window
window.mainloop()