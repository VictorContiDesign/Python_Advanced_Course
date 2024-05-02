import matplotlib.pyplot as plt
from basemap import Basemap

# Crear la figura y los ejes
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(1, 1, 1)

# Crear el mapa
mapa = Basemap(projection='merc', 
               resolution='l', 
               area_thresh=1000.0, 
               llcrnrlon=-5.0, llcrnrlat=41.0, 
               urcrnrlon=10.0, urcrnrlat=52.0)

# Dibujar la costa, las fronteras y los países
mapa.drawcoastlines(linewidth=0.5)
mapa.drawcountries(linewidth=0.5)
mapa.drawstates(linewidth=0.2)

# Dibujar Francia
mapa.readshapefile('shapefiles/FRA_adm1', 'FRA_adm1', linewidth=0.5, color='gray')

# Mostrar el mapa
plt.show()