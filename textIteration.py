#! /Program Files (x86)/PythonDownload


myFile = open("/Users/gbonn/Summer_Research_2020/pythonTesting/testIteration.txt",'r')
for lineNum, line in enumerate(myFile):
    listLine = line.split()
    for indx in range(len(listLine)):
        print(lineNum, indx, listLine[indx])
