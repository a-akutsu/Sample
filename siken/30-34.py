food_stuff = ["Banana", "Mango", "Fish", "Carrot", "cabbage"]

flag_found = False
for food in food_stuff:
    if food == "Mango":
        flag_found = True
        break

if flag_found:
    print("マンゴーが入っています。")
else:
    print("ありませんでした。")
