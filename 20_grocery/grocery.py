def main():
    userList = grocery_list()
    orderedList = ordered_list(userList)
    print_item(orderedList)




def grocery_list():
    userList = []
    while True:
        try:
            userList.append(input().upper())

        except EOFError:
            break
    return userList

def ordered_list(grocery):
    sortedGrocery = sorted(grocery)
    orderedList =[]
    for item in grocery:
        index = grocery.index(item)
        numberedItem = str(index+1)+" "+ item
        orderedList.append(numberedItem)
    return orderedList

def print_item(grocery):
    for index in range(len(grocery)):
        print(grocery[index])

main()