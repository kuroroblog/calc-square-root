# 問題PDF : https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/265459/1/Version2021_10_08_01.pdf
# 演習 5-17 力試し
while True:
    x = input("正の数値を入力してください ")
    if x == 'end':
        exit()

    try:
        x = float(x)
    except ValueError:
        print(x, "は数値に変換できません")
        continue
    except:
        print("予期していないエラーです")
        exit()

    if x <= 0:
        print(x, "は正の数値ではありません")
        continue

    rnew = x

    diff = rnew - x / rnew
    diff = abs(diff)
    while (diff > 1.0E-6):
        r1 = rnew
        r2 = x / r1
        rnew = (r1 + r2) / 2
        print(r1, rnew, r2)
        diff = r1 - r2

        # 相対誤差
        # 参考 : https://mathwords.net/soutaigosa
        # diff = abs(diff) / r2
        # 絶対誤差
        # 参考 : https://mathwords.net/soutaigosa
        diff = abs(diff)

    exit()
