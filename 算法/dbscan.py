#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/11 0011 下午 5:35
# @Author  : ligang

import sys
import numpy as np
import matplotlib.pyplot as plt
import math
import random
from scipy.spatial import KDTree
from sklearn import datasets
import time
from multiprocessing import Process, Pool, Manager
a = sys.stdout
reload(sys)
sys.setdefaultencoding('utf-8')

global N
N = []
global M
M = []
class visitlist:
    def __init__(self, count=0):
        self.unvisitedlist=[i for i in range(count)]
        self.visitedlist=list()
        self.unvisitednum=count

    def visit(self, pointId):
        self.visitedlist.append(pointId)
        self.unvisitedlist.remove(pointId)
        self.unvisitednum -= 1


def dbscan(dataSet, eps, minPts):
    # numpy.ndarray的 shape属性表示矩阵的行数与列数
    # 行数即表小所有点的个数
    nPoints = dataSet.shape[0]
    # (1) 标记所有对象为unvisited
    # 在这里用一个类vPoints进行实现
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C，簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    # 构建KD-Tree，并生成所有距离<=eps的点集合
    kd = KDTree(dataSet)
    while(vPoints.unvisitednum>0):
        # (3) 随机选择一个unvisited对象p
        p = random.choice(vPoints.unvisitedlist)
        # (4) 标t己p为visited
        vPoints.visit(p)
        # (5) if p 的$\varepsilon$-邻域至少有MinPts个对象
        # N是p的$\varepsilon$-邻域点列表
        N = kd.query_ball_point(dataSet[p], eps)
        if len(N) >= minPts:
            # (6) 创建个一个新簇C，并把p添加到C
            # 这里的C是一个标记列表，直接对第p个结点进行赋值
            k += 1
            C[p] = k
            # (7) 令N为p的$\varepsilon$-邻域中的对象的集合
            # N是p的$\varepsilon$-邻域点集合
            # (8) for N中的每个点p'
            for p1 in N:
                # (9) if p'是unvisited
                if p1 in vPoints.unvisitedlist:
                    # (10) 标记p'为visited
                    vPoints.visit(p1)
                    # (11) if p'的$\varepsilon$-邻域至少有MinPts个点，把这些点添加到N
                    # 找出p'的$\varepsilon$-邻域点，并将这些点去重新添加到N
                    M = kd.query_ball_point(dataSet[p1], eps)
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    # (12) if p'还不是任何簇的成员，把p'添加到c
                    # C是标记列表，直接把p'分到对应的簇里即可
                    if C[p1] == -1:
                        C[p1] = k
        # (15) else标记p为噪声
        else:
            C[p1] = -1

    # (16) until没有标记为unvisited的对象
    return C


def polar_distance(series_a, series_b):
    series_a = np.array(series_a)
    series_b = np.array(series_b)
    tmp_a = np.sqrt(np.sum(series_a ** 2))
    tmp_b = np.sqrt(np.sum(series_b ** 2))
    tmp_c = np.sum(series_a * series_b)
    try:
        tmp_d = tmp_c / (tmp_a * tmp_b)
    except:
        return False
    if tmp_d >= 1:
        return 0
    result = math.acos(tmp_d) / math.pi

    return result


def compute_polar_distance(series_a, series_b):
    union_list = list(series_a[0] | series_b[0])
    series_a_list = []
    series_b_list = []
    for sub_serie in union_list:
        try:
            series_a_list.append(series_a[1][sub_serie])
        except:
            series_a_list.append(0)
        try:
            series_b_list.append(series_b[1][sub_serie])
        except:
            series_b_list.append(0)

    result = polar_distance(series_a_list, series_b_list)
    print "%s\t%s\t%f" %(series_a[-1], series_b[-1], result)
    if result == False and result != 0:
        print "result is none"
        print series_a
        print series_b
        print series_a_list
        print series_b_list
        sys.exit(0)
    else:
        return result


