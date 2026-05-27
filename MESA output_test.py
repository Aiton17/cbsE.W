import matplotlib.pyplot as plt
import numpy as np
import mesa_reader as mr

# load entire LOG directory information
l = mr.MesaLogDir('./LOGS')
# grab the last profile
p = l.profile_data()

# this works even if you only have logRho and logT!
plt.loglog(p.Rho, p.T)
plt.xlabel("Density")
plt.ylabel("Temperature")
plt.show()  # Display the plot