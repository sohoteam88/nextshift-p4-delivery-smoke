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

Run tests: `python3 -B -m unittest discover -s tests -v`
