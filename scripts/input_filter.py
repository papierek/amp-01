## lets do some spice
import numpy as np
import matplotlib.pyplot as plt

import PySpice.Logging.Logging as logging

logger = logging.setup_logging()

from PySpice.Spice.Netlist import Circuit
from PySpice.Unit.Units import kilo, micro, mega
from PySpice.Plot.BodeDiagram import bode_diagram

cir = Circuit("Input filter")
cir.R('f', 'in', 'out', kilo(1))

cir.C('f', 'out', cir.gnd, micro(1))
cir.Sinusoidal("input", 'in', cir.gnd, amplitude=1)

simulator = cir.simulator(temperature=25, nominal_temperature=25)
analysis = simulator.ac(start_frequency=1, stop_frequency=mega(1), number_of_points=10,  variation='dec')


figure = plt.figure(1, (20, 10))
plt.title("Bode Diagram of a Low-Pass RC Filter")
bode_diagram(axes=(plt.subplot(211), plt.subplot(212)),
             frequency=analysis.frequency,
             gain=20*np.log10(np.absolute(analysis.out)),
             phase=np.angle(analysis.out, deg=False),
             marker='.',
             color='blue',
             linestyle='-',
         )
plt.tight_layout()
plt.show()
