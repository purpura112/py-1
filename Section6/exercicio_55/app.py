# a function that draws a staircase

def draw_staircase(n):
    if n < 10:
        n += 1
        print("#" * n)
        draw_staircase(n)
    else:
        return n
    
draw_staircase(1)