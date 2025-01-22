import traceback

def divide_same(a, b):
    try:
        print(a / b)
    except (ZeroDivisionError, TypeError) as e:
        t = traceback.format_exc()
        print("例外エラー：" + t)

divide_same(1, 0)
divide_same('a', 'b')
