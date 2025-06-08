from change_contact import on_change
from pynput import keyboard
from const import isEditing


def lisener():
    change = on_change()
    controller = keyboard.Controller()

    def delete():
        controller.press(keyboard.Key.backspace)
        controller.release(keyboard.Key.backspace)

    def on_key_down(key):
        global isEditing
        if not hasattr(key, "char"):
            return
        if not isEditing and key.char == "c":
            delete()
            isEditing = True
            return
        if isEditing:
            return
        delete()

    def on_release(key):
        global isEditing
        if isEditing and key == keyboard.Key.esc:
            isEditing = False
            return
        if isEditing:
            return
        if key == keyboard.Key.esc:
            return False
        if not hasattr(key, "char"):
            return
        match key.char:
            case "o":
                change("o")
            case "q":
                return False
            case "n" | "d":
                change("n")
            case "p" | "a":
                change("p")

    # listener = keyboard.Listener(on_press=on_key_down, on_release=on_release)
    # listener.start()
    with keyboard.Listener(on_press=on_key_down, on_release=on_release) as listener:
        listener.join()
