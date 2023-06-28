readList=['0531-7-24.txt']
count=[25,20,24]
for readl in readList:
    readF = open(readl, "r")
    pitches=[]
    for line in readF.readlines():
        # print(float(line.split(",")[0]))
        pitches.append(float(line.split(",")[0]))
    writeF=open(f"output-{readl}",'w')
    outputs=[]
    for min in range(-20,20):
        string =str(min)
        for max in range(45,95):
            
            _checkAddNum = 0
            count = 0
            for pitch in pitches:
                isMinAngle = pitch < min
                isMaxAngle = pitch > max
                if _checkAddNum == 0 and isMinAngle:
                    _checkAddNum += 0.5

                if _checkAddNum == 0.5 and isMaxAngle:
                    _checkAddNum += 0.5

                if _checkAddNum == 1:
                    count += 1
                    _checkAddNum = 0.0
            string=string+f",{count}"
        outputs.append(string+"\n")

    writeF.writelines(outputs)
    writeF.close()
    readF.close()