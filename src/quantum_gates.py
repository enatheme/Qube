import math
from qiskit.quantum_info.operators import Operator

def C2HGate():
    h = 1/math.sqrt(2)
    return Operator([
        [1, 0, 0, 0],
        [0, h, 0, h],
        [0, 0, 1, 0],
        [0, h, 0, -h]
    ])
