from numpy import *

def loadDataSet(fileName):
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

def distEclud(vecA, vecB):
    return sqrt(sum(power(vecA - vecB, 2)))

def randCent(dataSet, k):
    n = shape(dataSet)[1]
    centroids = mat(zeros((k, n)))
    for j in range(n):
        minJ = min(dataSet[:,j])
        print(type(minJ))
        rangeJ = float(max(dataSet[:,j]) - minJ)
        centroids[:, j] = minJ + rangeJ * random.rand(k,1)
    return centroids
def kMeans(dataSet, k, disMeas = distEclud, createCent = randCent):
    m = shape(dataSet)[0]
    clusterAssment = mat(zeros((m, 2)))
    centroids = createCent(dataSet, k)
    clusterChanged = True
    while clusterChanged:
        clusterChanged = False
        for i in range(m):
            minDist = inf
            minIndex = -1
            for j in range(k):
                distJI = disMeas(centroids[j, :], dataSet[i, :])
                if distJI < minDist:
                    minDist = distJI
                    minIndex = j
            if clusterAssment[i, 0]  != minIndex:
                clusterChanged = True
            clusterAssment[i, :] = minIndex, minDist**2
        for cent in range(k):
            ptsInclust = dataSet[nonzero(clusterAssment[:, 0].A == cent)[0]]
            centroids[cent, :] = mean(ptsInclust, axis = 0)
    return centroids, clusterAssment

def main():
    datMat = mat(loadDataSet('testSet.txt'))
    rankC = randCent(datMat, 2)
    print(rankC)
    dis = distEclud(datMat[0], datMat[1])
    print(dis)
    myCentroids, clustAssing = kMeans(datMat, 4)
    print(myCentroids)
    print(clustAssing)
    
if __name__ == '__main__':
    main()
    