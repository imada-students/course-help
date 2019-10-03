import random as rnd


adjs = []
with open("adjectives.txt") as f:
    adjs = list(f)

animals = []
with open("animalsExtended.txt") as f:
    animals = list(f)

colors = []
with open("colours.txt") as f:
    colors = list(f)

nouns = []
with open("nouns_basic.txt") as f:
    nouns = list(f)

verbs = []
with open("verbs.txt") as f:
    verbs = list(f)

def choose(l):
    x = rnd.randint(0, len(l)-1)
    return l[x].strip()

def verb():
    v = choose(verbs)
    if v[-3:] == "ing":
        return v

    if v[len(v)-1] == "e":
        v = v[:-1] + "ing"
    else:
        v = v + "ing"
    return v

def generate():
    anim = choose(animals)
    res = "This " + anim
    res += " has a " + choose(colors) + " colored " + choose(nouns)
    res += ".\n"
    res += "It is " + verb()
    res += ".\n"
    res += "%d/10 %s %s.\n" % (rnd.randint(1,12), choose(adjs), anim)
    res += "\n"
    return res


print(generate())
print(generate())
print(generate())
print(generate())
print(generate())
