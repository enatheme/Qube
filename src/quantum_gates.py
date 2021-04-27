import math
from qiskit.quantum_info.operators import Operator

def compute_first_operand(numerator, divisor):
    return math.cos(((numerator) / divisor) * (math.pi / 2))

def compute_second_operand(numerator, divisor):
    return math.cos(((divisor - numerator) / divisor) * (math.pi / 2))

def C2HGate(numerator = 1, divisor = 1):
    h1 = compute_first_operand(numerator, divisor)
    h2 = compute_second_operand(numerator, divisor)
    return Operator([
        [1, 0, 0, 0],
        [0, h1, 0, h2],
        [0, 0, 1, 0],
        [0, h2, 0, -h1]
    ])

def C2HGateNot(numerator = 1, divisor = 1):
    h1 = compute_first_operand(numerator, divisor)
    h2 = compute_second_operand(numerator, divisor)
    return Operator([
        [h1, 0, h2, 0],
        [0, 0, 0, 1],
        [h2, 0, -h1, 0],
        [0, 1, 0, 0]
    ])

def C3HGateAnd(numerator = 1, divisor = 1):
    h1 = compute_first_operand(numerator, divisor)
    h2 = compute_second_operand(numerator, divisor)
    return Operator([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, h1, 0, 0, 0, h2],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, h2, 0, 0, 0, -h1],
    ])

def C3HGateAndNot(numerator = 1, divisor = 1):
    h1 = compute_first_operand(numerator, divisor)
    h2 = compute_second_operand(numerator, divisor)
    return Operator([
        [1, 0, 0, 0, 0, 0, 0, 0],
        [0, h1, 0, 0, 0, h2, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
        [0, h2, 0, 0, 0, -h1, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0],
    ])

def C4HGate(numerator = 1, divisor = 1):
    h1 = compute_first_operand(numerator, divisor)
    h2 = compute_second_operand(numerator, divisor)
    return Operator([
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, h1, 0, 0, 0, 0, 0, 0, 0, h2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, h2, 0, 0, 0, 0, 0, 0, 0, -h1, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    ])
