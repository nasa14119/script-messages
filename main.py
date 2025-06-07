from pynput import keyboard
from change_contact import on_change

change = on_change()


def on_key_down(key):
    if not hasattr(key, "char"):
        return
    if key.char == "n" or key.char == "p":
        change(key.char)


listener = keyboard.Listener(on_release=on_key_down)
listener.start()
listener.join()
