import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

photonE, abs_coeff = np.loadtxt('hw2.txt', unpack=True)

def Lorentz_line(omega_in, omega_resonance, FWHM):
    return FWHM / ((omega_in - omega_resonance)**2 + (FWHM/2)**2)

fittedLL = curve_fit(Lorentz_line, photonE, abs_coeff)

x_fit = np.linspace(1.02, 1.035, 1000)
y_fit = Lorentz_line(x_fit, fittedLL[0][0], fittedLL[0][1])

print(f"Scipy's curvefit found the resonance frequency as {fittedLL[0][0]} eV and the FWHM as {fittedLL[0][1]} eV.")
#print(fittedLL)
      

plt.scatter(photonE, abs_coeff, s=5)
plt.plot(x_fit, y_fit, c='magenta')
plt.xlabel("Photon Energy (eV)")
plt.ylabel("Absorption Coefficient (a.u.)")
plt.title("Lorentzian Lineshape Fit for hw2.txt")

plt.savefig('HW2.png', dpi=500, bbox_inches='tight', pad_inches=0.4)