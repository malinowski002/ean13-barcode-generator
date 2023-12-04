import turtle

def draw_filled_rectangle(width):
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(140)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(4)


def draw_binary_barcode(binary_string):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(-200, 70)

    for digit in binary_string:
        if digit == '0':
            turtle.color("white")
            draw_filled_rectangle(4)
        elif digit == '1':
            turtle.color("black")
            draw_filled_rectangle(4)

    turtle.done()


def control_digit(code_12):
    checksum = 0
    counter = 0
    code_int = int(code_12)
    while code_int > 0:
        last_digit = int(code_int % 10)
        if counter % 2 == 0:
            checksum += last_digit * 3
        else:
            checksum += last_digit
        counter += 1
        code_int /= 10
    return str((10 - (checksum % 10)) % 10)


def encode_to_ean13(int_number):
    number = str(int_number)
    o = ["0001101", "0011001", "0010011", "0111101", "0100011", "0110001", "0101111", "0111011", "0110111", "0001011"]
    e = ["0100111", "0110011", "0011011", "0100001", "0011101", "0111001", "0000101", "0010001", "0001001", "0010111"]
    r = ["1110010", "1100110", "1101100", "1000010", "1011100", "1001110", "1010000", "1000100", "1001000", "1110100"]
    parity = [[1, 1, 1, 1, 1, 1], [1, 1, 0, 1, 0, 0], [1, 1, 0, 0, 1, 0], [1, 1, 0, 0, 0, 1],
              [1, 0, 1, 1, 0, 0], [1, 0, 0, 1, 1, 0], [1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 1, 0],
              [1, 0, 1, 0, 0, 1], [1, 0, 0, 1, 0, 1]]

    # first delimiter
    final_code = "101"
    first = int(number[0])

    # left
    for i in range(1, 7):
        if parity[first][i - 1] == 1:
            final_code += o[int(number[i])]
        else:
            final_code += e[int(number[i])]

    # middle delimiter
    final_code += "01010"

    # right
    for i in range(8, 14):
        final_code += r[int(number[i - 1])]

    # last delimiter
    final_code += "101"

    return final_code


code = input("Provide the 12-digit EAN number for which you want to generate a barcode: ")
if len(code) != 12 or not code.isnumeric():
    print("The code should consist of 12 digits.")
else:
    code += control_digit(code)
    binary_code = encode_to_ean13(code)
    # print(encode_to_ean13("0987654321562"))
    turtle.setup(600, 500)
    scrn = turtle.Screen()
    scrn.tracer(0)
    draw_binary_barcode(binary_code)
    scrn.update()

#     2o      3o      4e      5o      1e      2e           3e        4r      5r      1r      2r      3r
# 101 0010011 0111101 0011101 0110001 0110011 0011011 0101       0100001 0 1011100 1001110 1100110 1101100 1000010 101 1234512345123
# 101 0010011 0111101 0011101 0110001 0110011 0011011 0101       0100001 0 1011100 1001110 1100110 1101100 1000010 101