import math
def calc_f1_score(tp,fp,fn):
    precision = tp/(tp + fp)
    recall = tp/(tp + fn)
    f1_score = 2 * (precision * recall)/(precision + recall)
    return f1_score
assert round(calc_f1_score(tp=2,fp=3,fn=5),2) == 0.33
print(round(calc_f1_score(tp=2,fp=4,fn=5),2))
#cau 1 - dap an C