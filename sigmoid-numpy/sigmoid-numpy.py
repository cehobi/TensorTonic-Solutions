import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """

    arr = np.asarray(x, dtype = float)
    res = 1 / (1 + np.exp(-arr))

    if np.isscalar(x):
        return float(res)
    return res;

    print(res)


    # Write code here
    pass