# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: 20211175
# Date: 2022.04.08

#Creating Variables
cr_pass=0
cr_defer=0
cr_fail=0

progress=0
trailer=0
retriever=0
excluded=0

print("----PROGRESS PREDICTION SYSTEM BY UNIVERSITY OF WESTMINSTER----") #Suitable name for the program.
print()
while True:
    while True:
        try:
            cr_pass=int(input("Please enter your credits at pass : ")) #Validations
            if cr_pass>120 or cr_pass<0 or (cr_pass%20!=0):
                print ("Out of range\n")
                continue
        
            cr_defer=int(input("Please enter your credits at defer : "))
            if cr_defer>120 or cr_defer<0 or (cr_defer%20!=0):
                print ("Out of range\n")
                continue

            cr_fail=int(input("Please enter your credits at fail : "))
            if cr_fail>120 or cr_fail<0 or (cr_fail%20!=0):
                print ("Out of range\n")
                continue

            if cr_pass+cr_defer+cr_fail!=120:
                print("Total incorrect\n")
                continue
            break
        except ValueError:
            print("Integer Required\n")
            continue
#Defining outcomes
    if cr_pass == 120:
        print("\nProgress\n")
        progress+=1
                    
    elif cr_pass == 100 :
        print("\nProgress (module trailer)\n")
        trailer+=1

    elif (cr_pass < 100) and (cr_fail < 80):
        print("\nDo not progress – module retriever\n")
        retriever+=1
                    
    elif cr_fail >= 80 :
        print("\nExclude\n")
        excluded+=1
#Choosing option
    repeat=input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
    print()
    if repeat.lower()=="y":
        continue
    elif repeat.lower()=="q":
#Horizontal histogram
        total=progress+trailer+retriever+excluded
        print("________________________________________________________")
        print()
        print("Horizontal Histogram")
        print("Progress ",progress,"\t:","*"*progress)
        print("Trailer ",trailer,"\t:","*"*trailer)
        print("Retriever ",retriever,"\t:","*"*retriever)
        print("Excluded ",excluded,"\t:","*"*excluded)
        print()
        print(total," outcomes in total.")
        print("_________________________________________________________")
#Vertcal - Histogram
       
        print()
        print("Vertical Histogram")
        m = [progress, trailer, retriever, excluded]
        #sort - list
        m.sort()
        max_count = m[-1]

        print("Progress" , progress , "Trailer" , trailer ,"Retriever", retriever , "Excluded", excluded)
        for i in range(max_count):
             print("{}      {}      {}      {}".format(
                "    *  " if i <= progress-1 else "      ",
                 "   *  " if i <= trailer-1 else "      ",
                 "  *  " if i <= retriever-1 else "      ",
                "  *  " if i <= excluded-1 else "      "))
        print("________________________________________________________")
        print()
        print("Total attempts: ", progress + trailer + retriever + excluded)
        print("________________________________________________________")
        print()
        break
    else:
        print("Invalid option\n")
        
        break
print()
print("Coded by: T.T.H.Liyanage Student ID: 20211175")
