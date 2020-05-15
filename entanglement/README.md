
## Entangled Bell State

### Introduction


This first quantum program brings two qubits to one of the four simplest and maximal entangled two-qubit states, i.e the Bell state |B11>.

Namely, it implements the following quantum circuit:

<img src="https://einsteinrelativelyeasy.com/images/Quantum/CNOT_program1.png" >

which formally equates to:

<img src="https://einsteinrelativelyeasy.com/images/Quantum/Bellstate9.gif"/>

You can refer to this article [C-NOT gate, Bell State and Entanglement ](https://einsteinrelativelyeasy.com/index.php/quantum-mechanics/156-c-not-gate-bell-state-and-entanglement) on my website [einsteinrelativelyeasy.com](https://einsteinrelativelyeasy.com/) to refresh your memory about this formalism.

And you may also find it useful to read this article [Introduction-to-entanglement](https://einsteinrelativelyeasy.com/index.php/quantum-mechanics/147-introduction-to-entanglement) to give you an overall view of entanglement and to remind you that an entanglement state **can not be written as product state**.

### Getting Started

You have several options:

 1. The simplest way of executing the algorithm is to execute the Python Jupyter notebook by clicking the icon [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)
    - double-click the `entanglement/cirq_entanglement.ipynb` notebook
    - place yourself into the first cell and click execute to to install Cirq on the machine
  
```python
pip install --upgrade pip
pip install cirq==0.8.0
```
  
 Wait until all the packages have been installed
    
```python
Successfully installed cachetools-4.1.0 cirq-0.8.0 cycler-0.10.0 freezegun-0.3.15 google-api-core-1.17.0 google-auth-1.14.2 googleapis-common-protos-1.51.0 
grpcio-1.28.1 kiwisolver-1.2.0 matplotlib-3.2.1 mpmath-1.1.0 networkx-2.4 numpy-1.18.4 pandas-1.0.3 protobuf-3.8.0
 pyasn1-0.4.8 pyasn1-modules-0.2.8 pyparsing-2.4.7 pytz-2020.1 rsa-4.0 scipy-1.4.1 sortedcontainers-2.1.0 sympy-1.5.1 typing-extensions-3.7.4.2
```

Place yourself into the next Cell import packages and execute `Cell -> Run All Below`

You should see something similar into your browser:

    
```python
Circuit:
0: ───X───H───@───
              │
1: ───X───────X───

Results:
0=10100001111000001100
1=01011110000111110011
```
