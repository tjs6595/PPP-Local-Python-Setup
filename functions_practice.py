def hello():
    print("Hello User!")


def pack(item1, item2, item3):
    return [item1, item2, item3]


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is EMPTY!")
    else:
        for i in range(len(lunch_list)):
            if i == 0:
                print("First I Eat " + lunch_list[0])
            else:
                print("Then I Eat " + lunch_list[i])


hello()
pack("sandwich", "apple", "dessert")
eat_lunch(["sandwich", "apple", "dessert"])