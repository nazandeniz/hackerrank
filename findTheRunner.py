if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sets = set(arr)
    sets.discard(max(sets))
    p = max(sets)
    print(p)