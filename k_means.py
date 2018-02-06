import math
import numpy
import random
#from numpy.random import *

#点と点の距離を返す
def distance(point1, point2):

    x1 = point1[0]
    x2 = point2[0]
    y1 = point1[1]
    y2 = point2[1]

    distance_between_points = math.sqrt(numpy.square(x1-x2) + numpy.square(y1-y2))

    return distance_between_points

#dotsの最初のkつをスタート点に定める
def start_points(dots, k):
    random.shuffle(list(set(dots)))

    return dots[:k]

#与えられたlistの中心点を求める
def center_of_list(input_list):

    len_of_input_list = len(input_list)

    total_x = 0
    total_y = 0

    for i in input_list:
        total_x = total_x + i[0]
        total_y = total_y + i[1]

    ave_x = total_x/len_of_input_list
    ave_y = total_y/len_of_input_list

    return (ave_x,ave_y)

#listをグループに分ける
def group_by_points(dots, k, center_points):

    #center_points = start_points(dots, k)
    #print(center_points)
    groups = [ [] for i in range(len(center_points))]

    for dot in dots:
        distance_of_center_points = []

        min_distance = 100000
        for i, center_point in enumerate(center_points):
            distance_result = distance(center_point, dot)

            if distance_result < min_distance:
                clustering_group_index = i
                min_distance = distance_result

        groups[clustering_group_index].append(dot)

    return groups

#各groupの中心を求める
def center_point_of_groups(group_list):

    #group_list = group_by_points(groups)
    center_point_list = []

    for group in group_list:
        center_of_group = center_of_list(group)
        center_point_list.append(center_of_group)

    return center_point_list

#中心点が更新されなかったら、ストップする
def k_means(dots, k):

    #start状態
    start_point = start_points(dots, k)
    restart_group = group_by_points(dots, k, start_point)
    restart_point = center_point_of_groups(restart_group)

    #whileで比較し、restart状態とstart状態で一致した場合にストップ
    i = 0
    while start_point != restart_point:
        start_point = restart_point
        restart_group = group_by_points(dots, k, restart_point)
        restart_point = center_point_of_groups(restart_group)


    final_center_points = restart_point
    final_clustering_group = group_by_points(dots, k, final_center_points)

    return final_clustering_group



if __name__ == "__main__":

    dots = [(1,4), (2,2), (2,3), (3,2), (8,3), (2,5), (3,4), (7,2), (7,4),
            (6,3), (5,2), (5,6), (6,6), (6,7), (5,8), (4,8)]

    k = 5
    print(k_means(dots, k))
