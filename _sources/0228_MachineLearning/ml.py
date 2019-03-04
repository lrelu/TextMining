x = [1,2,3,4,5]
y = [2,4,6,8,10]


def get_cost(w, x, y):
    c = 0.0
    for i in range(len(x)):
        c += (w * x[i] - y[i]) ** 2

    return c / len(x)


def get_gradient(w, x, y):
    g = 0.0
    for i in range(len(x)):
        g += (w * x[i] - y[i]) * x[i]

    return g / len(x)


def main():
    learning_rate = 0.1
    w = 1

    while (True):
        #gradient
        g = get_gradient(w, x, y)
        #weight
        w = w - learning_rate * g
        #cost
        c = get_cost(w, x, y)

        #threshold
        if (c < 0.001):
            print("final: " + str(w))
            break

        print(w)



print(main())