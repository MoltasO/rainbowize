from . import data
fore = data.fore_color
back = data.back_color
style = data.set_style
bitc = data.bit_etc

class Styling():
    FBlack = fore("black")
    FRed = fore("red")
    FGreen = fore("green")
    FYellow = fore("yellow")
    FBlue = fore("blue")
    FMagenta = fore("magenta")
    FCyan = fore("cyan")
    FWhite = fore("white")
    FGray = fore("gray")
    FBrightRed = fore("bright red")
    FBrightGreen = fore("bright green")
    FBrightYellow = fore("bright yellow")
    FBrightBlue = fore("bright blue")
    FBrightMagenta = fore("bright magenta")
    FBrightCyan = fore("bright cyan")
    FBrightWhite = fore("bright white")

    BBlack = back("black")
    BRed = back("red")
    BGreen = back("green")
    BYellow = back("yellow")
    BBlue = back("blue")
    BMagenta = back("magenta")
    BCyan = back("cyan")
    BWhite = back("white")
    BGray = back("gray")
    BBrightRed = back("bright red")
    BBrightGreen = back("bright green")
    BBrightYellow = back("bright yellow")
    BBrightBlue = back("bright blue")
    BBrightMagenta = back("bright magenta")
    BBrightCyan = back("bright cyan")
    BBrightWhite = back("bright white")

    Reset = style("reset")
    Invert = style("invert")
    Italic = style("italic")
    Bold = style("bold")
    Dim =  style("dim")
    NormalIntensity =  style("normal intensity")
    RemoveFormat = style("remove format")
    Underline = style("underline")
    DoubleUnderline = style("double underline")
    RemoveUnderline = style("remove underline")
    Blinking = style("blinking")
    StopBlinking = "stop blinking"
    Strike = style("strike")
    RemoveStrike = style("remove strike")
    BDeafult = bitc["default_back"]
    FDeafult = bitc["default_fore"]

    def Brgb(_, red: int, green: int, blue: int):
        return (f"\033[48;2;{red};{green};{blue}m")
    
    def Frgb(_, red: int, green: int, blue: int):
        return (f"\033[38;2;{red};{green};{blue}m")

