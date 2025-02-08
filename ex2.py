winer8 = ''
winer9 = ''
winer10 = ''
winer11 = ''
winner_alg = ''
winner_geo = ''
max8 = 0
max9 = 0
max10 = 0
max11 = 0
max_alg = 0
max_geo = 0
f=open('111.txt', encoding='utf-8')
for i in f:
    FIO = i.split()[0] + ' ' + i.split()[1]
    summa_ballov = int(i.split()[3]) + int(i.split()[4])
    if i.split()[2] == '8':
        if summa_ballov > max8:
            max8 = summa_ballov
            winner8 = FIO
        elif summa_ballov == max8:
            winner8 += ', ' + FIO
    elif i.split()[2] == '9':
        if summa_ballov > max9:
            max9 = summa_ballov
            winner9 = FIO
        elif summa_ballov == max9:
            winner9 += ', ' + FIO
    elif i.split()[2] == '10':
        if summa_ballov > max10:
            max10 = summa_ballov
            winner10 = FIO
        elif summa_ballov == max10:
            winner10 += ', ' + FIO
    else:
        if summa_ballov > max11:
            max11 = summa_ballov
            winner11 = FIO
        elif summa_ballov == max11:
            winner11 += ', ' + FIO
    if max_alg < int(i.split()[3]):
        max_alg = int(i.split()[3])
        winner_alg = i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2]
    elif max_alg == int(i.split()[3]):
        winner_alg += ', ' +  i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2]
    if max_geo < int(i.split()[4]):
        max_geo = int(i.split()[4])
        winner_geo = i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2]
    elif max_geo == int(i.split()[4]):
        winner_geo += ', ' +  i.split()[0] + ' ' + i.split()[1] + ' ' + i.split()[2]
f.close()
print(winner8, max8)
print(winner9, max9)
print(winner10, max10)
print(winner11, max11)
print(winner_alg, max_alg)
print(winner_geo, max_geo)