def dbscan_old(dataSet, eps, minPts):
    # numpy.ndarray的 shape属性表示矩阵的行数与列数
    global N
    nPoints = len(dataSet)
    # (1)标记所有对象为unvisited
    # 在这里用一个类vPoints进行买现
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C,簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    while (vPoints.unvisitednum > 0):
        # (3)随机上选择一个unvisited对象p
        p = random.choice(vPoints.unvisitedlist)
        # (4)标记p为visited
        vPoints.visit(p)
        # (5)if p的$\varepsilon$-邻域至少有MinPts个对象
        # N是p的$\varepsilon$-邻域点列表
        N = [i for i in range(nPoints) if compute_polar_distance(dataSet[i], dataSet[p], ) <= eps]
        if len(N) >= minPts:
            # (6)创建个新簇C，并把p添加到C
            # 这里的C是一个标记列表，直接对第p个结点进行赋植
            k += 1
            C[p] = k
            # (7)令N为p的ε-邻域中的对象的集合
            # N是p的$\varepsilon$-邻域点集合
            # (8) for N中的每个点p'
            for p1 in N:
                # (9) if p'是unvisited
                if p1 in vPoints.unvisitedlist:
                    # (10)标记p’为visited
                    vPoints.visit(p1)
                    # (11) if p'的$\varepsilon$-邻域至少有MinPts个点，把这些点添加到N
                    # 找出p'的$\varepsilon$-邻域点，并将这些点去重添加到N
                    M = [i for i in range(nPoints) if compute_polar_distance(dataSet[i], \
                                                           dataSet[p1]) <= eps]
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    # (12) if p'还不是任何簇的成员，把P'添加到C
                    # C是标记列表，直接把p'分到对应的簇里即可
                    if C[p1] == -1:
                        C[p1] = k
        # (15)else标记p为噪声
        else:
            C[p] = -1

    # (16)until没有标t己为unvisitedl内对象
    return C


def get_distance(distance_dict, i, j):
    if i == j:
        return 10000
    try:
        return distance_dict[str(i) + "_" + str(j)]
    except:
        return distance_dict[str(j) + "_" + str(i)]


def dbscan_old_distance_matrix(data_len, eps, minPts, distance_dict):
    # numpy.ndarray的 shape属性表示矩阵的行数与列数
    nPoints = data_len
    # (1)标记所有对象为unvisited
    # 在这里用一个类vPoints进行买现
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C,簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    while (vPoints.unvisitednum > 0):
        # (3)随机上选择一个unvisited对象p
        p = random.choice(vPoints.unvisitedlist)
        # (4)标记p为visited
        vPoints.visit(p)
        # (5)if p的$\varepsilon$-邻域至少有MinPts个对象
        # N是p的$\varepsilon$-邻域点列表
        N = [i for i in range(nPoints) if get_distance(distance_dict, i, p) <= eps]
        if len(N) >= minPts:
            # (6)创建个新簇C，并把p添加到C
            # 这里的C是一个标记列表，直接对第p个结点进行赋植
            k += 1
            C[p] = k
            # (7)令N为p的ε-邻域中的对象的集合
            # N是p的$\varepsilon$-邻域点集合
            # (8) for N中的每个点p'
            for p1 in N:
                # (9) if p'是unvisited
                if p1 in vPoints.unvisitedlist:
                    # (10)标记p’为visited
                    vPoints.visit(p1)
                    # (11) if p'的$\varepsilon$-邻域至少有MinPts个点，把这些点添加到N
                    # 找出p'的$\varepsilon$-邻域点，并将这些点去重添加到N
                    M = [i for i in range(nPoints) if get_distance(distance_dict, i, p1) <= eps]
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    # (12) if p'还不是任何簇的成员，把P'添加到C
                    # C是标记列表，直接把p'分到对应的簇里即可
                    if C[p1] == -1:
                        C[p1] = k
        # (15)else标记p为噪声
        else:
            C[p] = -1

    # (16)until没有标t己为unvisitedl内对象
    return C


def run(process_method, process_num, data_list):
    process_num = process_num
    process_list = []

    eve_process_num = len(data_list) / process_num
    for i in range(process_num - 1):
        process_list.append(
            Process(target=process_method,args=(data_list[i], i)))
    i = process_num - 1
    process_list.append(Process(target=process_method, args=(data_list[i], i)))

    for process in process_list:
        process.start()
        # time.sleep(30)
    process.join()

    # if Process.is_alive()
    process_run_num = 0
    for process in process_list:
        if process.is_alive():
            process_run_num += 1
    while process_run_num > 0:
        process_run_num = 0
        for process in process_list:
            if process.is_alive():
                process_run_num += 1
        print "process_run_num\t" + str(process_run_num)
        time.sleep(0.1)
        # time.sleep(1)
    # print "all process finished"


def compute_distance(distance_dict, p, start_index, end_index, eps):
    tmp_list = []
    print "p in compute_distance_method\t%d" %(p)
    for i in xrange(start_index, end_index):
        if get_distance(distance_dict, p, i) <= eps:
            tmp_list.append(i)

    if p == 0:
        print tmp_list
    return tmp_list


