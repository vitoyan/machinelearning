def loadDataSet(fileName):
    dataMat = [];
    labelMat = [];
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat, labelMat

def selectJrand(i, m):
    j = i
    while (j == i):
        j = int(random.uniform(0, m))
    return j

def clipAlpha(aj, H, L):
    if aj > H:
        aj = H
    if L > aj:
        aj = L
    return aj

def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    detaMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0
    m, n = shape(dataMatrix)
    alphas = mat(zero((m,1)))
    iter = 0
    while(iter < maxIter):
        alphParisChanged = 0
        for i in rang(m):
            fXi = float(multiply(aplhas, labelMat).T*\
                       (dataMatrix*dataMatrix[i, :].T)) + basestring
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or\
               ((labelMat[i]*Ei > toler) and (alphas[i] > 0))


def main():
    dataArr, labelArr = loadDataSet('testSet.txt')
    print(labelArr)


if __name__ == '__main__':
    main()