# Preliminaries
1. IVT
for a continous function $f:\  [a,b] \rightarrow \mathbb{R}$, $\forall t \in [min_{x\in[a.b]} f(x),max_{x\in[a.b]}f(x)]$ $\exists c \in [a,b]$ such that $f(c)=t$
2. MVT
for a continous function $f:\  [a,b] \rightarrow \mathbb{R}$, that is differentiable on $(a,b)$ $\exists t \in [a,b]$ such that 

$f'(t)=\frac{f(b)-f(a)}{b-a}$
3. Integral MVT
if $g:\  [a,b] \rightarrow \mathbb{R}^+$is continous then for any continous $f:\  [a,b] \rightarrow \mathbb{R}$

$\exists t \in [a,b]$ such that $\int_a^bg(x)f(x)dx=f(t)\int_a^bg(x)dx$
4. Taylor's Theorem
if $f:\  [a,b] \rightarrow \mathbb{R}$ is a $\mathscr{C}^{n+1}$ function, then $\forall x_0 \in [a,b]$

$f(x)=\Sigma_{k=0}^n \frac{f^{(k)}(x_0)(x-x_0)^k}{k!} + \frac{(x-x_0)^{n+1}f^{(n+1)}(\zeta_{x,n})}{(n+1)!}$ where $\zeta_{x,n}$ lies between $x_0$ and $x$

* proof using L'Hospital Rule
* calculation of error terms using ???
# Error in Machine Reading/Operating on a Number
$x_{TRUE}-x_{APPROX}$
## floating point representation
### components
* s: sign
* m: mantissa
* b: base
* e: exponent
### representation
$smb^e$
### normalized floating pint representation	
$\sigma(.a_1,...a_t)_ \beta \beta^e$, that is on a machine with t digits of precision.
$a1\ne 0$
## Approximation Errors
1. Chopping / truncation
* $\beta^{(1-t)}\ge RelError\ge 0$
2. Rounding
* $\beta^{(1-t)}\ge RelError\ge \frac{\beta^{1-t}}{2}$
## Overflow and Underflow Errors
* smallest +ve number represantable
$x_L=(0.1) _ {\beta} \beta ^L$
* largest number representable
$x_U=(0.\gamma \gamma \dots)_ {\beta} \beta^U=(1-\frac{1}{\beta^t}).\beta^U$

## Propogation of Error
### Addition/Subtraction
* Errors simply add/subtract
* Relative error might become very large when subtracting very close values.
### Multiplication/Division
* Errors comparable to required precision.
* Relative errors nearly add/subtract. Pretty good.
### Function Evaluation
* Function is also read approximately, leads to computational error = $f(x_A)-\bar{f}(x_A)$ , negligible
* Exact error is the main error and is given by $f(x)-f(x_A)\cong f'(\zeta)|x_T-x_A|\cong f'(x_A)|x-x_A|$

# Root Finding (Iterative Methods)
Given an initial guess value $x_0$ and construct a sequence

$\{x_n\}$ given by $x_{n+1}=g(x_n)$ using an iteration $g(x)$ dependent on $f(x)$, the function whose roots we are looking for.
## Incremental Search
* for **continous** functions
* set a step value $=\Delta x$, needs to be smaller than distance between two consecutive zeroes.
1. choose any easy to compute $x_{1,0}$
2. get $sgn(f(x_{1,0}))$
3. increment $x$ by $\Delta x$ to obtain $x_{1,1}=x_{1,0}+\Delta x$
4. get $sgn(f(x_{1,1}))$
5. On sign change fix $x_1=x_{1,n-1}$
6. If required, repeat process with smaller $\Delta x$ and $x_{m+1,0}=x_{m}$

## fixed point iteration
for a continous iteration function $g(x)$,

$lim_{n \rightarrow \infty}g(x_n)=\alpha\implies g(\alpha)=\alpha$
## existence of a fixed point
### claim
if $g(x)$ is a continous map from $[a,b]$ to $[a,b]$ then it has a fixed point.
### proof
define $F(x):=g(x)-x$, a continous map on $[a,b]$

wlog, assume $F(a)\ne 0$ and $F(b)\ne 0$ , else we are trivially done.

