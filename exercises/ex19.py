def conv_to_decimal (binary):
    reverse_binary=binary[::-1]
    decimal =0
    for i in range (len(reverse_binary)):
        two_powered = (2**i)*int(reverse_binary[i])
        decimal=decimal +int(two_powered)
    return decimal
binary="1101"
decimal = conv_to_decimal(binary)
print(f"{binary} to decimal is {decimal}")

