COLOUR_AND_HEX = {"black": "#000000", "ghostwhite": "#f8f8ff", "gray": "#bebebe", "lawngreen": "#7cfc00",
                  "light": "	#eedd82", "linen": "#faf0e6", "medium": "#66cdaa", "mintcream": "#f5fffa",
                  "navyBlue": "#000080", "olivedrab": "#6b8e23"}
print(COLOUR_AND_HEX.keys())
colour = input("Hex for colour>>>")
while colour != "":
    if colour in COLOUR_AND_HEX:
        print(colour, "is", COLOUR_AND_HEX[colour])
    else:
        print("invalid colour option")
    colour = input("Hex for colour>>>")