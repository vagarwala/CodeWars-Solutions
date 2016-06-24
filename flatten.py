def flatten(lst):
    if str(lst).count('[') == 1:
        return lst
    else:
        return [item for sublist in lst for item in sublist]