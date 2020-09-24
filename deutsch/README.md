
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
