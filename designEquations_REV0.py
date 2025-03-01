# Design Equations Derived from Spacha Github Source
# by: Christian Miranda

# ---------------------------------------------------------------------------------------------------

# Library Import:
import numpy as np
import scipy as spi
import math
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------------------------------
# FUNDAMENTAL ASSUMPTIONS

# ---------------------------------------------------------------------------------------------------
# USER PROMPTS

# ---------------------------------------------------------------------------------------------------
# GENERAL CONSTANTS

g_o = 9.81 # acceleration due to gravity (m/s^2)
R_univ = 8.31446 # universal gas constant (J/(mol*K))

# ---------------------------------------------------------------------------------------------------
# COMBUSTION CHEMISTRY | Chemical Equation: C12H26 + O2 -> 12CO2 + 13H2O

# the following code uses simplistic combustion chemistry to obtain the propellants' combined gas constant

mm_C = 12.011/1000 # molar mass of carbon (kg/mol)
mm_H = 1.008/1000 # molar mass of hydrogen (kg/mol)
mm_O = 15.999/1000 # molar mass of oxygen (kg/mol)

mm_C12H26 = (12*mm_C)+(26*mm_H)
mm_O2 = (2*mm_O)
mm_12CO2 = (12*(mm_C + (2*mm_O))) 
mm_13H2O = (12*(2*mm_H + mm_O))
molar_12CO2 = 12
molar_13H2O = 13

mm_LOX = 32/1000 # molar mass of liquid oxyen, O_2 (kg/mol)
mm_RP1 = 170.34/1000 # molar mass of RP-1, ~C_12 H_26 (kg/mol)

mm_products = (mm_12CO2 + mm_13H2O) / (molar_12CO2 + molar_13H2O)
R_exhaust = R_univ / mm_products

R_LOX = R_univ / mm_LOX # specific gas constant for LOX (unitless)
R_RP1 = R_univ / mm_RP1 # specific gas constant for RP-1 (unitless)

# ---------------------------------------------------------------------------------------------------

# in order to calculate the nozzle equations, we need to establish the following: target chamber pressurs (P_c)
# target thrust (thrustForce), and the total mass flow rate of the propellants (m_dot_total)

# to simplify calculations for the moment, we'll establish target cha

m_dot_LOX = None # mass flow rate for liquid oxygen (kg/s)
m_dot_RP1 = None # mass flow rate for kerosene/RP-1 (kg/s)
m_dot_total = m_dot_RP1 + m_dot_LOX # total mass flow rate of both propellants (kg/s)

I_sp = I_t / 

thrustForce = m_dot_total * I_sp * g_o # idealized thrust force given mass flow rate targets and specific impulse









# Nozzle Equation

# initialization


m_dot_total = m_dot_LOX + m_dot_RP1 # cumulative mass flow rate for propellants (kg/s)

throat_pressure = 1 # throat pressure (Pa)
T_i = 1
gamma = 1.2 # ratio of gas specific heats -- rule of thumb, even for LOX and RP-1

# assumes Ideal Gas Law
A_t = (m_dot_total / throat_pressure)*math.sqrt((R_exhaust*T_i)/gamma) # throat area equation (m)
