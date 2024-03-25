# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1959731
# Date: 2022/12/14


# ----- Define variables ----- #
p_count=0  # to count progress
t_count=0  # to count module trailer
r_count=0  # to count module retriever
e_count=0  # to count exclude
progress_list = []   # ------------- 
trailer_list = []    # ------------- Creating lists to append user input marks
retriever_list = []  # -------------
exclude_list = []    # -------------
f = open("Result.txt", "w") # to open text file to insert user inputs 

vol = [0, 20, 40, 60, 80, 100, 120]  # Set range for marks

def main():    
# ----- Variables ----- #
    pass_c=0    # to get pass credit
    defer_c=0   # to get defer credit
    fail_c=0    # to get fail credit
    total=0     # to count total of inputs
    again=0     # to get user input for whether want to continue or not
# ----- Count Variables and lists ----- #
    global p_count
    global t_count
    global r_count
    global e_count
    global progress_list 
    global trailer_list 
    global retriever_list 
    global exclude_list
    global f
    

    print("|======== University predict progression system ========|")
    print()
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
        p_count+=1                      # count the results
        progress_list.append(pass_c)    # append each score to the list
        progress_list.append(defer_c)
        progress_list.append(fail_c)
        
        f.write('Progress : ')          # Write all result and scores to text file
        f.write(str(pass_c))
        f.write(",")
        f.write(str(defer_c))
        f.write(",")
        f.write(str(fail_c))
    
    elif pass_c>=100 and (defer_c==20 or fail_c==20):  # check mark range if it is module trailer or not 
        print("Progress(module trailer)")
        t_count+=1
        trailer_list.append(pass_c)
        trailer_list.append(defer_c)
        trailer_list.append(fail_c)
        
        f.write('\nProgress(module trailer) : ')    # Write all result and scores to text file
        f.write(str(pass_c))
        f.write(",")
        f.write(str(defer_c))
        f.write(",")
        f.write(str(fail_c))
    elif fail_c>=80:                                # check mark range if it is Exclude or not
        print("Exclude")
        e_count+=1
        exclude_list.append(pass_c)
        exclude_list.append(defer_c)
        exclude_list.append(fail_c)
        
        f.write('\nExclude : ')                     # Write all result and scores to text file
        f.write(str(pass_c))
        f.write(",")
        f.write(str(defer_c))
        f.write(",")
        f.write(str(fail_c))
        
    elif pass_c<=80 and(defer_c>=20 or fail_c>=20):     # check mark range if it is Modeule retriever or not
        print("Do not Progress - module retriever")
        r_count+=1
        retriever_list.append(pass_c)
        retriever_list.append(defer_c)
        retriever_list.append(fail_c)
        
        f.write('\nDo not Progress module retriever : ')    # Write all result and scores to text file
        f.write(str(pass_c))
        f.write(",")
        f.write(str(defer_c))
        f.write(",")
        f.write(str(fail_c))
        

        
# ----- check if user want to continue or not  ----- #   
    while True:
        again=input("""\nWould you like to enter another set of data?
        \nEnter 'y' for yes or 'q' to quit and view results : """)      # Ask user want to continue or not
        if again=='y' or again=='Y':
            print()
            main()              # Run the programme again  
        elif again=='q' or again=='Q':
            
            print("---------------------------------------------------------------")
            print("Histogram")                          # Printing the hisogram
            print("Progress",p_count,":","*"*p_count)    # Print each results line by line         
            print("Trailer",t_count,":","*"*t_count)
            print("Retriever",r_count,":","*"*r_count)
            print("Excluded",e_count,":","*"*e_count)
            loop_total=(p_count+t_count+r_count+e_count) # Calculating total results
            print(loop_total,"outcomes in total") # Print total
            print("---------------------------------------------------------------")
            # Part 02 - Print all progress,trailer,retriever and exclude lists
            print("Progress :",progress_list)
            print("Progress ( Module Trailer ) :",trailer_list)
            print("Module  retriever :",retriever_list)
            print("Exclude :",exclude_list)
            f.close()
            print("---------------------------------------------------------------")
            # Part 03 - Print saved text file to python 
            f = open("Result.txt", "r")   # open text file which previoulsy saved
            print(f.read())               # read and print text file
            exit()                        # exiting the programme
            
main()










