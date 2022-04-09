from  itertools import combinations

EPSILON=1e-10

def is_possible(array):
    s = sum(array)
    n = len(array)
    for i in range(1,n):
        if (s*i)%n==0:
            return True
    return False

def check_for_solution(array):
    if not is_possible(array):
        return False
    mean = sum(array)/len(array)
    for i in range(1, len(array) // 2 + 2):
        for combo in combinations(array, i):
            mean_combo = sum(combo)/len(combo)
            if abs(mean_combo-mean)<EPSILON:
                print(combo)
                return True
    return False

if __name__ == '__main__':
    #array = [1,2,3,4,5,6,7,8]
    array = [i for i in range(1,31)]
    print(check_for_solution(array))
