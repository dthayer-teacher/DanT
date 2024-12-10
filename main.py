import random

def id():
    statement = " "
    print(statement.isspace())

def reader():
    win = 0
    sb_win = [1,"GB",2,"GB",3,"NYJ",4,"KC",5,"BC",6,"DC",7,"MD",8,"MD",9,"PS",10,"PS"]
    team = input("Super bowl winner: ")
    for champ in sb_win:
        if champ == team:
            win+=1
    print(team,"won",win,"Super Bowls.")


def sentence_builder():
    sentence = input("Type a sentence in here: ")
    count = 0
    first =[]
    space = False
    for letter in sentence:
        if letter=='.':
            space =True
            first.append(letter)
        elif letter==',':
            space = True
            first.append(letter)

        elif space ==True:
            if letter.isspace()==False:
                first.append(letter)
                space = False

        else:
            first.append(letter)
    print(first)
    cap = True
    for let in first:
        if let ==".":
            print(let,end="  ")
            cap=True
        elif let==',':
            print(let, end=" ")
        elif cap==True:
            print(let.upper(),end="")
            cap= False
        else:
            print(let.lower(),end="")

def sentence():
    count=0
    letterCount = 0
    sentence = input("Enter a sentence: ")
    for letter in sentence:
        if letter != " ":
            letterCount+=1
        if letter=="A" or letter=='a':
            count +=1
    size = len(sentence)
    print(letterCount)
    print("The letter A appears",count,"times.")
    print("There are",size,"characters in the sentence, but only",letterCount,"letters.")
    x = int(input("What number of letter you want to see? "))
    if sentence[x-1] == " ":
        print("This is a space")
    else:

        print(sentence[x-1])

def log_maker():
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    year_of_birth = input("Year of birth: ")

    first = first_name[0:2]
    login_name = (year_of_birth+"_"+first+"."+last_name)
    login_name=login_name.lower()
    print(login_name)
    # middle 2 year, first of fN and last 3 of lN
    password = (year_of_birth[1:3]+first_name[0]+last_name[-3:])
    last = password[5].upper()
    password = password[0:5].lower()
    symbol =['#','%','$','*','+']
    symbol = random.choice(symbol)
    print(password+last+symbol)


def main():
    #log_maker()
    #sentence_builder()
    reader()
main()