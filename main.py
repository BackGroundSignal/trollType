import keyboard

characters = ["Q", "W", "乇", "尺", "ｲ", "ﾘ", "U", "ﾉ", "O", "ｱ", "ﾑ", "丂",
              "D", "ｷ", "G", "ん", "ﾌ", "ズ", "ﾚ", "乙", "ﾒ", "C", "√", "乃", "刀", "ﾶ"]
while True:
    if keyboard.is_pressed("q") or keyboard.is_pressed("Q"):
        keyboard.press("backspace")
        keyboard.write(characters[0])
    if keyboard.is_pressed("w") or keyboard.is_pressed("W"):
        keyboard.press("backspace")
        keyboard.write(characters[1])
    if keyboard.is_pressed("e") or keyboard.is_pressed("E"):
        keyboard.press("backspace")
        keyboard.write(characters[2])
    if keyboard.is_pressed("r") or keyboard.is_pressed("R"):
        keyboard.press("backspace")
        keyboard.write(characters[3])
    if keyboard.is_pressed("t") or keyboard.is_pressed("T"):
        keyboard.press("backspace")
        keyboard.write(characters[4])
    if keyboard.is_pressed("y") or keyboard.is_pressed("Y"):
        keyboard.press("backspace")
        keyboard.write(characters[5])
    if keyboard.is_pressed("u") or keyboard.is_pressed("U"):
        keyboard.press("backspace")
        keyboard.write(characters[6])
    if keyboard.is_pressed("i") or keyboard.is_pressed("I"):
        keyboard.press("backspace")
        keyboard.write(characters[7])
    if keyboard.is_pressed("o") or keyboard.is_pressed("O"):
        keyboard.press("backspace")
        keyboard.write(characters[8])
    if keyboard.is_pressed("p") or keyboard.is_pressed("P"):
        keyboard.press("backspace")
        keyboard.write(characters[9])