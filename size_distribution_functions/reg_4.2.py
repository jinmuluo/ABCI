import numpy as np
import matplotlib.pyplot as plt
from functions import dN_dlnd, dA_dlnd, dV_dlnd
from aerosols import nucleation, aitken,accumulation, coarse, super_coarse


diameters = np.arange(1, 20000, 0.1, dtype=float)


def graph():
    fig, axs = plt.subplots(3, 2, figsize=(12, 8))
    
    # figure 4.2 (row 1 col 1)
    N_1 = dN_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(N_1 >= 1)]
    y = N_1[np.where(N_1 >= 1)]
    axs[0, 0].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[0, 0].set_xscale("log")

    N_2 = dN_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(N_2 >= 1)]
    y = N_2[np.where(N_2 >= 1)]
    axs[0, 0].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    N_3 = dN_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(N_3 >= 1)]
    y = N_3[np.where(N_3 >= 1)]
    axs[0, 0].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')

    N = N_1 + N_2 + N_3
    x = diameters[np.where(N >= 1)]
    y = N[np.where(N >= 1)]
    axs[0, 0].plot(x, y+10, linestyle='solid', linewidth=5.0, c='black', alpha=0.3)
    
    axs[0,0].arrow(x=40, y=980, dx=200, dy=0, width=28, color='black', alpha=0.8, shape='right')
    axs[0,0].arrow(x=1100, y=600, dx=18000, dy=0, width=28, color='black', alpha=0.8, shape='right')
    axs[0,0].arrow(x=200, y=850, dx=1000, dy=0, width=28, color='black', alpha=0.8, shape='right')

    axs[0,0].set_xlim(1, 20000)
    axs[0,0].set_ylim(0, 1100)
    axs[0,0].set_ylabel("dN/dlog $\it{d}$ / $cm^{-3}$")
    axs[0,0].text(1.5, 1000, "Number", size=13)
    axs[0,0].text(60, 1010, "CCN", size=13)
    axs[0,0].text(150, 730, "Light scattering", size=13)
    axs[0,0].text(1000, 490, "Cloud drops", size=13)
    

    # figure 4.2 (row 1 col 2)
    N_1 = dN_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(N_1 >= 0.1)]
    y = N_1[np.where(N_1 >= 0.1)]
    axs[0, 1].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[0, 1].set_xscale("log")
    axs[0, 1].set_yscale("log")

    N_2 = dN_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(N_2 >= 0.1)]
    y = N_2[np.where(N_2 >= 0.1)]
    axs[0, 1].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    N_3 = dN_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(N_3 >= 0.1)]
    y = N_3[np.where(N_3 >= 0.1)]
    axs[0, 1].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')


    N_4 = dN_dlnd(coarse[0], coarse[1], coarse[2], diameters)
    x = diameters[np.where(N_4 >= 0.1)]
    y = N_4[np.where(N_4 >= 0.1)]
    axs[0, 1].plot(x, y, linestyle='dashed', linewidth=1.5, c='black')

    axs[0,1].set_xlim(1, 20000)
    axs[0,1].set_ylim(0.1, 10000)
    axs[0,1].set_ylabel("dN/dlog $\it{d}$ / $cm^{-3}$")


    # figure 4.2 (row 2 col 1)
    A_1 = dA_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(A_1 >= 0.1)]
    y = A_1[np.where(A_1 >= 0.1)]
    axs[1, 0].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[1, 0].set_xscale("log")

    A_2 = dA_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(A_2 >= 0.1)]
    y = A_2[np.where(A_2 >= 0.1)]
    axs[1, 0].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    A_3 = dA_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(A_3 >= 0.1)]
    y = A_3[np.where(A_3 >= 0.1)]
    axs[1, 0].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')


    A_4 = dA_dlnd(coarse[0], coarse[1], coarse[2], diameters)
    x = diameters[np.where(A_4 >= 0.1)]
    y = A_4[np.where(A_4 >= 0.1)]
    axs[1, 0].plot(x, y, linestyle='dashed', linewidth=1.5, c='black')
    
    A_5 = dA_dlnd(super_coarse[0], super_coarse[1], super_coarse[2], diameters)
    x = diameters[np.where(A_5 >= 0.1)]
    y = A_5[np.where(A_5 >= 0.1)]
    axs[1, 0].plot(x, y, linestyle='dashdot', linewidth=1.5, c='black')

    axs[1,0].arrow(x=200, y=190, dx=1000, dy=0, width=8, color='black', alpha=0.8, shape='right')

    axs[1,0].set_xlim(1, 20000)
    axs[1,0].set_ylim(0, 250)
    axs[1,0].set_ylabel("dA/dlog $\it{d}$ / $um^{2}$ $cm^{-3}$")
    axs[1,0].text(140, 210, "Light scattering", size=13)
    axs[1,0].text(1.5, 200, "Surface area", size=13)


     # figure 4.2 (row 2 col 2)
    A_1 = dA_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(A_1 >= 0.1)]
    y = A_1[np.where(A_1 >= 0.1)]
    axs[1, 1].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[1, 1].set_xscale("log")
    axs[1, 1].set_yscale("log")

    A_2 = dA_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(A_2 >= 0.1)]
    y = A_2[np.where(A_2 >= 0.1)]
    axs[1, 1].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    A_3 = dA_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(A_3 >= 0.1)]
    y = A_3[np.where(A_3 >= 0.1)]
    axs[1, 1].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')


    A_4 = dA_dlnd(coarse[0], coarse[1], coarse[2], diameters)
    x = diameters[np.where(A_4 >= 0.1)]
    y = A_4[np.where(A_4 >= 0.1)]
    axs[1, 1].plot(x, y, linestyle='dashed', linewidth=1.5, c='black')

    A_5 = dA_dlnd(super_coarse[0], super_coarse[1], super_coarse[2], diameters)
    x = diameters[np.where(A_5 >= 0.1)]
    y = A_5[np.where(A_5 >= 0.1)]
    axs[1, 1].plot(x, y, linestyle='dashdot', linewidth=1.5, c='black')

    axs[1, 1].set_xlim(1, 20000)
    axs[1, 1].set_ylim(0.1, 1000)
    axs[1, 1].set_ylabel("dA/dlog $\it{d}$ / $um^{2}$ $cm^{-3}$")
    axs[1, 1].text(1.5, 1, "Nucleation", size=10)
    axs[1, 1].text(20, 50, "Aitken", size=10)
    axs[1, 1].text(100, 220, "Accumulation", size=10)
    axs[1, 1].text(300, 7, "Coarse", size=10)
    axs[1, 1].text(2300, 25, "Super-coarse", size=10)

    
    # figure 4.2 (row 3 col 1)
    V_1 = dV_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(V_1 >= 0.1)]
    y = V_1[np.where(V_1 >= 0.1)]
    axs[2, 0].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[2, 0].set_xscale("log")

    V_2 = dV_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(V_2 >= 0.1)]
    y = V_2[np.where(V_2 >= 0.1)]
    axs[2, 0].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    V_3 = dV_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(V_3 >= 0.1)]
    y = V_3[np.where(V_3 >= 0.1)]
    axs[2, 0].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')


    V_4 = dV_dlnd(coarse[0], coarse[1], coarse[2], diameters)
    x = diameters[np.where(V_4 >= 0.1)]
    y = V_4[np.where(V_4 >= 0.1)]
    axs[2, 0].plot(x, y, linestyle='dashed', linewidth=1.5, c='black')

    V_5 = dV_dlnd(super_coarse[0], super_coarse[1], super_coarse[2], diameters)
    x = diameters[np.where(V_5 >= 0.1)]
    y = V_5[np.where(V_5 >= 0.1)]
    axs[2, 0].plot(x, y, linestyle='dashdot', linewidth=1.5, c='black')

    axs[2,0].set_xlabel("Diameter, $\it{d}$ (nm)")
    axs[2,0].set_xlim(1, 20000)
    axs[2,0].set_ylim(0, 60)
    axs[2,0].set_ylabel("dV/dlog $\it{d}$ / $um^{3}$ $cm^{-3}$") 
    axs[2,0].text(1.5, 50, "Volume", size=13)

    # figure 4.2 (row 3 col 2)
    V_1 = dV_dlnd(nucleation[0], nucleation[1], nucleation[2], diameters)
    x = diameters[np.where(V_1 >= 0.01)]
    y = V_1[np.where(V_1 >= 0.01)]
    axs[2, 1].plot(x, y, linestyle='solid', linewidth=1.0, c='black')
    axs[2, 1].set_xscale("log")
    axs[2, 1].set_yscale("log")

    V_2 = dV_dlnd(aitken[0], aitken[1], aitken[2], diameters)
    x = diameters[np.where(V_2 >= 0.01)]
    y = V_2[np.where(V_2 >= 0.01)]
    axs[2, 1].plot(x, y, linestyle='solid', linewidth=1.5, c='black')

    V_3 = dV_dlnd(accumulation[0], accumulation[1], accumulation[2], diameters)
    x = diameters[np.where(V_3 >= 0.01)]
    y = V_3[np.where(V_3 >= 0.01)]
    axs[2, 1].plot(x, y, linestyle='dashed', linewidth=1.0, c='black')


    V_4 = dV_dlnd(coarse[0], coarse[1], coarse[2], diameters)
    x = diameters[np.where(V_4 >= 0.01)]
    y = V_4[np.where(V_4 >= 0.01)]
    axs[2, 1].plot(x, y, linestyle='dashed', linewidth=1.5, c='black')

    V_5 = dV_dlnd(super_coarse[0], super_coarse[1], super_coarse[2], diameters)
    x = diameters[np.where(V_5 >= 0.01)]
    y = V_5[np.where(V_5 >= 0.01)]
    axs[2, 1].plot(x, y, linestyle='dashdot', linewidth=1.5, c='black')

    axs[2, 1].set_xlabel("Diameter, $\it{d}$ (nm)")
    axs[2, 1].set_xlim(1, 20000)
    axs[2, 1].set_ylim(0.01, 100)
    axs[2, 1].set_ylabel("dV/dlog $\it{d}$ / $um^{3}$ $cm^{-3}$") 
    plt.show()


if __name__ == "__main__":
    graph()
