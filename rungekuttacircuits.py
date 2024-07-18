import numpy as np
import matplotlib.pyplot as plt

def rlc_circuit(t, state, R, L, C, V_in):
    q, I = state
    dI_dt = (V_in(t) - R * I - q / C) / L
    dq_dt = I
    return np.array([dq_dt, dI_dt], dtype=np.float64)

def runge_kutta_4(f, t0, state0, t_end, h, *args):
    t = t0
    state = state0.astype(np.float64)  # Garantir que o estado inicial seja do tipo float64
    t_values = [t]
    state_values = [state]
    
    while t < t_end:
        k1 = h * f(t, state, *args)
        k2 = h * f(t + h/2, state + k1/2, *args)
        k3 = h * f(t + h/2, state + k2/2, *args)
        k4 = h * f(t + h, state + k3, *args)
        
        state += (k1 + 2*k2 + 2*k3 + k4) / 6
        t += h
        
        t_values.append(t)
        state_values.append(state)
    
    return np.array(t_values), np.array(state_values)

# Parâmetros do circuito
R = 5.0  # resistência em ohms
L = 0.5  # indutância em henrys
C = 0.2  # capacitância em farads
V_in = lambda t: 5 * np.sin(2 * np.pi * 1 * t)  # tensão senoidal com amplitude de 5V e frequência de 1Hz
state0 = np.array([0, 0], dtype=np.float64)  # carga inicial e corrente inicial
t0 = 0
t_end = 10
h = 0.01  # Passo de tempo menor para maior precisão

# Simular o circuito RLC
t_values, state_values = runge_kutta_4(rlc_circuit, t0, state0, t_end, h, R, L, C, V_in)

# Visualizar os resultados
plt.plot(t_values, state_values[:, 0], label='Carga (q)')
plt.plot(t_values, state_values[:, 1], label='Corrente (I)')
plt.xlabel('Tempo (t)')
plt.ylabel('Amplitude')
plt.title('Simulação de Circuito RLC usando Runge-Kutta de Quarta Ordem')
plt.legend()
plt.grid(True)
plt.show()