def compute_distance_new(para_list, index_k):
    distance_dict, p, start_index, end_index, eps, result_list = para_list
    tmp_list = []
    # print "p in compute_distance_method\t%d\t%d\t%d" %(p, start_index, end_index)
    for i in xrange(start_index, end_index):
        if get_distance(distance_dict, p, i) <= eps:
            tmp_list.append(i)
    # print tmp_list
    result_list.extend(tmp_list)


def merge_result_list_n(data_list):
    global N
    N = []
    for data in data_list:
        N.extend(data)

    return N


def merge_result_list_m(data_list):
    global M
    M = []
    for data in data_list:
        N.extend(data)

    return M


def dbscan_distance_matrix_multi(data_len, eps, minPts, distance_dict):
    global N
    global M
    N = []
    M = []
    # numpy.ndarray的 shape属性表示矩阵的行数与列数
    nPoints = data_len
    process_num = 40
    p_pool = Pool(process_num)
    every_process_num = data_len / 40
    index_list = []
    for i in range(process_num - 1):
        start_index = i * every_process_num
        end_index = (i + 1) * every_process_num
        index_list.append([start_index, end_index])
    index_list.append([i * every_process_num, nPoints])
    # (1)标记所有对象为unvisited
    # 在这里用一个类vPoints进行买现
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C,簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    compute_distance(distance_dict, 0, 1, 500, 0.1)
    start_flag = 0
    while (vPoints.unvisitednum > 0):
        # (3)随机上选择一个unvisited对象p
        if start_flag == 0:
            p = 0
        else:
            p = random.choice(vPoints.unvisitedlist)
        # (4)标记p为visited
        vPoints.visit(p)
        # (5)if p的$\varepsilon$-邻域至少有MinPts个对象
        # N是p的$\varepsilon$-邻域点列表
        # N = [i for i in range(nPoints) if get_distance(distance_dict, i, p) <= eps]
        print "p in dbscan is:\t%d" %(p)
        for i in range(process_num):
            p_pool.apply_async(func=compute_distance, args=(distance_dict, p, index_list[i][0], index_list[i][1], eps),
                               callback=merge_result_list_n)
        p_pool.close()
        p_pool.join()
        # p_pool.apply_async(func=compute_distance, args=(distance_dict, p, nPoints, ), callback=)
        if p == 0:
            print N
        if len(N) >= minPts:
            # (6)创建个新簇C，并把p添加到C
            # 这里的C是一个标记列表，直接对第p个结点进行赋植
            k += 1
            C[p] = k
            # (7)令N为p的ε-邻域中的对象的集合
            # N是p的$\varepsilon$-邻域点集合
            # (8) for N中的每个点p'
            for p1 in N:
                # (9) if p'是unvisited
                if p1 in vPoints.unvisitedlist:
                    # (10)标记p’为visited
                    vPoints.visit(p1)
                    # (11) if p'的$\varepsilon$-邻域至少有MinPts个点，把这些点添加到N
                    # 找出p'的$\varepsilon$-邻域点，并将这些点去重添加到N
                    # M = [i for i in range(nPoints) if get_distance(distance_dict, i, p1) <= eps]
                    for i in range(process_num):
                        p_pool.apply_async(func=compute_distance,
                                           args=(distance_dict, p, index_list[i][0], index_list[i][1], eps),
                                           callback=merge_result_list_m)
                    p_pool.close()
                    p_pool.join()
                    if p == 0:
                        print M
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    # (12) if p'还不是任何簇的成员，把P'添加到C
                    # C是标记列表，直接把p'分到对应的簇里即可
                    if C[p1] == -1:
                        C[p1] = k
        # (15)else标记p为噪声
        else:
            C[p] = -1
        N = []
        if p == 0:
            print C
        start_flag = 1

    # (16)until没有标t己为unvisitedl内对象
    return C


