#using endpoints 
def JI(pred, truth):
    count = 0
    for num in pred:
        if num in truth:
            count += 1
    return count / len(pred)