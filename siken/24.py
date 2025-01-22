import traceback

def divide_else(a, b):
    try:
        print(a / b)
    except ZeroDivisionError as e:
        t = traceback.format_exc()
        print("例外エラー：" + t)
    finally:
        print('all finish')

divide_else(1, 2)
divide_else(1, 0)
