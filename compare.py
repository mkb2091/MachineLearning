global cache
cache={}
class Compare():
    def __init__(self):
        self.cache={}
        self.valcache
    def CompareDict(self, one, two):
        if str(onev) == str(twov):
            return 1
        allowed=[dict, list, int, float]
        valcache=self.valcache
        try:
            onev=valcache[one]
        except KeyError:
            onev=[a for a in one.values() if type(a) in allowed]
            valcache[one]=onev
        try:
            twov=valcache[two]
        except KeyError:
            twov=[a for a in two.values() if type(a) in allowed]
            
def CompareDict(one, two):
    allowed=[dict, list, int, float]
    onev=[a for a in one.values() if type(a) in allowed]
    twov=[a for a in two.values() if type(a) in allowed]
    if onev==twov:
        return 1
    try:
        return cache[hash(str(onev)+str(twov))]
    except KeyError:
        pass
    result=list()
    add=result.append
    for first, second in zip(onev, twov):
        try:
            if first==second:
                add(1)
            else:
                if first<second:
                    add(first/second)
                else:
                    add(second/first)
        except TypeError:
            if type(first)==dict and type(second)==dict:
                add(CompareDict(first, second))
        except KeyError:
            add(0)
        except Exception as error:
            print(error, type(error))
    try:
        result=sum(result)/len(result)
    except ZeroDivisionError:
        result=0
    cache[hash(str(onev)+str(twov))]=result
    return result