now $g(a)\gt a \implies F(a)\gt 0$ similarly $F(b)\lt 0$ thus by IVT, $\exists t\in [a,b]$ such that $F(t)=0$ and hence we have found a fixed point
## Contraction map / Lipchitz Map
### definition
 $g(x)$, a continous map from a metric space $(M,d) \rightarrow (M,d)$ is called a contraction if $\exists\ \lambda \in (0,1)$ such that $d(g(x),g(y))\le\lambda* d(x,y)\ \forall\ x,y \in M$
### properties on a closed interal $[a,b]$ on the real line
1. The fixed point ($\alpha$) is unique.
because $|\alpha-\beta|=|g(\alpha)-g(\beta)|\le \lambda|\alpha-\beta|\implies (1-\lambda)|\alpha-\beta|\le 0\implies |\alpha-\beta|\le 0\implies \alpha=\beta$
2. An iteration converges.
because $|\alpha-x_n|=|g(\alpha)-g(x_{n-1})|\le \lambda|\alpha-x_{n-1}|\le\dots\le \lambda^{n}|\alpha-x_0|$ but $\lambda^n\rightarrow 0$
thus $x_n\rightarrow \alpha$
3. $|\alpha-x_n|\le \frac{\lambda^n}{1-\lambda}* |x_1-x_0|$
coz $|\alpha-x_0|\le |\alpha-x_1|+|x_1-x_0|\le \lambda |\alpha-x_0|+|x_1-x_0|\implies (1-\lambda)|\alpha-x_0|\le |x_1-x_0|\implies |\alpha-x_0|\le \frac{|x_1-x_0|}{1-\lambda}$
### special case with known $\lambda$
if $g(x)\in \mathscr{C}^1$ then $\lambda=max_{x\in [a,b]}|g'(x)|$ defines it's contraction constant if it is less than 1

follows because of MVT.

also, here, it converges linearly, since $\alpha-x_{n+1}=g(\alpha)-g(x_n)=g(\zeta)(\alpha-x_n)\implies lim_{n\rightarrow \infty}\frac{|\alpha-x_{n+1}|}{|\alpha-x_n|}=|g(\alpha)|$ $\because g'(x)$ is continous.
## Order of convergence
if $|\alpha-x_{n+1}|\le C|\alpha-x_n|^p$ for some constant $C$ in the limit, then $p$ is called the order of convergence
## Choosing g
* should converge and should converge fast
## Bisection Search
1. find two points using inc search with opposite sign of function values.
2. take the midpoint. $p=(a+b)/2$
3. check which side gives opp func values.
4. change the edge point to that side.
5. repeat.


## Newton Method
1. start at a point close to the zero
2. draw a tangent to the function thru the pt
3. drop a perp from where it touches the func.
4. take this perp's intersection with the x-axis as the new seed.
5. repeat
$x_{i+1}=x_i-\frac{f(x_i)}{f'(x_i)}$

## Regula Falsi
* chords instead of tangents as in newton-raphson
* choose points on opposite sides by incremental search.
* get a new point not by bisection but by drawing a chord joining the functional values and its intersection with the x-axis. $p=\frac{af(b)-bf(a)}{f(b)-f(a)}$
* change the endpoint with the same function sign as $p$ to $p$.
## Secant
* like newton but approximate derivative with divided difference.
* like regula falsi but seeds need not be on opposite sides, so that we draw a secant(extended chord) and not a chord(line segment).
* supra-linear convergence (golden ratio)

$x_{i+1}=\frac{f(x_i)x_{i-1}-f(x_{i-1})x_i}{f(x_i)-f(x_{i-1})}$
# Integration
# Interpolation
## Lagrange/polynomial fitting.
* Goal:  given n points $(x_i,y_i)$ construct a degree n polynomial passing through them.
* ALgorithm: $p_n(x)=\Sigma y_i* l_i(x)$ where $l_i=\Pi_{j \ne i}\frac{x-x_j}{x_i-x_j}$
# Approxiamtion of functions
# ODE
# System of Linear Equations
# System of non-linear equations
* solve using analogue to newton-raphson method. replace derivative by determinant of Jacobian / Total Derievative.
* $X_{i+1}=X_i-\frac{F[X_i]}{det(DF(X_i))}$
# Matrix Eigenvalue Problem
