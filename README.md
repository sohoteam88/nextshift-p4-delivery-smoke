# NextShift P4 disposable arithmetic smoke

Synthetic, non-business test repository. No production data or credentials.

`src.operations.add(a, b)` returns the sum of two numbers.

`src.operations.multiply(a, b)` returns the product of two numbers, supporting
positive, negative, zero, and fractional values.

```python
from src.operations import multiply

multiply(2, 3)       # 6
multiply(-2, 3)      # -6
multiply(0, 5)       # 0
multiply(1.5, 2.5)   # 3.75
```

Run from the repository root:
`python3 -B -c "from src.operations import multiply; print(multiply(1.5, 2.5))"`
(prints `3.75`).

`src.operations.subtract(a, b)` returns `a - b`, supporting positive, negative,
zero, and fractional values. Operand order matters.

```python
from src.operations import subtract

subtract(5, 3)       # 2
subtract(3, 5)       # -2
subtract(-2, 3)      # -5
subtract(2, -3)      # 5
subtract(0, 5)       # -5
subtract(5, 0)       # 5
subtract(2.5, 1.25)  # 1.25
```

Run from the repository root:
`python3 -B -c "from src.operations import subtract; print(subtract(2.5, 1.25))"`
(prints `1.25`).

Run tests: `python3 -B -m unittest discover -s tests -v`
