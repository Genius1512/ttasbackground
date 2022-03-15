import tkinter as tk


hash = None
auth_key = None
id = None


def set_values(v1, v2, v3):
    global hash
    global auth_key
    global id

    hash = v1
    auth_key = v2
    id = v3


class Root(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Config Editor")
        self.geometry("500x500")
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # TODO: add labels
        self.hash_input = tk.Entry(
            self,
        )
        self.hash_input.pack()

        self.auth_key_input = tk.Entry(
            self,
        )
        self.auth_key_input.pack()

        self.id_input = tk.Entry(
            self,
        )
        self.id_input.pack()

        self.mainloop()

    def on_close(self):
        set_values(
            self.hash_input.get(),
            self.auth_key_input.get(),
            self.id_input.get()
        )

        self.destroy()


def get_config():
    root = Root()
    return hash, auth_key, id


if __name__ == "__main__":
    print(get_config())