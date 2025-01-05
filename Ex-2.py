import math
import matplotlib.pyplot as plt

V_t = [5, 4.982, 4.968, 4.953, 4.939, 4.924, 4.910]
t = [0, 30, 60, 90, 120, 150, 180]  
C = 1048e-6  

y = [math.log(v) for v in V_t]

N = len(t)
sum_t = sum(t)
sum_y = sum(y)
sum_t2 = sum([i**2 for i in t])
sum_ty = sum([t[i] * y[i] for i in range(N)])

m = (N * sum_ty - sum_t * sum_y) / (N * sum_t2 - sum_t**2)

R_leakage = -1 / (m * C)

print(f"Estimated leakage resistance R_leakage: {R_leakage/1e6} Mega Ohms")

# Plotting both graphs
fig, axs = plt.subplots(2, 1, figsize=(8, 10))

# V(t) vs t
axs[0].plot(t, V_t, 'bo-', label='V(t) vs t')
axs[0].set_xlabel('Time (seconds)')
axs[0].set_ylabel('Voltage (Volts)')
axs[0].set_title('Capacitor Discharge: V(t) vs t')
axs[0].grid(True)
axs[0].legend()

# log(V(t)) vs t
axs[1].plot(t, y, 'ro-', label='Log(V(t)) vs t')
axs[1].set_xlabel('Time (seconds)')
axs[1].set_ylabel('Log(V(t))')
axs[1].set_title('Capacitor Discharge: Log(V(t)) vs t')
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.show()
