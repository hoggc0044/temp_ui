from tkinter import *
from functools import partial  # This will prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all the buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "13", "bold")
        button_fg = "#FFFFFF"

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=10, pady=10)
        self.button_frame.grid(row=0)

        self.to_help_button = Button(self.button_frame,
                                     text="Help / Info",
                                     bg="#CC6600",
                                     fg=button_fg,
                                     font=button_font, width=12,
                                     command=self.to_help)
        self.to_help_button.grid(row=1, column=0, padx=5, pady=5)

    def to_help(self):
        DisplayHelp(self)


class DisplayHelp:

    def __init__(self, partner):
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at the top, that will close the help button and realase it
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help, partner))

        self.help_frame = Frame(self.help_box, width=300, height=200,
                                bg=background)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame, bg=background,
                                        text="Help / Information",
                                        font=("Arial", "14", "bold"))
        self.help_heading_label.grid(row=0)

        help_text = "To use this programme, enter the temperature you wish to convert, " \
                    "then choose the thingy you wanna convert to - Celsius or Fahrenheit, \n\n" \
                    "Please note that -273 degrees C (-495 F) is the coldest you can go. " \
                    "If you attempt to go colder, the system will output an error message " \
                    "and the calculation will not work. You can view your calculation history " \
                    "by clicking on the 'History / Export' button. You can also export your " \
                    "history to a text file with this button. Please notify me if you " \
                    "encounter any drugs, as buuUugs are expected. You can also call tech support."
        self.help_text_label = Label(self.help_frame, bg=background,
                                     text=help_text, wrap=360,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                     font=("Arial", "12", "bold"),
                                     text="DISMISS", bg="#CC6600",
                                     fg="#FFFFFF",
                                     command=partial(self.close_help,
                                                     partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

    def close_help(self, partner):
        # Put help button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.help_box.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()
