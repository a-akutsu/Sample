import traceback

try:
    s = "おはよう"
    num = 100
    ans = s + num
    print(ans)
except Exception as e:
    t = traceback.format_exc()
    print("例外エラー：" + t)
