#######################################
# 1) Взять из hack_data.csv ключ и название города
# 2) Найти в Моно-Олиго.csv mode или не найти 
# 3) Найти в Все группы вместе.csv stations and km in year
# 4) Записать в market_system.csv
#######################################

with open("hack_data.csv", 'r') as hd:
    hd = hd.read() 
    hd = hd.split('\n')
    hd = hd[1:]
with open("mono_oligo.csv", 'r', encoding='utf-8') as mo:
    mo = mo.read() 
    mo = mo.split('\n')
    mo = mo[1:]
with open("POINTallgroups.csv", 'r', encoding='utf-8') as ag:
    ag = ag.read() 
    ag = ag.split('\n')
    ag = ag[1:]
for strHD in hd:
    row = ""
    strHD = strHD.split(',')
    #Index
    index = strHD[0]
    row += strHD[0] + ','
    #Mode
    city = strHD[1].strip()
    flag = False
    for strMO in mo:
        if strMO.find(city) != -1:
            strMO = strMO.split(',')
            row += strMO[2] + ','
            flag = True
            break
    if flag == False:
        row += ','
    #Stations and km in year
    flag = False
    for strAG in ag:
        if strAG.find(city) != -1:
            strAG = strAG.split(',')
            row += strAG[7] + ',' + strAG[8] + ','
            flag = True
            break
    if flag == False:
        row += ',' + ','
    row += '\n'
    with open("market_system.csv", 'a', encoding='utf-8') as ms:
        ms.write(row)