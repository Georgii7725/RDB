with open("allgroups.csv", "r", encoding="utf-8") as ag:
    data = ag.read()
data = data.split('\n')
data = data[1:]
dataAG = []
for row in data:
    row = row.split(',')
    dataAG.append(row[0])
with open("POINTallgroups.csv", "r", encoding="utf-8") as ag:
    data = ag.read()
data = data.split('\n')
data = data[1:]
dataADLIST = []
for i in range(23):
    data[i] = data[i].split(',')
    data[i][0] = dataAG[i]
    row = ""
    for j in range(len(data[i])):
        row += data[i][j] + ","
    data[i] = row + "\n" 
with open("POINTallgroups.csv", "w", encoding="utf-8") as ag:
    for i in range(23):
        ag.write(data[i])
    