import numpy as np
import PyWSINDy_ODE.wsindy as ws
import PyWSINDy_ODE.ODE_examples as ODE_examples 
import matplotlib.pylab as plt
from scipy.integrate import solve_ivp

def addNoise(x, noise_ratio):
    """
    addNoise Add normally distributed noise to a solve_ivp solution, stolen from PyWSINDy_ODE

    Args:
        x (numpy ndarray): The values of the solution at each integration time step
        noise_ratio (float): signal to noise ratio

    Returns:
        _type_: _description_
    """
    signal_power = np.sqrt(np.mean(x**2))
    sigma = noise_ratio*signal_power
    noise = np.random.normal(0, sigma, x.shape)
    xobs = x + noise
    return xobs

def recoverDynamics(model):
    """
    recoverDynamics Recover ODEs from a PyWSINDy_ODE wsindy model object

    Args:
        model (object): fitted wsindy model object
    """

    coeffs = model.coef
    tags = model.tags
    num_states = coeffs.shape[1]

    for i in range(num_states):
        equation_terms = []
        for j in range(len(tags)):
            c = coeffs[j, i]
            if np.abs(c) > 1e-5: 
                
                powers = tags[j]
                monomial = ""
                
                for k in range(len(powers)):
                    p = powers[k]
                    if p == 1:
                        monomial += f"x{k}"
                    elif p > 1:
                        monomial += f"x{k}^{int(p)}"
                
                if monomial == "": 
                    equation_terms.append(f"{c:.4f}")
                else:
                    equation_terms.append(f"({c:.4f}){monomial}")
        
        equation_str = " + ".join(equation_terms).replace("+ -", "- ")
        print(f"dx{i}/dt = {equation_str}")

