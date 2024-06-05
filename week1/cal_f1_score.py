import math

def is_int(n):
    return isinstance(n,int)

def calc_f1_score(tp,fp,fn):
    if not is_int(tp):
        print("tp must be int")
        return
    elif not is_int(fp):
        print("fp must be int")
        return
    elif not is_int(fn):
        print("fn must be int")
        return
    if tp <= 0 or fp <= 0 or fn <= 0:
        print("tp,fp,fn must be greater than zero")
        return
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2 * (precision * recall)/(precision + recall)
    return f1_score

#Test
test1 = calc_f1_score(2,3,4)
test2 = calc_f1_score('a',2,3)
test3 = calc_f1_score(-4,2,1)
print(f"{test1} {test2} {test3}")