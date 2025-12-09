def print_formatted(number):
    if number >= 1 and number <= 100:
        
        width = len(bin(number)) - 2

        for i in range(1, number + 1):
            
            decn = str(i)
            octn = oct(i)[2:]
            hexn = hex(i)[2:].upper()
            binn = bin(i)[2:]
            
            print(f"{decn:>{width}} {octn:>{width}} {hexn:>{width}} {binn:>{width}}")
