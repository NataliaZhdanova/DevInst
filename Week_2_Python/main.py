tn_name = 0
tn_age = 0
init_tn_list = ['Masha', 'Sasha', 'John', 'Vlad']
final_list = list()
for x in init_tn_list :
    tn_name = input("What is your name? \n")
    if tn_name in init_tn_list :
        tn_age = int(input("How old are you? \n"))
        if tn_age < 16 :
            print("You are not permitted to watch the movie!\n")
        elif tn_age >=21 :
            print("You are not permitted to watch the movie!\n")
        else :
            print("You're allowed to watch the movie!\n")
            final_list.append(tn_name)
    else :
        print("You're not in the list!")
        break
print("The final list of teenagers:", final_list)
