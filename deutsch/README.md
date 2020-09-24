
## Deutsch Algorithm

### Introduction


This python program provided as an example by Google Cirq implements the Deutsch quantum algorithm.

You can refer to this article [The Deutsch-Jozsa algorithm](https://einsteinrelativelyeasy.com/index.php/quantum-mechanics/168-the-deutsch-jozsa-algorithm) on my website [einsteinrelativelyeasy.com](https://einsteinrelativelyeasy.com/) to read a quick introduction to this algorithm.

During this article, we will particularly break down how the oracle works, and how they are implemented.

### Getting Started

You have several options:

 1. The simplest way of executing the algorithm is to execute the Python Jupyter notebook remotely on a machine by clicking the icon [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)
   
 2. If you have Python installed on your local computer
      
     - clone the project
 
     - install Cirq via 
    
```python   
python -m pip install --upgrade pip
python -m pip install cirq
```

Execute `deutsch.py`

Enjoy!

## Program

The quantum circuit implementing the Deutsch algorithm is shown below

<img src="images/deutsch_circuit.png"/>

In a few words, we bring two qubits in a superposition state via a Hadamard gate, we then apply a `quantum oracle` to this 2-qubit state and finally we make a measurement of the first qubit.

These main three steps are defined in the function  `make_deutsch_circuit`

```python 
def make_deutsch_circuit(q0, q1, oracle):
    c = cirq.Circuit()

    # Initialize qubits.
    c.append([X(q1), H(q1), H(q0)])

    # Query oracle.
    c.append(oracle)

    # Measure in X basis.
    c.append([H(q0), measure(q0, key='result')])
    return c
```

This (unique) measure will be enough to determine the nature of the function, at least if she is `constant` or `balanced`.

### Quantum Oracle

The most interesting of the program concerns the second step of the algorithm, i.e. the quantum oracle.

<img src="images/deutsch_oracle.png"/>

The oracle maps the state |x>|y> to |x>|y XOR f(x)> , where + is addition modulo 2.
In other words, the oracle leaves the |x> qubit in its original state, and the |y> qubit is replaced by the XOR operation between y and f(x).

Let us first consider the case where `f(x)= 0`.

The output |x>|y XOR f(x)> equates |x>|y XOR 0> that equates the input |x>|y>, which means basically that the Oracle in this case should do NOTHING.

If we check the piece of code which generates the Oracle

```python 

# Pick a secret 2-bit function and create a circuit to query the oracle.
  secret_function = [random.randint(0, 1) for _ in range(2)]
  oracle = make_oracle(q0, q1, secret_function)
    
def make_oracle(q0, q1, secret_function):
    """ Gates implementing the secret function f(x)."""

    if secret_function[0]:
        yield [CNOT(q0, q1), X(q1)]

    if secret_function[1]:
        yield CNOT(q0, q1)
```

if we have f(x)=0  then secret_function[0] = 0 and secret_function[1] = 0 so that the function make_oracle returns without any oracle.

Let us consider now the case f(x)=x:

<img src="images/CNot.gif"/>

We can check that if f(0)=0 and f(1)=1 the function make_oracle returns actually the CNOT gate.

Another thing that we can verify is that we measure 1 at the end of the algorithm in case of applying a Cnot gate.

The state just after the Oracle is

<img src="images/CNot2.gif"/>

So that applying the Hadamard gate to the first qubit state gives


<img src="images/CNot3.gif"/>

and the measurement is indeed 1.













