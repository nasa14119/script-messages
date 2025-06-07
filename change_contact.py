import os
import platform
import subprocess
import webbrowser
from const import phones


def on_change():
    current_os = platform.system()

    def open_whatapp(phone):
        link = f"whatsapp://send?phone={phone}"
        try:
            if current_os == "Window":
                subprocess.run(["start", link], shell=True, check=True)
            if current_os == "Darwin":
                subprocess.run(["open", link], check=True)
        except:
            webbrowser.open_new(f"https://wa.me/{phone}")

    def update_index(prev, v, max=0):
        new_val = prev + v
        if new_val > max or new_val < 0:
            return prev
        return new_val

    global current_index
    current_index = 0

    def apply(opt):
        global current_index
        current_index = update_index(
            current_index, 1 if opt == "n" else -1, len(phones)
        )
        phone = phones[current_index]
        open_whatapp(phone)

    return apply
