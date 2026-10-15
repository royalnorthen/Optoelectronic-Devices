import numpy as np
import matplotlib.pyplot as plt

# E_V(0) will be treated as zero in calculations since it's just an offset/constant

def E_V(gamma1, gamma2, gamma3, k, orientation):
    if orientation == 100:
        kx = k
        ky = 0
        kz = 0
    elif orientation == 110:
        kx = k / np.sqrt(2)
        ky = k / np.sqrt(2)
        kz = 0
    elif orientation == 111:
        kx = k / np.sqrt(3)
        ky = k / np.sqrt(3)
        kz = k / np.sqrt(3)
    plus_branch = (1 - gamma1)*k**2 + np.sqrt(4*(gamma2**2)*k**4 + 12*(gamma3**2 - gamma2**2)*((kx**2)*(ky**2) + (ky**2)*(kz**2) + (kz**2)*(kx**2)))
    minus_branch = (1 - gamma1)*k**2 - np.sqrt(4*(gamma2**2)*k**4 + 12*(gamma3**2 - gamma2**2)*((kx**2)*(ky**2) + (ky**2)*(kz**2) + (kz**2)*(kx**2)))

    # input k in units of nanometer^-1
    # these branches are in units of (hbar^2 / 2m0) per square nanometer, which is 0.0381 eV.  conversion below:
    plus_branch *= 0.0381
    minus_branch *= 0.0381
    
    return plus_branch, minus_branch

k_space = np.linspace(-1, 1, 1000)
E_100_plus, E_100_minus = E_V(5.04, 1.55, 2.4, k_space, 100)
E_110_plus, E_110_minus = E_V(5.04, 1.55, 2.4, k_space, 110)
E_111_plus, E_111_minus = E_V(5.04, 1.55, 2.4, k_space, 111)

# FOR PART 3c)

def second_derivative(f, x, h=1e-6):
    return (f(x + h) - 2 * f(x) + f(x - h)) / (h**2)

def Ek_100_HH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 100)
    return HH
def Ek_100_LH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 100)
    return LH
def Ek_110_HH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 110)
    return HH
def Ek_110_LH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 110)
    return LH
def Ek_111_HH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 111)
    return HH
def Ek_111_LH(k):
    HH, LH = E_V(5.04, 1.55, 2.4, k, 111)
    return LH

HH_100= second_derivative(Ek_100_HH, 0)
LH_100= second_derivative(Ek_100_LH, 0)
HH_110= second_derivative(Ek_110_HH, 0)
LH_110= second_derivative(Ek_110_LH, 0)
HH_111= second_derivative(Ek_111_HH, 0)
LH_111= second_derivative(Ek_111_LH, 0)

# the units here are eV * nm^2
print(f"HH_100 = {HH_100}")
print(f"LH_100 = {LH_100}")
print(f"HH_110 = {HH_110}")
print(f"LH_110 = {LH_110}")
print(f"HH_111 = {HH_111}")
print(f"LH_111 = {LH_111}")

# PLOTTING      

plt.plot(k_space, E_100_plus, c='black')
plt.plot(k_space, E_100_minus, c='black')
plt.xlabel(r"k ($nm^{-1}$)")
plt.ylabel("Energy (eV)")
plt.title("E vs k for heavy and light holes in [100] InP")

plt.savefig('HW3-3b-100.png', dpi=500, bbox_inches='tight', pad_inches=0.4)

plt.cla()

plt.plot(k_space, E_110_plus, c='black')
plt.plot(k_space, E_110_minus, c='black')
plt.xlabel(r"k ($nm^{-1}$)")
plt.ylabel("Energy (eV)")
plt.title("E vs k for heavy and light holes in [110] InP")

plt.savefig('HW3-3b-110.png', dpi=500, bbox_inches='tight', pad_inches=0.4)

plt.cla()

plt.plot(k_space, E_111_plus, c='black')
plt.plot(k_space, E_111_minus, c='black')
plt.xlabel(r"k ($nm^{-1}$)")
plt.ylabel("Energy (eV)")
plt.title("E vs k for heavy and light holes in [111] InP")

plt.savefig('HW3-3b-111.png', dpi=500, bbox_inches='tight', pad_inches=0.4)