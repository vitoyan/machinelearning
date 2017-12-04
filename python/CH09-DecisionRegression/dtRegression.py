from numpy import *


def loadDataSet(fileName):
    num = len(open(fileName).readline().strip().split('\t'))
    dataMat= []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        lineArr = []
        for i in range(num):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
    dataMat = array(dataMat)
    return asmatrix(dataMat)

def binSplitDataSet(dataSet, feature, value):
    #mat0 = dataSet[nonzero(dataSet[:, feature] > value)][0], :][0]
    mat0 = dataSet[nonzero(dataSet[:, feature] > value)[0], :]
    #mat1 = dataSet[nonzero(dataSet[:, feature] <= value)][0], :][0]
    mat1 = dataSet[nonzero(dataSet[:, feature] <= value)[0], :]
    return mat0, mat1

def regLeaf(dataSet):
    return mean(dataSet[:, -1])

def regErr(dataSet):
    return var(dataSet[:, -1])*shape(dataSet)[0]
    
def chooseBestSplit(dataSet, leafType = regLeaf, errType = regErr, ops = (1,4)):
    tols = ops[0]
    tolN = ops[1]
    if len(set(dataSet[:, -1].T.tolist()[0])) == 1:
        return None, leafType(dataSet)
    m, n = shape(dataSet)
    S = errType(dataSet)
    bestS = inf
    bestIndex = 0
    bestValue = 0
    for featIndex in range(n - 1):
        for splitVal in set(asarray(dataSet[:, featIndex]).ravel()):
            mat0, mat1 = binSplitDataSet(dataSet, featIndex, splitVal)
            if(shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN): 
                continue
            newS = errType(mat0) + errType(mat1)
            if newS < bestS:
               bestS = newS
               bestIndex = featIndex
               bestValue = splitVal
    if (S - bestS) < tols:
        return None, leafType(dataSet)
    mat0, mat1 = binSplitDataSet(dataSet, bestIndex, bestValue)
    if(shape(mat0)[0] < tolN) or (shape(mat1)[0] < tolN):
        return None, leafType(dataSet)
    return bestIndex, bestValue 
    
def createTree(dataSet, leafType = regLeaf, errType = regErr, ops = (1,4)):
    feat, val = chooseBestSplit(dataSet, leafType, errType, ops)
    if feat == None: return val
    retTree = {}
    retTree['spInd'] = feat
    retTree['spVal'] = val
    lSet, rSet = binSplitDataSet(dataSet, feat, val)
    retTree['left'] = createTree(lSet, leafType, errType, ops)
    retTree['right'] = createTree(rSet, leafType, errType, ops)
    return retTree

def main():
    myDat = loadDataSet('ref/ex00.txt')    
    #myMat = mat(myDat)
    myTree = createTree(myDat)
    print(myTree)


if __name__ == '__main__':
    main()

