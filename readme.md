# Weak SINDy Dynamical Systems Project

This project experiments with **Weak SINDy / WSINDy** for recovering governing equations from simulated dynamical systems, including chaotic systems and extremum seeking control examples.

## Systems

- [Lorenz system](https://en.wikipedia.org/wiki/Lorenz_system)
- [Rössler system](https://en.wikipedia.org/wiki/R%C3%B6ssler_attractor)
- Extremum seeking control examples, based on a 2d implementation of the system in this [extremum seeking control video](https://www.youtube.com/watch?v=hxY-IWByn-Q)

## Dependency

This project uses the PyWSINDy ODE implementation as a project dependency/module:

- [MathBioCU/PyWSINDy_ODE](https://github.com/MathBioCU/PyWSINDy_ODE)

Clone or include that repository as needed for local development.

## Setup

Create and activate a virtual environment, then install dependencies from `requirements.txt`:

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows
pip install -r requirements.txt
```
