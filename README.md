# Matrix Inverter (Python)

A command-line tool that computes the inverse of an ( n \times n ) matrix using **Gaussian elimination** with **exact rational arithmetic**.

---

## Features

* Computes matrix inverses using row operations (no external libraries)
* Uses Python’s `Fraction` class for **exact precision**
* Supports:

* Manual matrix input
* Clean, formatted output
* Handles non-invertible matrices with proper error messages

---

## How It Works

This program performs matrix inversion by:

1. Augmenting the input matrix ( A ) with the identity matrix ( I )

2. Applying elementary row operations to transform:

   [
   [A \mid I] \rightarrow [I \mid A^{-1}]
   ]

3. Extracting the right-hand side as the inverse

All computations are done using exact fractions to avoid floating-point errors.

---

##  Example

### Input

Enter size of matrix (n for nxn): 2
Enter row 1: 1 2
Enter row 2: 3 4

### Output

Inverse matrix:

```
-2     1
3/2   -1/2
```

---


## How to Run

1. Clone the repository:

```
git clone https://github.com/YOUR_USERNAME/matrix-inverter.git
```

2. Navigate into the folder:

```
cd matrix-inverter
```

3. Run the program:

```
python main.py
```

---

##  What I Learned

* Implementing Gaussian elimination from scratch
* Working with 2D data structures in Python
* Handling edge cases like singular matrices
* Writing clean, modular, reusable code

---

