from tkinter import *
from functools import partial  # This will prevent unwanted windows


class Converter:

    def __init__(self):
        # common format for all the buttons
        # Arial size 14 bold, with white text
        button_font = ("Arial", "13", "bold")
        button_fg = "#FFFFFF"

        # Five item list
        # self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°',
        #                          '30 F° is -1 C°', '0 C° is 86 F°',
        #                          '40 F° is -4 C°']

        # Six item list
        self.all_calculations = ['0 F° is -18 C°', '0 C° is 32 F°',
                                 '30 F° is -1 C°', '0 C° is 86 F°',
                                 '40 F° is -4 C°', '100 C° is 212 C°']

        # Set up GUI Frame
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.button_frame = Frame(padx=10, pady=10)
        self.button_frame.grid(row=0)

        self.to_history_button = Button(self.button_frame,
                                        text="history / Info",
                                        bg="#006deb",
                                        fg=button_fg,
                                        font=button_font, width=12,
                                        command=self.to_history)
        self.to_history_button.grid(row=1, column=0, padx=5, pady=5)

    #     ***** Remove when integrating!! ****

    def to_history(self):
        HistoryExport(self)


class HistoryExport:

    def __init__(self, partner):
        background = "#ffffff"
        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)

        # If users press cross at the top, that will close the history button and release it
        self.history_box.protocol('WM_DELETE_WINDOW',
                                  partial(self.close_history, partner))

        self.history_frame = Frame(self.history_box, width=300, height=200,
                                bg=background)
        self.history_frame.grid()

        self.history_heading_label = Label(self.history_frame, bg=background,
                                        text="history / Information",
                                        font=("Arial", "14", "bold"))
        self.history_heading_label.grid(row=0)

        history_text = "Below are your recent calculations - " \
                       "showing 3 / 3 calculations.  " \
                       "All calculations are shown to the nearest degree."
        self.text_instructions_label = Label(self.history_frame,
                                        text=history_text, wraplength=300,
                                        justify="left",
                                        padx=10, pady=10)
        self.text_instructions_label.grid(row=1, padx=10)

        self.all_cacls_label = Label(self.history_frame,
                                     text="calculations go here",
                                     justify="left", width=40,
                                     fg="#FFFFFF",
                                     padx=10, pady=10, bg="#006deb",
                                     font=("Arial", "12", "bold"))
        self.all_cacls_label.grid(row=2)

        # instructions for saving files
        save_text = "Either choose a custom file name and push " \
                    "<Export> or simply push <exploit> to save your " \
                    "calculations in a text file. If the " \
                    "filename already exists, it will be overwritten!"
        self.save_instructions_label = Label(self.history_frame,
                                             text=save_text,
                                             wraplength=300,
                                             justify="left", width=40,
                                             padx=10, pady=10)
        self.save_instructions_label.grid(row=3)

        # Filename entry widget, white background to start
        self.filename_entry = Entry(self.history_frame,
                                    font=("Arial", "14"),
                                    bg="#ffffff", width=25)
        self.filename_entry.grid(row=4, padx=10, pady=10)

        self.filename_error_label = Label(self.history_frame,
                                          text="FILENAME ERROR",
                                          fg="#9C0000",
                                          font=("Arial", "14", "bold"))
        self.filename_error_label.grid(row=5)

        self.button_frame = Frame(self.history_frame)
        self.button_frame.grid(row=6)

        self.export_button = Button(self.button_frame,
                                    font=("Arial", "12", "bold",),
                                    text="Export", bg="#004C99",
                                    fg="#FFFFFF", width=12)
        self.export_button.grid(row=0, column=0, padx=10, pady=10)

        self.dismiss_button = Button(self.button_frame,
                                     font=("Arial", "12", "bold"),
                                     text="DISMISS", bg="#666666",
                                     fg="#FFFFFF", width=12,
                                     command=partial(self.close_history,
                                                     partner))
        self.dismiss_button.grid(row=0, column=1, padx=10, pady=10)

    def close_history(self, partner):
        # Put help button back to normal...
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()

# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    Converter()
    root.mainloop()