import traceback

try:
    for i in [-2, -1, 1, 1, 2]:
        print(1 / i, end=",")
except Exception as e:
    t = traceback.format_exc()
    print("\n例外エラー：" + t)
