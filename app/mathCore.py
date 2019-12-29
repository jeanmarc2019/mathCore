import json
import random
import urllib.request


def oeis(q):
    """Retrieve the OEIS accession data.
    
    Arguments:
        q {[str]} -- [the A-number]
    """
    url = f"https://oeis.org/search?q=id:{q}&fmt=json"
    with urllib.request.urlopen(url) as file:
        return json.load(file)

# generates portion of result from Cantor's diagonalization argument
def countabilityProof():
    floatList = []
    result = ''
    for i in range(50):
        # excludes 0, to comply with proof requirement
        num = 0
        while float(num) == 0:
            num = random.random()
        floatList.append('{0:.50f}'.format(num))

    for i in range(2, 50):
        if int(floatList[i][i]) == 0:
            result += str(1)
        else:
            result += str(0)

    return result
