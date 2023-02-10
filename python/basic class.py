str_1 = "string 1!!!"



class example:
  def __init__(self, data_1 = "No data provided", data_2 = "No data provided"):


    self._1 = data_1
    self._2 = data_2


  def data(self):
    return f"- {self._1}\n- {self._2}" # line 9/10
  
  def view(self):
    class class_example(object):
      data_1 = self._1 # line 9
      data_2 = self._2 # line 10
    return class_example





main_example = example(str_1) # str / line 1


print(main_example.data()) # func / line 13
#Expected response
"""
- string 1!!!
- No data provided
"""


class_example = main_example.view() # func / line 16

print("+ "+class_example.data_1)
print("+ "+class_example.data_2)
# Expected response 
"""
+ string 1!!!
+ No data provided
"""
