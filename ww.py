def need_jacket(temp):
    if not isinstance(temp, (int, float)):
        return False
    if temp < 10:
        return True
    else:
        return False
