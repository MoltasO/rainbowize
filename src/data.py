# https://en.wikipedia.org/wiki/ANSI_escape_code

four_bit_colors = {
    "black": "0",
    "red": "1",
    "green": "2",
    "yellow": "3",
    "blue": "4",
    "magenta": "5",
    "cyan": "6",
    "white": "7",
    "gray": "0;1",
    "bright red": "1;1",
    "bright green": "2;1",
    "bright yellow": "3;1",
    "bright blue": "4;1",
    "bright magenta": "5;1",
    "bright cyan": "6;1",
    "bright white": "7;1"
}

bit_styles = {
    "reset": "0",
    "invert": "7",
    "italic": "3",
    "bold": "1",
    "dim": "2",
    "remove format": "23",
    "normal intensity": "22",
    "underline": "4",
    "double underline": "21",
    "remove underline": "24",
    "blinking": "5",
    "stop blinking": "25",
    "strike": "9",
    "remove strike": "29"
}

bit_etc = {
    "default_back": "49",
    "default_fore": "39",
    "rgb_fore": "38;2",
    "rgb_back": "48;2"
}

def esc(code: str):
    return "\33[" + code + "m"

def reset():
    return esc(bit_styles["reset"])

def set_style(style: str):
    return esc(bit_styles[style.lower()])
        
def back_color(color: str):
    return esc("4" + four_bit_colors[color.lower()])
    
def fore_color(color: str):
    return esc("3" + four_bit_colors[color.lower()])
        
def back_rgb_color(red: int, green: int, blue: int):
    return esc(f"{bit_etc['rgb_back']};{red};{green};{blue}")
    
def fore_rgb_color(red: int, green: int, blue: int):
    return esc(f"{bit_etc['rgb_fore']};{red};{green};{blue}")


if __name__ == "__main__":
    import random
    string = ""
    for i in range(100):
        string += (fore_rgb_color(random.randint(0,255),random.randint(0,255),random.randint(0,255)) + "Hello! " + reset())
    print(string)
