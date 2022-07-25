## How to use yacs with argparse

- Yacs config will be updated using input arguments
- You must call [0] at the end of an argument, e.g., cfg.foo[0]. This is because yacs does not allow updating a value with new value with different type. Will be fixed in future (constructing new cfg will fix this problem).
