from compare import CompareDict

def match(new, groups):
    potential=list()
    add=potential.append
    compare=CompareDict
    for i in groups:
        now=list()
        nowadd=now.append
        for a in groups[i]:
            nowadd(compare(new, a))
        add([sum(now)/len(now), i])
    return potential

def creategroups(data, threshold=0.8):
    groups=dict()
    groups[hash(str(data[0]))]=[data[0]]
    for i in data:
        result=match(i, groups)
        result=max(result)
        if result[0]>threshold:
            groups[result[1]].append(i)
        else:
            groups[hash(str(i))]=[i]
    return groups
