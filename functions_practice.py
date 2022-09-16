def hello():
    print("Hello User!")


def pack(item1, item2, item3):
    packed_list = [item1, item2, item3]
    return packed_list


def eat_lunch(lunch_list):
    if len(lunch_list) == 0:
        print("My lunchbox is EMPTY!")
    else:
        for i in range(len(lunch_list)):
            if i == 0:
                print("First I eat a " + lunch_list[0] + ".")
            else:
                print("Then I eat a " + lunch_list[i] + ".")


hello()
basket = pack("sandwich", "apple", "dessert")
print(basket)
eat_lunch(basket)


# Printed output of hello()
# Hello User!

# Printed output of pack()
# ['sandwich', 'apple', 'dessert']

# Printed output of eat_lunch()
# First I eat a sandwich.
# Then I eat a apple.
# Then I eat a dessert.