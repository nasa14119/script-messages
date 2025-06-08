import os
import platform
import subprocess
import webbrowser
from src.const import phones
from src.const import current_index


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

    def apply(opt):
        global current_index
        if opt == "o":
            open_whatapp(phones[current_index.value])
            return
        new_value = 1 if opt == "n" else -1
        try:
            current_index.change_value(new_value)
            phone = phones[current_index.value]
            open_whatapp(phone)
        except:
            pass

    open_whatapp(phones[0])
    return apply
