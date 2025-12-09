def wrap(string, max_width):
    result = ""
    
    if (len(string) > 0) and (len(string) < 1000) and (max_width > 0) and (max_width < len(string)):
        for i in range(0, len(string), max_width):
            result += string[i:max_width+i] + "\n"
    
    return result.rstrip("\n") 
