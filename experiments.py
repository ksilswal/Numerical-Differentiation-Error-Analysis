import numpy as np
import matplotlib.pyplot as plt
from differentiation import forward_diff, backward_diff, central_diff
import os

# Create plots directory if it doesn't exist
os.makedirs("plots", exist_ok=True)

# Step sizes
h_values = np.logspace(-1, -8, 20)

# Test functions and derivatives
functions = {
    "polynomial": (
        lambda x: x**3 - 2*x + 1,
        lambda x: 3*x**2 - 2,
        1.0
    ),
    "exponential": (
        np.exp,
        np.exp,
        1.0
    ),
    "logarithm": (
        np.log,
        lambda x: 1/x,
        1.0
    ),
    "rational": (
        lambda x: 1 / (x**2 - 1),
        lambda x: -2*x / (x**2 - 1)**2,
        1.5
    )
}

methods = {
    "Forward": forward_diff,
    "Backward": backward_diff,
    "Central": central_diff
}
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PLOTS_DIR = os.path.join(BASE_DIR, "plots")

os.makedirs(PLOTS_DIR, exist_ok=True)
for name, (f, df, x0) in functions.items():
    plt.figure()

    exact = df(x0)

    for method_name, method in methods.items():
        errors = []

        for h in h_values:
            try:
                approx = method(f, x0, h)
                error = abs(approx - exact)
            except Exception:
                error = np.nan

            errors.append(error)

        plt.loglog(h_values, errors, label=method_name)

    plt.xlabel("Step size h")
    plt.ylabel("Absolute error")
    plt.title(f"Numerical Differentiation Error: {name}")
    plt.legend()
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.savefig(os.path.join(PLOTS_DIR, f"{name}_error.png"))
plt.close()
print("Current working directory:", os.getcwd())