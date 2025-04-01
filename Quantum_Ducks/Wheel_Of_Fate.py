import random
import pennylane as qml
from pennylane import numpy as np

dev = qml.device("default.qubit", wires=["A", "B"])
@qml.qnode(dev)
def circuit(state):
    list_1=[0,1,2,3,4,5]
    Modifier = random.choice(list_1)
    qml.Hadamard(wires="A")
    qml.CNOT(wires=["A", "B"])
    def fate(Modifier):
        if(Modifier == 0):
            qml.PauliX(wires="A")
            print("You have been gifted with a Pauli-X gate")
        if(Modifier == 1):
            qml.PauliY(wires="A")
            print("You have been gifted with a Pauli-Y gate")
        if(Modifier == 2):
            qml.PauliZ(wires="A")
            print("You have been gifted with a Pauli-Z gate")
        if(Modifier == 3):
            qml.S(wires="A")
            print("You have been gifted with a S gate")
        if(Modifier == 4):
            qml.T(wires="A")
            print("You have been gifted with a T gate")
        if(Modifier == 5):
            print("You have been gifted with a Hadamard gate")
            qml.Hadamard(wires="A")
    fate(Modifier)
    qml.CNOT(wires=["A", "B"])
    qml.Hadamard(wires="A")
    fate(Modifier)
    return qml.state()
    
    
state = np.array([1, 1])
output = circuit(state)
print(output)
# If The output contains a negative sign, they loose the game, negate points or come up with a punishment
# If The output contains a positive sign, they win the game, add points or come up with a reward
# If The output contains a decimal number, they get a neutral outcome, Decide their fate