def dbscan_distance_matrix_multi_process(data_len, eps, minPts, distance_dict):
    global N
    global M
    N = []
    M = []
    manager = Manager()
    result_list_n = manager.list()
    result_list_m = manager.list()
    para_list = []
    # numpy.ndarray的 shape属性表示矩阵的行数与列数
    nPoints = data_len
    process_num = 20
    p_pool = Pool(process_num)
    every_process_num = data_len / 40
    index_list = []
    for i in range(process_num - 1):
        start_index = i * every_process_num
        end_index = (i + 1) * every_process_num
        index_list.append([start_index, end_index])
    index_list.append([i * every_process_num, nPoints])
    # (1)标记所有对象为unvisited
    # 在这里用一个类vPoints进行买现
    vPoints = visitlist(count=nPoints)
    # 初始化簇标记列表C,簇标记为 k
    k = -1
    C = [-1 for i in range(nPoints)]
    compute_distance(distance_dict, 0, 1, 500, 0.1)
    start_flag = 0
    while (vPoints.unvisitednum > 0):
        # (3)随机上选择一个unvisited对象p
        result_list_n = manager.list()
        # if start_flag == 0:
        #     p = 0
        # else:
        p = random.choice(vPoints.unvisitedlist)
        # (4)标记p为visited
        vPoints.visit(p)
        # (5)if p的$\varepsilon$-邻域至少有MinPts个对象
        # N是p的$\varepsilon$-邻域点列表
        # N = [i for i in range(nPoints) if get_distance(distance_dict, i, p) <= eps]
        print "p in dbscan is:\t%d" %(p)
        para_list = []
        for i in range(process_num):
            # p_pool.apply_async(func=compute_distance, args=(distance_dict, p, index_list[i][0], index_list[i][1], eps),
            #                    callback=merge_result_list_n)
            para_list.append([distance_dict, p, index_list[i][0], index_list[i][1], eps, result_list_n])
        # print "process apply_async finish"
        run(compute_distance_new, 20, para_list)
        # p_pool.close()
        # p_pool.join()
        # p_pool.apply_async(func=compute_distance, args=(distance_dict, p, nPoints, ), callback=)
        N = [x for x in result_list_n]
        if p == 0:
            print N
        if len(N) >= minPts:
            # (6)创建个新簇C，并把p添加到C
            # 这里的C是一个标记列表，直接对第p个结点进行赋植
            k += 1
            C[p] = k
            # (7)令N为p的ε-邻域中的对象的集合
            # N是p的$\varepsilon$-邻域点集合
            # (8) for N中的每个点p'
            for p1 in N:
                # (9) if p'是unvisited
                result_list_m = manager.list()
                if p1 in vPoints.unvisitedlist:
                    # (10)标记p’为visited
                    vPoints.visit(p1)
                    # (11) if p'的$\varepsilon$-邻域至少有MinPts个点，把这些点添加到N
                    # 找出p'的$\varepsilon$-邻域点，并将这些点去重添加到N
                    # M = [i for i in range(nPoints) if get_distance(distance_dict, i, p1) <= eps]
                    # for i in range(process_num):
                    #     p_pool.apply_async(func=compute_distance,
                    #                        args=(distance_dict, p, index_list[i][0], index_list[i][1], eps),
                    #                        callback=merge_result_list_m)
                    para_list = []
                    for i in range(process_num):
                        # p_pool.apply_async(func=compute_distance, args=(distance_dict, p, index_list[i][0], index_list[i][1], eps),
                        #                    callback=merge_result_list_n)
                        para_list.append([distance_dict, p, index_list[i][0], index_list[i][1], eps, result_list_m])
                    # print "process apply_async finish"
                    run(compute_distance_new, 20, para_list)
                    M = [x for x in result_list_m]
                    # p_pool.close()
                    # p_pool.join()
                    if p == 0:
                        print M
                    if len(M) >= minPts:
                        for i in M:
                            if i not in N:
                                N.append(i)
                    # (12) if p'还不是任何簇的成员，把P'添加到C
                    # C是标记列表，直接把p'分到对应的簇里即可
                    if C[p1] == -1:
                        C[p1] = k
        # (15)else标记p为噪声
        else:
            C[p] = -1
        N = []
        if p == 0:
            print C
        # start_flag = 1

    # (16)until没有标t己为unvisitedl内对象
    return C

def test():

    X1, Y1 = datasets.make_circles(n_samples=2000, factor=0.6, noise=0.05,
                                   random_state=1)
    X2, Y2 = datasets.make_blobs(n_samples=500, n_features=2, centers=[[1.5, 1.5]],
                                 cluster_std=[[0.1]], random_state=5)

    X = np.concatenate((X1, X2))
    plt.figure(figsize=(12, 9), dpi=80)
    plt.scatter(X[:, 0], X[:, 1], marker='.')
    plt.show()

    start = time.clock()
    C2 = dbscan(X, 0.1, 10)
    end = time.clock()
    print "运行时间:", end - start
    plt.scatter(X[:, 0], X[:, 1], c=C2, marker='.')
    plt.show()


if __name__ == "__main__":
    test()