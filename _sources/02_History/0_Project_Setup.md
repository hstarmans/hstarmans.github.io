# History
The project starts with the assumption that it is not possible to get a laser grid. There are ways around this, e.g. laser with a DMD device. There is also research into nano-lasers; which could possible form a laser led screen. All these technologies have their limitations, due to cooling, diffraction or focusing of the laser. A way around this is moving the laser bundle either by mirrors or prisms.
Rotating prisms have a lower cross-scan error and require simpler optics than rotating mirrors.
The initial idea of using prism for laser scanning originates from Dr. Jacobus Jamar and was developed at [TNO](https://www.tno.nl).
The Netherlands is especially interested in lithography due to the regional importance of [ASML](https://www.asml.com).
This first system moves a plurality of laser bundles with a thicker prism under an angle, see [US10114289B2](https://patents.google.com/patent/US10114289B2)
The original system is shown below;
```{image} ../images/LDI_systems_ED600px.jpg
:alt: no scanner showing
:class: bg-primary mb-1
:width: 300px
:align: center
```
The patent has a loop hole as claim one specifies a plurality or more than one bundle is moved by a prism.
Rik Starmans realized a single laser bundle per prism would make the system more cost-effective.
Luckily, [Henner Zeller](https://github.com/hzeller/ldgraphy) had a already developed an open-hardware laser scanner for a rotating mirror.
This system was used to create a proof of concept version on the [beaglebone](https://github.com/hstarmans/ldgraphy).
Rik Starmans won 3000 USD in the Hackaday Prize 2019 using the [system](https://youtu.be/SofTXG5s_MA).
A microcontroller was however seen as too limiting for further development.
The system therefore moved to [Nmigen](https://github.com/nmigen/nmigen) and uses some components from [luna](https://github.com/greatscottgadgets/luna).