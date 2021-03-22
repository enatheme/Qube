from qiskit import *

from qiskit import QuantumCircuit, QuantumRegister
from qiskit.quantum_info.operators import Operator
import math
from qiskit.visualization import plot_histogram


def generate_floor_v0(number_line):
    """ version 0 of generation
    simple H gate on all qubits, generates 'flying' floor blocks
    """
    qr = QuantumRegister(number_line)
    cr = ClassicalRegister(number_line)

    circuit = QuantumCircuit(qr, cr)
    circuit.h(qr)

    circuit.barrier()
    circuit.measure(qr, cr)

    qasm_sim = Aer.get_backend('qasm_simulator')
    qobj = assemble(circuit, qasm_sim)

    arr = []
    for j in range(20):
        line = []
        results = qasm_sim.run(qobj, shots = 1).result()
        for i in results.get_counts():
            for k in i:
                line.append(int(k))
            arr.append(line)
    return arr
