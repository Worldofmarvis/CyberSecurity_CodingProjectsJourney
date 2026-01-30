def hex_to_bin(hex_string):

    hex_string = hex_string.strip().replace("0x", "").upper()

    binary_string = ""
    for digit in hex_string:
        binary_string += format(int(digit, 16), "04b") + " "
    
    return binary_string.strip()

hex_value = input("Enter a hexadecimal value: ")
binary_value = hex_to_bin(hex_value)

print("Hexadecimal:", hex_value)
print("Binary:", binary_value)