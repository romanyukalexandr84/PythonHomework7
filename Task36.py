def PrintOperationTable(operation, numRows, numColumns):
    baseLst = [i for i in range (1, numColumns+1)]
    for j in range (1, numRows+1):
        newLst = [operation (i,j) for i in baseLst]
        print(*newLst)

rows = 6
columns = 6

PrintOperationTable(lambda x,y: x*y,rows,columns)