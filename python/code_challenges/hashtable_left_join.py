

def left_join(ht1, ht2):
    # joined = []
    # for key in ht1:
    #     joined.append([key, ht1[key], ht2.get(key)])
    # return joined
    return [ [key, ht1[key], ht2.get(key)] for key in ht1 ]
