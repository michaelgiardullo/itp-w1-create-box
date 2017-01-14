"""This is the entry point of the program."""


def create_box(height,width,character):
    height_count = 0
    boxstring=""
    if height==0 and width==0:
            return ("invalid measurements")
    while True:
        if height_count < height:
            for w in range(width):
                boxstring = boxstring + character
            height_count = height_count + 1
            if height_count <= height:
                boxstring = boxstring + '\n'
        else:
            break
    return boxstring

if __name__ == '__main__':
    create_box(3, 4, '*')
