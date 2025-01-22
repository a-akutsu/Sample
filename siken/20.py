import traceback

a_file = open("test.txt", mode="w", encoding="utf-8")
try:
    s = a_file.read()
    a_file.close()
    print(s)
except Exception as e:
    t = traceback.format_exc()
    print("例外エラー：" + t)
