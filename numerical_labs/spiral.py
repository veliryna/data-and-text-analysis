import numpy as np
def spiralize(size):
    spiral = [[0 for i in range(size)] for j in range(size)]
    rowBegin = 0
    rowEnd = size - 1
    columnBegin = 0
    columnEnd = size - 1
    print(spiral)
    for i in range(0, size):
        spiral[0][i] = 1
        spiral[i][size-1] = 1
        spiral[size-1][i] = 1
    
    while(rowBegin <= rowEnd and columnBegin <= columnEnd):
        for i in range(columnBegin,columnEnd+1):
            if i <= columnEnd-2:
                if spiral[rowBegin][i+2] != 1:
                    spiral[rowBegin][i] = 1
                else:
                    break
        rowBegin = rowBegin+1
        
        for i in range(rowBegin,rowEnd+1):
            if i <= rowEnd-2:
                if spiral[i+2][columnEnd] != 1:
                    spiral[i][columnEnd] = 1
                else:
                    break
        columnEnd = columnEnd-1        
       
        if rowBegin <= rowEnd:
            for i in range(columnEnd,columnBegin-1,-1):
                if i >= columnBegin+2:
                    if spiral[rowEnd][i-2] != 1:
                        spiral[rowEnd][i] = 1
                    else:
                        break
        rowEnd = rowEnd-1
       
        if columnBegin <= columnEnd:
            for i in range(rowEnd,rowBegin-1,-1):
                if i >= rowBegin+2:
                    if spiral[i-2][columnBegin] != 1:
                        spiral[i][columnBegin] = 1
                    else:
                        break
        columnBegin = columnBegin + 1
    print(np.matrix(spiral))

spiralize(5)