def favorite_colors():
    print("Red, Green, Blue")
favorite_colors()

def favorite_colors_with_args(color1, color2, color3):
    say_colors = f"{color1}, {color2}, {color3}"
    return say_colors
print(favorite_colors_with_args("Black", "White", "Purple"))