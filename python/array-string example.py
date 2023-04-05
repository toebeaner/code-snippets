array = [ ["Top Message 1", "Bottom Message 1"], ["Top Message 2", "Bottom Message 2"] ]

def func(array = [ "Top Message", "Bottom Message" ]):
    data = ""
    for string in array:
        data += f">> {string[0]}\n> {string[1]}\n" 
        return data

print(func(array))
