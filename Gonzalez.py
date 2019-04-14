

import collections
import math

def gonzalez(data,cluster_num, single_compl_mean):
    if(single_compl_mean == 0):
        return single_link(data,cluster_num)
    if(single_compl_mean == 1):
        return complete_link(data,cluster_num)
    if(single_compl_mean == 2):
        return mean_link(data,cluster_num)
    

def single_link(data, cluster_num):
    clusters = collections.defaultdict(list)
    to_return = collections.defaultdict(list)
    for i in range(0,len(data)):
        clusters[i].append(data[i])
        to_return[i].append((i,data[i]))

    while(len(clusters) > cluster_num):
        x, y = find_min(clusters)
        #print(x,y)
        for i in clusters[y]:
            #print(i)
            #to_return[x].append(i)
            clusters[x].append(i)
        for i in to_return[y]:
            #print(i)
            to_return[x].append(i)
        del clusters[y]
        del to_return[y]
        #print(clusters)
    return to_return

def complete_link(data, cluster_num):
    clusters = collections.defaultdict(list)
    to_return = collections.defaultdict(list)
    for i in range(0,len(data)):
        clusters[i].append(data[i])
        to_return[i].append((i,data[i]))

    while(len(clusters) > cluster_num):
        x, y = find_max(clusters)
        #print(x,y)
        for i in clusters[y]:
            #print(i)
            clusters[x].append(i)
        for i in to_return[y]:
                to_return[x].append(i)
        del clusters[y]
        del to_return[y]
        #print(clusters)
    return to_return

def mean_link(data, cluster_num): 
    clusters = collections.defaultdict(list)
    to_return = collections.defaultdict(list)
    for i in range(0,len(data)):
        clusters[i].append(data[i])
        to_return[i].append((i,data[i]))

    while(len(clusters) > cluster_num):
        x, y = find_mean(clusters)
        #print(x,y)
        for i in clusters[y]:
            #print(i)
            clusters[x].append(i)
        for i in to_return[y]:
            to_return[x].append(i)
        del clusters[y]
        del to_return[y]
        #print(clusters)
    return to_return

def find_mean(clusters):
    #min1 = 0
    #min2 = 1
    #M = 0
    matr = collections.defaultdict(dict)
    for x,a in clusters.items():
        for y,b in clusters.items():
            if(x != y):
                M = 0
                avg_a = avg(a)
                avg_b = avg(b)
                Mt = dist(avg_a,avg_b)
                #print(Mt)
                if(Mt > M):
                    M = Mt
                matr[x][y] = Mt
    #print(M)
    min1 = 0
    min2 = 0
    min = float("inf")
    for x,y in clusters.items():
        for i,j in clusters.items():
            if x != i:
                if matr[x][i] < min:
                    min = matr[x][i]
                    min1 = x
                    min2 = i
    return (min1,min2)

def avg(a):
    sumx = 0
    sumy = 0
    for i in a:
        sumx += i[1]
        sumy += i[2]
    return [0, sumx/len(a), sumy/len(a)]

def find_max(clusters):
    #min1 = 0
    #min2 = 1
    #M = 0
    matr = collections.defaultdict(dict)
    for x,a in clusters.items():
        for y,b in clusters.items():
            if(x != y):
                M = 0
                for i in a:
                    for j in b:
                        Mt = dist(i,j)
                        #print(Mt)
                        if(Mt > M):
                            M = Mt
                        matr[x][y] = Mt
    #print(M)
    min1 = 0
    min2 = 0
    min = float("inf")
    for x,y in clusters.items():
        for i,j in clusters.items():
            if x != i:
                if matr[x][i] < min:
                    min = matr[x][i]
                    min1 = x
                    min2 = i
    return (min1,min2)


def find_min(clusters):
    #min1 = 0
    #min2 = 1
    #M = 0
    matr = collections.defaultdict(dict)
    for x,a in clusters.items():
        for y,b in clusters.items():
            if(x != y):
                M = float("inf")
                for i in a:
                    for j in b:
                        Mt = dist(i,j)
                        #print(Mt)
                        if(Mt < M):
                            M = Mt
                        matr[x][y] = Mt
    #print(M)
    min1 = 0
    min2 = 0
    min = float("inf")
    for x,y in clusters.items():
        for i,j in clusters.items():
            if x != i:
                if matr[x][i] < min:
                    min = matr[x][i]
                    min1 = x
                    min2 = i
    return (min1,min2)

'''
Euclidean distance - we're not using this
'''
def euc_dist(i,j):
    sum = 0
    for x in range(1, len(i)):
        sum += (i[x] - j[x])**2
    return math.sqrt(sum)

'''
Hamming distance
'''
def dist(i,j):
    hamming = 0
    for x in range(0,len(i)):
        if i[x] != j[x]:
            hamming += 1

    return hamming