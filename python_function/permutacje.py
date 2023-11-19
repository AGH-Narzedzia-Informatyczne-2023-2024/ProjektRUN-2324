n = int(input("Please enter number: "))
wolne = []
A = []
for i in range(n):
    wolne.append(1)
    A.append(-1)


def perm(miejsce):
    for j in range(n):
        if wolne[j] == 1:
            A[miejsce] = j
            wolne[j] = 0
            if miejsce + 1 < n:
                perm(miejsce + 1)
            else:
                    print(A)
            wolne[j] = 1

perm(0)