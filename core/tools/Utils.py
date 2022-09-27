

class Utils:
    def count_by(arr, fn=lambda x: x):
        key = {}
        for el in map(fn, arr):
            key[el] = 1 if el not in key else key[el] + 1
        return key

    def quchong(arr):
        return list(set(arr))