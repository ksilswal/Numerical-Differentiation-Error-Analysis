# Numerical-Differentiation-Error-Analysis
A computational study comparing finite-difference methods for numerical differentiation to analytical derivatives, with a focus on convergence behavior, truncation error, and numerical instability near singularities.
## Overview
This project studies the accuracy of numerical differentiation by comparing
finite-difference approximations to analytical derivatives. Forward, backward,
and central difference schemes are implemented and evaluated across a range of
step sizes to analyze convergence behavior, truncation error, and numerical
instability.

## Methods
Three finite-difference schemes were implemented:
- **Forward difference:**  
  \[
  f'(x) \approx \frac{f(x+h) - f(x)}{h}
  \]
- **Backward difference:**  
  \[
  f'(x) \approx \frac{f(x) - f(x-h)}{h}
  \]
- **Central difference:**  
  \[
  f'(x) \approx \frac{f(x+h) - f(x-h)}{2h}
  \]

Each method was applied to several analytic test functions, including
polynomial, exponential, logarithmic, and rational functions. Numerical
approximations were evaluated at fixed points and compared against exact
derivatives.

Step sizes were chosen logarithmically in the range  
\[
h = 10^{-1} \text{ to } 10^{-8}
\]
and absolute error was measured as
\[
\lvert f'_{\text{numerical}}(x) - f'_{\text{exact}}(x) \rvert.
\]

## Results
Error behavior was visualized using log–log plots of absolute error versus step
size. The following patterns were observed:
- Forward and backward differences exhibit first-order convergence
- Central differences exhibit second-order convergence
- For sufficiently small step sizes, error increases due to floating-point
  precision limits
- Numerical differentiation becomes unstable near singularities, as observed
  for rational functions evaluated close to poles

These results align with theoretical expectations for finite-difference
schemes.

## Files
- `differentiation.py` — Implements forward, backward, and central difference methods  
- `experiments.py` — Runs numerical experiments and generates error plots  
- `plots/` — Saved log–log error plots for each test function  

## Usage
Run the full experiment suite with:
```bash
python experiments.py
