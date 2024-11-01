import numpy as np

def calculate(lst):

    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    a = np.reshape(lst, (3, 3))

    r = {
        'mean': [],
        'variance': [],
        'standard deviation': [],
        'max': [],
        'min': [],
        'sum': []
    }

    for ax in [0, 1, None]:
        r['mean'].append(np.mean(a, axis= ax).tolist())
        r['variance'].append(np.var(a, axis= ax).tolist())
        r['standard deviation'].append(np.std(a, axis= ax).tolist())
        r['max'].append(np.max(a, axis= ax).tolist())
        r['min'].append(np.min(a, axis= ax).tolist())
        r['sum'].append(np.sum(a, axis= ax).tolist())

    return r
