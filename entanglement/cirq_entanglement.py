#!/usr/bin/env python
# coding: utf-8

# # Entanglement algorithm with Google Cirq API

# install Cirq API

# In[ ]:


get_ipython().system('pip install --upgrade pip')
get_ipython().system('pip install cirq==0.8.0')


# Required imports

# In[1]:


import random
import numpy as np
import cirq


# In[12]:


# Create a circuit
circuit = cirq.Circuit()
(q0, q1) = cirq.LineQubit.range(2)

# Apply the X-Pauli gate to each qubit
circuit.append([cirq.X(q0), cirq.X(q1)])
# Apply the Hadamard gate to first qubit and CNOT gate to both qubits
circuit.append([cirq.H(q0), cirq.CNOT(q0, q1)])

#Print the Circuit
print("Circuit:")
print(circuit)

#Measure both qubits
circuit.append([cirq.measure(q0), cirq.measure(q1)])

# Simulate the circuit several times.
simulator = cirq.Simulator()
result = simulator.run(circuit, repetitions=20)

#Print the results
print("\nResults:")
print(result)

