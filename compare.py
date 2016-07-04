def CompareDict(one, two):
    if str(one)==str(two):
        return 1
    result=list()
    add=result.append
    for i in set(list(one)+list(two)):
        try:
            first=one[i]
            second=two[i]
            if str(first)==str(second):
                add(1)
            else:
                if first<second:
                    add(first/second)
                else:
                    add(second/first)
        except TypeError:
            if type(first)==dict and type(second)==dict:
                add(CompareDict(first, second))
        except IndexError:
            add(0)
        except Exception:
            pass
    try:
        return sum(result)/len(result)
    except ZeroDivisionError:
        return 0
