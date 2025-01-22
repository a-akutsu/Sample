color = "赤青黄緑紫"
color_list = list(color)
find = ""
for str in color_list:
    if str == "赤青黄緑紫":
        find = "5色あります"
        break
    if str == "紫":
        find = "紫色あります"
    if str == "赤":
        find = "赤色あります"
print(find)
