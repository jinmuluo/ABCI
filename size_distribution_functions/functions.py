import numpy as np


def dN_dlnd(N_mode, r_m, sigma, r):
    result = N_mode/np.sqrt(2*np.pi)/np.log10(sigma)
    result = result * np.exp(-(np.log10(r) - np.log10(r_m))**2 / (2*np.log10(sigma)**2))
    return result


def dA_dlnd(N_mode, r_m, sigma, r):
    dNdlnd = dN_dlnd(N_mode, r_m, sigma, r)
    r_m = r_m / 1000
    r = r/1000
    result = 4 * np.pi * r**2 * dNdlnd * np.exp(2*np.log(sigma)**2)
    return result

def dV_dlnd(N_mode, r_m, sigma, r):
    dNdlnd = dN_dlnd(N_mode, r_m, sigma, r)
    r_m = r_m / 1000
    r = r/1000
    result = 4/3 * np.pi * r**3 * dNdlnd* np.exp(9/2*np.log(sigma)**2)
    return result