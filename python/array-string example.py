
data = [ ["Title 1", "Message 1"], ["Title 2", "Message 2"] ]

def func(array = None):
    data = ""
    if array:
        for x in array:
            newdata = f"""
> {x[0]}
{x[1]}\n""" 
            data += newdata
        return data
    else:
        return "error"
    

print( func(data) )
