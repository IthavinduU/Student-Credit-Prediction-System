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

total = 0


#list of reults
list_progress = []
list_trailer = []
list_retriever = []
list_excluded = []

#List of results after removing brakets
new_list_progress = []
new_list_trailer = []
new_list_retriever = []
new_list_excluded = []


#opening the file
text_file = open('text_file.txt','a')  
text_list = []

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
        list_progress.append(str(cr_pass))
        list_progress.append(str(cr_defer))
        list_progress.append(str(cr_fail))

        new_list_progress.append(list_progress)

        list_progress = []

                    
    elif cr_pass == 100 :
        print("\nProgress (module trailer)\n")
        trailer+=1
        list_trailer.append(str(cr_pass))
        list_trailer.append(str(cr_defer))
        list_trailer.append(str(cr_fail))

        new_list_trailer.append(list_trailer)

        list_trailer = []


    elif (cr_pass < 100) and (cr_fail < 80):
        print("\nDo not progress – module retriever\n")
        retriever+=1
        list_retriever.append(str(cr_pass))
        list_retriever.append(str(cr_defer))
        list_retriever.append(str(cr_fail))

        new_list_retriever.append(list_retriever)

        list_retriever = []

                    
    elif cr_fail >= 80 :
        print("\nExclude\n")
        excluded+=1
        list_excluded.append(str(cr_pass))
        list_excluded.append(str(cr_defer))
        list_excluded.append(str(cr_fail))

        new_list_excluded.append(list_excluded)

        list_excluded = []

        total = total + 1

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

#List   
        for i in range(total):
            if len(new_list_progress) > i :
                print("progress :" , ",".join(new_list_progress[i]))

            if len(new_list_trailer) > i :
                print("Progress (module trailer) :" , ",".join(new_list_trailer[i]))

            if len(new_list_retriever) > i :
                print("module retriever :" , ",".join(new_list_retriever[i]))

            if len(new_list_excluded) > i :
                print("excluded :" , ",".join(new_list_excluded[i]))



#Text file

        for x in range(len(new_list_progress)):
            text_list.append(("progress:-"+str(new_list_progress[x])))

        for x in range(len(new_list_trailer)):
            text_list.append(("Trailer:-"+str(new_list_trailer[x])))

        for x in range(len(new_list_retriever)):
            text_list.append(("Retriever:-"+str(new_list_retriever[x])))

        for x in range(len(new_list_excluded)):
            text_list.append(("Excluded:-"+str(new_list_excluded[x])))

        for i in text_list:
            text_file.write(i+'\n')   
        text_file.flush()   
        text_file.close()   

        break 

    else:
        print("Invalid option\n")
        
        break
print("________________________________________________________")
print()
print()
print("Coded by: T.T.H.Liyanage Student ID: 20211175")
