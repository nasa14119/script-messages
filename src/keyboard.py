from src.change_contact import on_change
from pynput import keyboard
from src.const import isEditing
from src.messages import messages

controller = keyboard.Controller()


def lisener():
    global controller
    change = on_change()

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
            case "s":
                messages.send()

    with keyboard.Listener(on_press=on_key_down, on_release=on_release) as listener:
        listener.join()
