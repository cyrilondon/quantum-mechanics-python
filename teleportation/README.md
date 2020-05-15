[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)

# Cirq Teleportation Algorithm

Provides Criq Python implementation of the teleportation quantum algorithm as introduced in our article [The quantum teleportation algorithm](https://einsteinrelativelyeasy.com/index.php/quantum-mechanics/163-the-quantum-teleportation-algorithm)

<img src="https://github.com/cyrilondon/quantum-mechanics-java/blob/master/teleportation/src/main/resources/teleportation1.png"/>

## Getting Started

You have several options:

 1. The simplest way of executing the algorithm is to execute the Python Jupyter Notebook by clicking the icon [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)
    - double-click the `teleportation/cirq_teleportation.ipynb` notebook
    - uncomments the two lines of the first cell to install Cirq on the machine
  
```python
pip install --upgrade pip
pip install cirq==0.8.0
```
  
   wait until all the packages have been installed
    
```python
Successfully installed cachetools-4.1.0 cirq-0.8.0 cycler-0.10.0 freezegun-0.3.15 google-api-core-1.17.0 google-auth-1.14.2 googleapis-common-protos-1.51.0 
grpcio-1.28.1 kiwisolver-1.2.0 matplotlib-3.2.1 mpmath-1.1.0 networkx-2.4 numpy-1.18.4 pandas-1.0.3 protobuf-3.8.0
 pyasn1-0.4.8 pyasn1-modules-0.2.8 pyparsing-2.4.7 pytz-2020.1 rsa-4.0 scipy-1.4.1 sortedcontainers-2.1.0 sympy-1.5.1 typing-extensions-3.7.4.2
```

Place yourself into the next Cell import packages and execute `Cell -> Run All Below`

You should see something similar into your browser:

```python
Circuit:
0: ───X^0.161───Y^0.663───@───H───M───────@───
                          │       │       │
1: ───H─────────@─────────X───────M───@───┼───
                │                     │   │
2: ─────────────X─────────────────────X───@───

Bloch Sphere of Message After Random X and Y Gates:
x:  0.7623 y:  -0.4853 z:  -0.4283

Bloch Sphere of Qubit 2 at Final State:
x:  0.7623 y:  -0.4853 z:  -0.4283
```

   You are ready to execute the Notebook directly in the browser!
 
 2. if you have Python installed on your computer
 
     - install Cirq via 
    
```python   
python -m pip install --upgrade pip
python -m pip install cirq
```

Execute `python cirq_teleportation.py`

Enjoy!

## Program

We bring the `msg` qubit to be teleported in a random state, which as we know can be represented on the unit Bloch Sphere as a point with coordinates x, y and z.
Those coordinates are printed out on the console.

```python 
 q0 = cirq.LineQubit(0)
 message = sim.simulate(cirq.Circuit([cirq.X(q0)**ranX, cirq.Y(q0)**ranY]))

 print("\nBloch Sphere of Message After Random X and Y Gates:")
 # Prints the Bloch Sphere of the Message after the X and Y gates.
 expected = cirq.bloch_vector_from_state_vector(message.final_state, 0)
 print("x: ", np.around(expected[0], 4), "y: ", np.around(expected[1], 4),
      "z: ", np.around(expected[2], 4))
```

We apply the teleportation circuit to the three qubits msg, alice and bob

```python 
 # Creates Bell state to be shared between Alice and Bob.
 circuit.append([cirq.H(alice), cirq.CNOT(alice, bob)])
 # Creates a random state for the Message.
 circuit.append([cirq.X(msg)**ranX, cirq.Y(msg)**ranY])
 # Bell measurement of the Message and Alice's entangled qubit.
 circuit.append([cirq.CNOT(msg, alice), cirq.H(msg)])
 circuit.append(cirq.measure(msg, alice))
 # Uses the two classical bits from the Bell measurement to recover the
 # original quantum Message on Bob's entangled qubit.
 circuit.append([cirq.CNOT(alice, bob), cirq.CZ(msg, bob)])
```

Finally we print out the bob qubit, and we check that it is represented by exactly the same point on the Bloch Sphere:

```python 
 print("\nBloch Sphere of Qubit 2 at Final State:")
 # Prints the Bloch Sphere of Bob's entangled qubit at the final state.
 teleported = cirq.bloch_vector_from_state_vector(final_results.final_state,
                                                     2)
 print("x: ", np.around(teleported[0], 4), "y: ",
 np.around(teleported[1], 4), "z: ", np.around(teleported[2], 4))
```



