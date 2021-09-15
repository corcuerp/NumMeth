from numpy import *

def solver_linear_damping(I, V, m, b, s, F, t):
    N = t.size - 1              # No of time intervals
    dt = t[1] - t[0]            # Time step
    u = zeros(N+1)              # Result array
    u[0] = I
    u[1] = u[0] + dt*V + dt**2/(2*m)*(-b*V - s(u[0]) + F[0])

    for n in range(1,N):
        u[n+1] = 1./(m + b*dt/2)*(2*m*u[n] + \
            (b*dt/2 - m)*u[n-1] + dt**2*(F[n] - s(u[n])))
    return u

def s(u):
    return 2*u

T = 10*pi      # simulate for t in [0,T]
dt = 0.2
N = int(round(T/dt))
t = linspace(0, T, N+1)
F = zeros(t.size)
I = 1; V = 0
m = 2; b = 0.2
u = solver_linear_damping(I, V, m, b, s, F, t)

from matplotlib.pyplot import *
plot(t, u)
savefig('tmp.pdf')   # save plot to PDF file
savefig('tmp.png')   # save plot to PNG file
show()
