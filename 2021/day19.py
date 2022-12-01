import math
from itertools import permutations
from collections import defaultdict


with open('inputs/test_input_day19.txt') as f:
    lines = f.read().splitlines()

def get_perms(points):
    signs = [[1, 1, 1], [-1,-1, 1],
             [-1,1,-1], [ 1,-1,-1]]
    perms = set()
    for perm in permutations(points, r=3):
        for s in signs:
            perms.add((perm[0]*s[0], perm[1]*s[1], perm[2]*s[2]))
    return perms

def get_distances(scanner):
    dists = defaultdict(set)
    for i, p1 in enumerate(scanner):
        for j, p2 in enumerate(scanner):
            if i != j:
                dists[p1].add(int(math.sqrt(sum((p1[i]-p2[i])**2 for i in range(3)))))
    return dists

def get_diffs(link, perms):
    diffs = set()
    for perm in perms:
        diffs.add((abs(link[0]-perm[0]), abs(link[1]-perm[1]), abs(link[2]-perm[2])))
    return diffs


scanners = []
for l in lines:
    if l.startswith('---'):
        temp_arr = set()
    elif l == '':
        scanners.append(temp_arr)
    else:
        temp_arr.add(tuple(map(int, l.split(','))))
scanners.append(temp_arr)

first_scanner = scanners.pop(0)
first_dists = get_distances(first_scanner)
intersections = []
for scanner in scanners:
    dists = get_distances(scanner)
    compare = []
    for p1 in first_dists:
        for p2 in dists:
            compare.append(len(first_dists[p1].intersection(dists[p2])))
    intersections.append(max(compare))
print(intersections)
# [12, 3, 3, 6]

def get_offset(a, b, min_shared=10):
    dists_a = get_distances(a)
    dists_b = get_distances(b)
    links = [] # Store linked scanners as tuple (x, y)
    for p1 in dists_a:
        for p2 in dists_b:
            if len(dists_a[p1].intersection(dists_b[p2])) > min_shared:
                links.append((p1, p2))
    print(links)
    diffs = [get_diffs(link[0], get_perms(link[1])) for link in links]
    offset = None
    while offset is None:
        for i in range(len(links)-1):
            for j in range(i+1, len(links)):
                common_points = diffs[i].intersection(diffs[j])
                if len(common_points) == 1:
                    print(common_points)
                    offset = common_points.pop()
                    break
        
    return offset

max_idx = intersections.index(max(intersections))
print(max_idx)

max_scanner = scanners.pop(max_idx)
dists2 = get_distances(max_scanner)
offset = get_offset(first_scanner, max_scanner)
print(offset)
for point in max_scanner:
    first_scanner.add(point[0]+offset[0])


# links = []
# for p1 in first_dists:
#     for p2 in dists2:
#         if len(first_dists[p1].intersection(dists2[p2])) > 10:
#             links.append((p1, p2))
#             print(p1, p2)

# diffs = [get_diffs(link[0], get_perms(link[1])) for link in links[:3]]
# offset = diffs[0].intersection(diffs[1]).intersection(diffs[2]).pop()
# print(offset)



# # results = []
# for i in range(len(links)):
#     print(links[i][0]) 
#     print(links[i][1])
#     temp_results = []
#     for perm in get_perms(links[i][1]):
#         # print(perm)
#         temp_results.append((links[i][0][0]-perm[0], links[i][0][1]-perm[1],
#                              links[i][0][2]-perm[2]))
#     results.append(temp_results)

#     if i == 2:
#         break
# results0 = results[0]
# for result in results[1:]:
#     for point in result:
#         if point in results0:
#             print(point) 

            
                
# p1 = np.array([-618,-824,-621])
# p2 = np.array([686,422,578])
# for perm in get_perms(p2):
#     print(p1 - perm)