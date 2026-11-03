import numpy as np

def sigmoid(x: list | float) -> np.ndarray | float:
    """
    Returns the sigmoid value for a scalar or each element of a list.
    """

    arr = np.asarray(x, dtype = float)
    res = 1 / (1 + np.exp(-arr))
    print(res)

    if np.isscalar(x):
        return float(res)
    return res;



    # Write code here
    pass