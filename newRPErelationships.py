# Governing Equations in Rocket Propulsion Elements
# by: Christian Miranda

# ---------------------------------------------------------------------------------------------------

# Library Import:
import numpy as np
import scipy as spi
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------------------

# ---------------------------------------------------------------------------------------------------
# Total Impulse Equations:


# (this assumes exponential decay in thrust over time -- transient):
# initialization

T_init = 1000 # initial thrust force (kN)
m_init = 1 # initial mass flow rotate (kg/s)
time_final = 1000 # final time (s)
num_points = 10 # number of points for integration
timeValues = np.linspace(0,time_final,num_points)

# we define this as part of the total impulse equation below
def thrustForce(t):
    x = 2 # power of e (e^2)
    return 2*np.exp(-2 * x * t) # sample equation for thrust force, y = 2e^(-2t)

forceValues = thrustForce(timeValues) # calculates thrust force at EACH given step in linspace

# fyi: scipy.integrate.quad = continuous functions; numpy.trapz = discrete, time-step data (aka experimental results)
# trapezoidal integration = trapz

total_impulse_tran = np.trapz(forceValues,timeValues) # integrates/sums each individual calculation in forceValues

# (this assumes steady-state where transients are negligible and thrust is constant):
# T = 1 # thrust force (kN)
# sample_time = 100 # time (s)
# total_impulse_ss = T*sample_time

# ---------------------------------------------------------------------------------------------------
# Specific Impulse Equations:


# initialization
T = 1 # thrust force (kN)
m_dot_LOX = 1 # idealized mass flow rate for oxidizer (LOX) -- define later
m_dot_fuel = 1 # idealized mass flow rate for fuel (RP-1/Kerosene) -- define later
m_dot_total = m_dot_LOX + m_dot_fuel # combined idealized mass flow rate for propellants

# Equation 1 | Time-averaged specific impulse; varying mass flow rate and thrust force over time (works for transients too)
g_0 = 9.81 # acceleration due to gravity (m/s^2)

def m_dot(t):
    return 

# Equation 3 | Constant mass flow rate, constant thrust force, and negligible start/stop transient
I_s_3 = (T) / (m_dot_total)