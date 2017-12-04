#!/usr/bin/python

from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) -1
    dataMat = []
    labMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = []
        curLine = line.strip().split('\t')
        for i in range(numFeat):
            lineArr.append(float(curLine[i]))
        dataMat.append(lineArr)
        labMat.append(float(curLine[-1]))
    return dataMat, labMat

def standRegres(xArr, yArr):
    xMat = mat(xArr);yMat = mat(yArr).T
    xTx = xMat.T*xMat
    if linalg.det(xTx) == 0.0:
        print("this matrix is singular, cannot do inverse")
        return
    ws = xTx.I * (xMat.T*yMat)
    return ws

def gradientDescent(xArr, yArr, alph, iterNum):
    xMat = mat(xArr)
    m,n = xMat.shape
    yMat = mat(yArr).T
    theta = ones((n, 1))
    theta = mat(theta)
    thetaHistory = []
    for iter in range(iterNum):
        theta = theta - alph*(xMat.T * (xMat*theta - yMat))/m
        thetaHistory.append(theta);
    return thetaHistory
    
def showPlot(xArr, yArr, ws):
    xMat = mat(xArr)
    yMat = mat(yArr)
    yHat = xMat*ws
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xMat[:, 1].flatten().A[0], yMat.T[:, 0].flatten().A[0])
    xCopy = xMat.copy()
    xCopy.sort(0)
    yHat = xCopy*ws
    ax.plot(xCopy[:,1],yHat)
    plt.show()

def lwlr(testPoint, xArr, yArr, k = 1.0):
    xMat = mat(xArr);yMat = mat(yArr).T
    m = shape(xMat)[0]
    weights = mat(eye(m))
    for j in range(m):
        diffMat = testPoint - xMat[j,:]
        weights[j,j] = exp(diffMat*diffMat.T/(-2.0*(k**2)))
    xTx = xMat.T * (weights * xMat)
    if(linalg.det(xTx) == 0.0):
        print("this matrix is singular, can not do inverse")
        return
    ws = xTx.I * (xMat.T * (weights * yMat))
    return testPoint*ws

def lwlrTest(testArr, xArr, yArr, k = 1.0):
    m = shape(testArr)[0]
    yHat = zeros(m)
    for i in range(m):
        yHat[i] = lwlr(testArr[i], xArr, yArr,k)
    return yHat

def lwlrBGD(xArr, yArr, alph, iterNum, k):
    xMat = mat(xArr)
    m,n = xMat.shape
    yMat = mat(yArr).T
    theta = ones((n, 1))
    theta = mat(theta)
    thetaHistory = []
    for iter in range(iterNum):
        theta = theta - alph*(xMat.T * (xMat*theta - yMat))/m
        weight = exp(())    
    return thetaHistory

def showLwlrPlot(xArr, yArr, k):
    xMat = mat(xArr)
    yHat = lwlrTest(xArr, xArr, yArr, k)
    srtInd = xMat[:,1].argsort(0)
    xSort = xMat[srtInd][:,0,:]
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(xSort[:,1], yHat[srtInd])
    ax.scatter(xMat[:,1].flatten().A[0], mat(yArr).T.flatten().A[0], s = 2, c = 'red')
    plt.show()
    
def main():
    xArr,yArr = loadDataSet('ex0.txt')
    print("use normal equation to get ws")
    ws1 = standRegres(xArr, yArr)
    print("ws by normal equation is")
    print(ws1)
    print("use liner regression to get ws")
    ws2 = standRegres(xArr, yArr)
    print("ws by liner regression is")
    print(ws2)
    print("the plot is")
    showPlot(xArr, yArr, ws1)
    #input("Press Enter to continue...")
    #print("use Locally Weighted Linear Regression to get Y")
    #print(lwlr(xArr[0], xArr, yArr, 1.0))
    print("use Locally Weighted Linear Regression with K = 1.0 plot is")
    showLwlrPlot(xArr, yArr, 1.0)
    print("use Locally Weighted Linear Regression with K = 0.01 plot is")
    showLwlrPlot(xArr, yArr, 0.01)
    print("use Locally Weighted Linear Regression with K = 0.003 plot is")
    showLwlrPlot(xArr, yArr, 0.003)


if __name__ == '__main__':
    main()