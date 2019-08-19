#%%
import numpy as np
import matplotlib.pyplot as plt

from rayopt import *

np.set_printoptions(precision=3)
plt.style.use('default')


#%%
description = "oslo cooke triplet example 50mm f/4 20deg"
columns = "type roc distance radius material"
text = """
O 0       0     .364 AIR
S 21.25   5     6.5  SK16
S -158.65 2     6.5  AIR
S -20.25  6     5    F4
S 19.3    1     5    AIR
A 0       0     4.75 AIR
S 141.25  6     6.5  SK16
S -17.285 2     6.5  AIR
I 0       42.95 .364 AIR
"""

_description = "triplet 50mm f/4 20deg"
_columns = "type curvature distance radius material"
_text = """
O 0         0  .364 AIR
S .25285    5   1.8 1.62
S -.01474  .6   1.8 AIR
S -.1994 1.0654 1.3 1.621
S .25973  .15   1.3 AIR
A 0        .1   1.1 AIR
S .05065 1.0396 1.7 1.62
S -.24588  .6   1.7 AIR
I 0   8.27937     2 AIR
"""

_description = "photo triplet, f/2.7, f=100 U.S.-Pat 2,453,260 (1948-Pestrecov)"
_columns = "type distance roc diameter material"
_text = """
O 0      0   .25 AIR
S 20 40.94    20 1.617/55
S 8.74   0    20 AIR
S 11.05 -55.65 20 1.649/33.8
S 2.78 39.75  20 AIR
A 0      0    30 AIR
S 7.63 107.56 30 1.617/55
S 9.54 -43.33 30 AIR
I 79.34  0    30 AIR
"""

_description="cooke type triplet, USP 2453260 Pestrecov, Modern Optical Engineering, Smith"
_columns = "type roc distance radius material"
_text = """
    O      0     0   .3 AIR
    S  40.94    10   16 S-BSM9
    S      0  8.74   16 AIR
    S -55.65 10.05   14 S-TIM22
    A      0  2.78   12 S-TIM22
    S  39.75     0   14 AIR
    S 107.56  7.63 14.5 S-BSM9
    S -43.33  9.54 14.5 AIR
    I      0    90    0 AIR
"""

s = system_from_text(text, columns.split(),
    description=description)
s.object.angle = np.deg2rad(20)

s = system_from_yaml("""
description: "code v cooke triplet example 50mm f/4.5 20deg"
stop: 3
object: {angle_deg: 20, pupil: {radius: 5.55}}
elements:
- {material: air, radius: 10}
- {distance: 4, material: SCHOTT/SK16, roc: 21.48138, radius: 7}
- {distance: 2, material: air, roc: -124.1, radius: 7}
- {distance: 5.26, material: HOYA/F4, roc: -19.1, radius: 4.1}
- {distance: 1.25, material: air, roc: 22, radius: 4.1}
- {distance: 4.69, material: SCHOTT/SK16, roc: 328.9, radius: 7}
- {distance: 2.25, material: air, roc: -16.7, radius: 7}
- {distance: 43.050484, material: air}
""")

s = system_from_yaml("""
description: "smith triplet p444, 100mm f/8 23.4deg"
stop: 4
object: {angle_deg: 23.4, pupil: {radius: 6.25}}
elements:
- {material: air, radius: 20}
- {distance: 10, material: SCHOTT/SK4, roc: 40.1, radius: 17}
- {distance: 6, material: air, roc: -537.1, radius: 17}
- {distance: 10, material: SCHOTT/FN11, roc: -47.0, radius: 15}
- {distance: 1, material: air, roc: 40, radius: 15}
- {distance: 10.8, material: SCHOTT/SK4, roc: 234.5, radius: 16}
- {distance: 6, material: air, roc: -37.9, radius: 16}
- {distance: 85.3, material: air, radius: 45}
""")
s.update()
s.paraxial.focal_length_solve(100)
s.paraxial.update()
s.paraxial.refocus()

print(s)
#s.reverse()
#print(s)

#%%
a = Analysis(s, refocus_full=False)

#%%
