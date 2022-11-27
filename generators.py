def binary_converter(num, base):
    oct =''
    binary = ''
    while True:
        oct += str(num % base)
        num = num // base
        if num == 0:
            break
    for i in range(len(oct), 0, -1):
        binary += oct[i - 1]
    return binary


while True:
    val =  input("Enter value  and base (separate with space): ")
    if val in ["Exit", "exit", "EXIT"]:
        break
    print(binary_converter(int(val.split()[0]), int(val.split()[1])))




