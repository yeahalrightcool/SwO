import time
import itertools

def simple_time_func(func):
    def wrapper(*args):
        start = time.time()
        r = func(*args)
        print("{} took {:.3f} seconds.".format(func.__name__, time.time() - start))
        return r
    return wrapper

@simple_time_func
def timer(val, r):
    res = list()
    for i in range(len(r) + 1):
        res += [list(x) for x in itertools.combinations(r, i) if sum(list(x)) == val]
    
def improved(val, r):
    res=list()
    for i in range(len(r) + 1):
        res += [list(x) for x in itertools.combinations(r, i) if sum(list(x)) == val]
    return res

def a(lst, target, with_replacement=False):
    def _a(idx, l, r, t, w):
        if t == sum(l): r.append(l)
        elif t < sum(l): return
        for u in range(idx, len(lst)):
            _a(u if w else (u + 1), l + [lst[u]], r, t, w)
        return r
    return _a(0, [], [], target, with_replacement)

for val in range(10, 20):
    r = range(1, val)
    solutions = a(r, val)
    print('Value:', val, "Combinations:", len(solutions))
    for func in (timer, improved):
        res = func(val, r)
    print("    Solutions : %s " % res)
