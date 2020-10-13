import tkinter as tk
from tithiwa import Tithiwa


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_containers()
        self.create_widgets()

    def create_containers(self):
        # entry for number phone
        self.container1 = tk.Frame(self.master)
        self.container1["padx"] = 20
        self.container1["pady"] = 5
        self.container1.pack()

        # text area message
        self.container2 = tk.Frame(self.master)
        self.container2["pady"] = 10
        self.container2.pack()

        # buttons
        self.container3 = tk.Frame(self.master)
        self.container3["pady"] = 10
        self.container3.pack()  # mostrar na tela

    def create_widgets(self):
        self.font = ("Verdana", "10")
        self.lbl_number = tk.Label(self.container1,
                                   text="Give a number phone :")
        self.lbl_number["font"] = self.font
        self.lbl_number.pack(side="left")

        self.txt_area_number = tk.Entry(self.container1)
        self.txt_area_number.pack(side="left", fil="both")
        self.txt_area_number["font"] = self.font

        self.lbl_msg = tk.Label(self.container2,
                                text="Give a msg :",
                                width=10)
        self.lbl_msg["font"] = self.font
        self.lbl_msg.pack(side="top")

        self.txt_area_msg = tk.Text(self.container2, height=10, width=30)
        self.txt_area_msg.pack(side="top")
        self.txt_area_msg["font"] = self.font

        self.send_message_button = tk.Button(self.container3, width=12)
        self.send_message_button["text"] = "Send message"
        self.send_message_button["command"] = self.send_message
        self.send_message_button.pack(side="right")

        self.quit = tk.Button(self.container3,
                              text="Quit",
                              fg="red",
                              command=self.master.destroy,
                              width=12)
        self.quit.pack(side="bottom")

    def send_message(self):
        tithiwabot = Tithiwa()
        tithiwabot.session.generate_session()
        number = self.txt_area_number.get()
        msg = self.txt_area_msg.get()
        tithiwabot.chatroom.send_message_to_number(number, msg)
        self.clear()
        tithiwabot.quit()

    def clear(self):
        self.txt_area_number.delete(0, "end")
        self.txt_area_msg.delete(1.0, "end")


if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()
