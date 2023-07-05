# Johnswap-and-ITTC-Spectra-Calculation

In this repository, the wave spectrum obtained in different sea conditions has been calculated. Although the first figure given is the input screen of the GUI to be used, the converged results in Fig 2. are given. At the same time, it is shown in Fig 3. that the problem does not converge when the frequency interval is reduced.

Steps to Obtain Wave Spectra:
- Download and open the GUI.py file
- Determine your sea state and depend on your sea state put equivalent values for significant wave height(Hs) and zero crossing period(Tz)
- Determine your frequency range and number of intervals
- Determine your nondimensional peak shape parameter
- Click the calculate button

GUI:

![image](https://github.com/kaganbozali/Johnswap-and-ITTC-Spectra-Calculation/assets/104154215/64d3a3e6-97b9-4cbf-985d-4b7a2e7893f4)
                                              **Fig 1. Clear Screen View**

![image](https://github.com/kaganbozali/Johnswap-and-ITTC-Spectra-Calculation/assets/104154215/e6d4f7fe-b319-4327-a75d-2e20f7e8249f)
                                    **Fig 2. Results with Enough Intervals to Converge**

![image](https://github.com/kaganbozali/Johnswap-and-ITTC-Spectra-Calculation/assets/104154215/21f0db23-ed19-49ff-a1f0-6c4e8f62efcf)
                                        **Fig 3. Results with Convergence Issue**


Notes :

- A value other than 0 should be selected as the smallest frequency value. Otherwise, the value is infinite in obtaining the spectra and the result gives an error.
- You have must results if you performed analysis before and want to perform a new one
- In case of a change in sea condition, zero crossing period and significant wave height values should change.
