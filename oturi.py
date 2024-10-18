tounyu = int(input('\n100任意のお金(お金∈N)を入れてください:'))
nedan = int(input('購入する商品の金額(金額∈N)を入れてください:'))
oturi = tounyu - nedan

if oturi == 0:
    print('おつりはありません')
    exit
elif tounyu <= nedan:
    print('お金が足りません')
    exit
else:
    if oturi >= 500:
        go = oturi // 500
        oturi = oturi % 500
        print(f'500円硬貨:{go}枚')
    if oturi >= 100:
        hya = oturi // 100
        oturi = oturi % 100
        print(f'100円硬貨:{hya}枚')
    if oturi >= 50:
        gozyu = oturi // 50
        oturi = oturi % 50
        print(f'50円硬貨:{gozyu}枚')
    if oturi >= 10:
        zyu = oturi // 10
        oturi = oturi % 10
        print(f'10円硬貨:{zyu}枚')

    print(f'端数:{oturi}円')