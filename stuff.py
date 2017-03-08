# some coding tests that I've run to test out my Python abilities
#will update as time goes on

n = [1,2,3]
def addTwo(x):
    for i in range(len(x)):
      x[i] = x[i] + 2
    return x

print addTwo(n)
