def damerau_levenshtein(s1: str, s2: str, multiplier: float = 1) -> float:
    d: dict[tuple[int, int], float] = {}
    
    lenstr1 = len(s1)
    lenstr2 = len(s2)
    max_distance = max(lenstr1, lenstr2)
    
    for i in range(-1, lenstr1 + 1):
        d[(i, -1)] = i+1
    
    for j in range(-1, lenstr2 + 1):
        d[(-1, j)] = j+1
    
    for i in range(lenstr1):
        for j in range(lenstr2):
            cost = 0 if s1[i] == s2[j] else 1
            deletion      = d[i-1, j] + multiplier
            insertion     = d[i, j-1] + multiplier
            substitution  = d[i-1, j-1] + cost * multiplier
            transposition = d[i-2, j-2] + cost * multiplier if i and j and s1[i] == s2[j-1] and s1[i-1] == s2[j] else max_distance
            d[(i,j)] = min([deletion, insertion, substitution, transposition])
    
    return d[lenstr1-1,lenstr2-1]

def match(string1: str, string2: str) -> float:
    max_distance = max(len(string1), len(string2))
    return 1 - (damerau_levenshtein(string1, string2) / max_distance)

def match_words(string1: str, string2: str,) -> float:
    if string1 in string2 or string2 in string1:
        return 1
    
    list1, list2 = string1.split(' '), string2.split(' ')
    
    max_distance = min(len(string1), len(string2))
    distance1 = float(0)
    
    for word in list1:
        if word in list2:
            distance1 += 0.9
    
    distance2 = float(0)
    
    for word in list2:
        if word in list1:
            distance2 += 0.9
    
    return max(distance1, distance2) / max_distance

def match_partial(string1: str, string2: str, matcher = match) -> float:
    if len(string1) < len(string2):
        shorter = string1
        longer = string2
    else:
        shorter = string2
        longer = string1
    
    scores = []
    
    for start, stop in get_blocks(string1, string2):
        substr = longer[start:stop]
        scores.append(matcher(shorter, substr))
    
    return max(scores) if scores else 0

def get_blocks(string1: str, string2: str) -> list[tuple[int, int]]:
    long = max(len(string1), len(string2))
    short = min(len(string1), len(string2))
    blocks = []
    
    for i in range(long - short):
        blocks.append((i, i + short))
    
    return blocks