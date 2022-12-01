




def important_tab(value = None):
    print("so much important information here")
   

def settings_tab(value = None):
    print("so many settings")

  





def main():
    while True:

        op = None

        class options():



            def important(self): # Important
                important_tab()
                

            def settings(self): # Settings
                settings_tab()
             
                
                
        def run_cmd(option):
            try:
                getattr( 
                    options(), 
                    option
                )()
            except:
                getattr(
                    options(),
                    'Please try again.'
                )()
        op = input("option - ")
        run_cmd(op)
       


main()
