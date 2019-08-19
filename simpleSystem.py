#%%
import warnings
import numpy as np
import matplotlib.pyplot as plt

import rayopt as ro

plt.style.use('default')

# ignore matplotlib and numpy warning each other
warnings.simplefilter("ignore", FutureWarning)
# ignore floating point exceptions
np.seterr(divide="ignore", invalid="ignore")
# by default only print 4 significant digits
np.set_printoptions(precision=1)

#%%
s = ro.system_from_yaml("""
object:
  pupil:
    radius: 1
elements:
- {}
- {distance: 1, material: 1.5, roc: 5, radius: 1}
- {distance: .2, material: 1.0}
- {}
""")
s.update()
print(s)

#%%
lib = ro.Library.one()
for g in lib.session.query(
    ro.library.Material).filter(
    ro.library.Material.name.contains("N-BK7")):
    print(g.name, g.catalog.name, g.catalog.source)

#%%
s[1].material = lib.get("material", "SCHOTT-BK|N-BK7", source="rii")
s.object.angle = np.deg2rad(5)
s.fields = 0, 1., 0
s.update()
s.paraxial.resize()
s.resize_convex()
s.paraxial.refocus()
ro.Analysis(s)

#%%
