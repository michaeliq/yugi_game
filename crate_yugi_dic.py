

def checkLink():
    with open('cards_path.txt','r') as register:
        for link in register.read():
            print(link)

checkLink()
