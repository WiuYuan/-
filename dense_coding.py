import numpy as np
import tensorcircuit as tc
def dense_coding(b1, b2):
    c = tc.Circuit(2)

    # EPR pair preparation

    c.h(0)
    c.cnot(0, 1)

    # information encoding

    if b1 == 1:
        c.z(0)
    if b2 == 1:
        c.x(0)

    # Bell basis measurement

    c.cnot(0, 1)
    c.h(0)

    r1 = c.cond_measure(0)
    r2 = c.cond_measure(1)

    return r1, r2

print(dense_coding(1,1))
