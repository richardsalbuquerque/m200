import numpy as np
import pynbody
from sys import argv


'''
calculates the m200 of the galaxy cluster centered at the origin.

usage:

python3 m200.py snapshot
'''


snapshot = pynbody.load(f'{argv[1]}')

# Position in Mpc unit
x = snapshot['x']/1000
y = snapshot['y']/1000
z = snapshot['z']/1000
m = snapshot['mass']


h = 0.7
rhoc = 2.77e1 * h**2 # 1e10 M0/Mpc^3 (apostila do gastao)


nbins = 1000
rmax  = 1000
r1    = 0.005
bin   = np.log10(rmax/r1)/nbins
dcen  = np.sqrt(x**2 + y**2 + z**2)

for i in range(nbins):

    r2 = 10**( np.log10( r1 ) + bin ) 
    vol = ( 4/3 ) * np.pi * r2**3
    cond = np.where(dcen<r2)
    mass = np.sum(m[cond])
    rho  = mass/vol
    if rhoc > rho:
        print(f'm200 = {mass*1e10:.2e} Msun')
        break

    r1 = r2