from numpy import *

def loadDataSet(fileName, delim = '\t'):
    num = len(open(fileName).readline().strip().split('\t'))
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        lineArr = []
        for i in range(num):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
    dataMat = array(dataMat)
    return asmatrix(dataMat)

def pca(dataMat, topNfeat = 9999999):
    meanVals = mean(dataMat, axis = 0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved, rowvar = 0)
    eigVals, eigVects = linalg.eig(mat(covMat))
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    redEigVects = eigVects[:, eigValInd]
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def main():
    dataMat = loadDataSet('testSet.txt')
    lowDMat, reconMat = pca(dataMat, 1)
    print(shape(lowDMat))

if __name__=='__main__':
    main()