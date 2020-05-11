[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)

# Cirq Teleportation Algorithm

Provides Criq Python implementation of the teleportation quantum algorithm as introduced in our article [The quantum teleportation algorithm](https://einsteinrelativelyeasy.com/index.php/quantum-mechanics/163-the-quantum-teleportation-algorithm)

<img src="https://github.com/cyrilondon/quantum-mechanics-java/blob/master/teleportation/src/main/resources/teleportation1.png"/>

## Getting Started

You have several options:

 1. The simplest way of executing the algorithm is to execute the Python Jupiter notebook by clicking the icon [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/cyrilondon/quantum-mechanics-python/master)
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





