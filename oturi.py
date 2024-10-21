tounyu = int(input('\n任意のお金(お金∈N)を入れてください:'))
nedan = int(input('購入する商品の金額(金額∈N)を入れてください:'))
oturi = tounyu - nedan
otugohya = int(input('五百円硬貨の枚数を入力してください'))
otuhya = int(input('百円硬貨の枚数を入力してください'))
otugozyu = int(input('五十円硬貨の枚数を入力してください'))
otuzyu = int(input('十円硬貨の枚数を入力してください'))

if oturi == 0:
    print('おつりはありません')
    exit
elif tounyu <= nedan:
    print('お金が足りません')
    exit

else:
    if oturi >= 500:
        gohya = min(oturi//500,otugohya)
        oturi -= gohya * 500
        print(f'500円硬貨:{gohya}枚')
    if oturi >= 100:
        hya = min(oturi // 100, otuhya)
        oturi -= hya * 100
        print(f'100円硬貨:{hya}枚')
    if oturi >= 50:
        gozyu = min(oturi // 50, otugozyu)
        oturi -= gozyu * 50
        print(f'50円硬貨:{gozyu}枚')
    if oturi >= 10:
        zyu = min(oturi // 10, otuzyu)
        oturi -= zyu * 10
        print(f'10円硬貨:{zyu}枚')
# おつりの硬貨枚数を指定しない場合
# else:
#     if oturi >= 500:
#         go = oturi // 500
#         oturi = oturi % 500
#         print(f'500円硬貨:{go}枚')
#     if oturi >= 100:
#         hya = oturi // 100
#         oturi = oturi % 100
#         print(f'100円硬貨:{hya}枚')
#     if oturi >= 50:
#         gozyu = oturi // 50
#         oturi = oturi % 50
#         print(f'50円硬貨:{gozyu}枚')
#     if oturi >= 10:
#         zyu = oturi // 10
#         oturi = oturi % 10
#         print(f'10円硬貨:{zyu}枚')

    print(f'端数:{oturi}円')
