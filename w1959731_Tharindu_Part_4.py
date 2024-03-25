# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1959731

# ----- Define variables ----- #
p_count=0  # to count progress
t_count=0  # to count module trailer
r_count=0  # to count module retriever
e_count=0  # to count exclude
progress_list = []   # ------------- 
trailer_list = []    # ------------- Creating lists to append user input marks
retriever_list = []  # -------------
exclude_list = []    # -------------
st_id=0    # to get student id from the user
result = {} # creating dictionary 

vol = [0, 20, 40, 60, 80, 100, 120]  # Set range for marks

#
def main():
    
# ----- Main Variables ----- #
    pass_c=0    # to get pass credit
    defer_c=0   # to get defer credit
    fail_c=0    # to get fail credit
    total=0     # to count total of inputs
    again=0     # to get user input for whether want to continue or not
    
# ----- Count Variables ----- #
    global p_count
    global t_count
    global r_count
    global e_count
    

    print("|======== University predict progression system ========|")
    print()
    st_id=str(input("Enter your student ID : "))
    while True:
        try:
            pass_c=int(input("Please enter your credits at pass : ")) # Get input for pass credits
            while pass_c not in vol: # check if it is within the range or not
                print("Out of range")
                pass_c=int(input("Please enter your credits at pass : ")) # Ask user to input again if it is invalid input
            total+=pass_c
            defer_c=int(input("Please enter your credits at defer : ")) # Get input for defer credits
            while defer_c not in vol: # check if it is within the range or not
                print("Out of range")
                defer_c=int(input("Please enter your credits at defer : ")) # Ask user to input again if it is invalid input
            total+=defer_c
            fail_c=int(input("Please enter your credits at fail : ")) # Get input for fail credits
            while fail_c not in vol: # check if it is within the range or not
                print("Out of range")
                fail_c=int(input("Please enter your credits at fail : ")) # Ask user to input again if it is invalid input
            total+=fail_c
        except ValueError: 
            print("Integer required") # if user input invalid data type print what data type is need 
            continue
        else:
            break
        

# ----- check and count the result ----- #

    if total!=120:                      # check the total of scores
        print("Total incorrect")      
    elif pass_c==120:
        print("Progress")
        progress_list.append(pass_c)    # append each score to the list
        progress_list.append(defer_c)
        progress_list.append(fail_c)
        result[st_id]=progress_list     # append list to the dictionary
        
    elif pass_c>=100 and (defer_c==20 or fail_c==20):
        print("Progress(module trailer)")
        trailer_list.append(pass_c)     # append each score to the list
        trailer_list.append(defer_c)
        trailer_list.append(fail_c)
        result[st_id]=trailer_list  # append list to the dictionary
        
    elif fail_c>=80:
        print("Exclude")
        exclude_list.append(pass_c) # append each score to the list
        exclude_list.append(defer_c)
        exclude_list.append(fail_c)
        result[st_id]=exclude_list  # append list to the dictionary
        
    elif pass_c<=80 and(defer_c>=20 or fail_c>=20):
        print("Do not Progress - module retriever")
        retriever_list.append(pass_c)   # append each score to the list
        retriever_list.append(defer_c)
        retriever_list.append(fail_c)
        result[st_id]=retriever_list    # append list to the dictionary
               
# ----- check if user want to continue or not  ----- #   
    while True:
        again=input("""\nWould you like to enter another set of data?
        \nEnter 'y' for yes or 'q' to quit and view results : """)  # Ask user want to continue or not
        if again=='y' or again=='Y':
            print()
            main()
        elif again=='q' or again=='Q':
            print(result)       # Print the dictionary
            exit()
            break

main()
