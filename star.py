# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copernicus - Star class

Version 1.0.0 - 19 Apr 2020
	Added planet class

Version 1.1.0 - 6 May 2020
	Added star class

"""

__author__ = "Richard Camuccio"
__version__ = "1.1.0"

import math

class Star:

	def __init__(self):

		# Identification parameters
		self.__luminosity_class = "unknown"
		self.__name = "unknown"
		self.__spectral_type = "unknown"

		# Bulk parameters
		self.__circumference = 0
		self.__core_density = 0
		self.__core_temperature = 0
		self.__corona_temperature = 0
		self.__density = 0
		self.__escape_velocity = 0
		self.__flattening = 0
		self.__luminosity = 0
		self.__mass = 0
		self.__metallicity = 0
		self.__moment_of_inertia_factor = 0
		self.__radius = 0
		self.__rotation_period = 0
		self.__surface_area = 0
		self.__surface_gravity = 0
		self.__surface_temperature = 0
		self.__volume = 0

		# Orbital parameters
		self.__obliquity = 0

		# Coordinate parameters
		self.__x = 0
		self.__y = 0

	# Identification parameter methods
	def __str__(self):
		return self.__name

	def get_luminosity_class(self):
		return self.__luminosity_class

	def set_luminosity_class(self, luminosity_class):
		self.__luminosity_class = luminosity_class

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	def get_spectral_type(self):
		return self.__spectral_type

	def set_spectral_type(self, spectral_type):
		self.__spectral_type = spectral_type

	# Bulk parameter methods
	def get_circumference(self):
		return self.__circumference

	def set_circumference(self, circumference):
		self.__circumference = circumference

	def get_core_density(self):
		return self.__core_density

	def set_core_density(self, core_density):
		self.__core_density = core_density

	def get_core_temperature(self):
		return self.__core_temperature

	def set_core_temperature(self, core_temperature):
		self.__core_temperature = core_temperature

	def get_corona_temperature(self):
		return self.__corona_temperature

	def set_corona_temperature(self, corona_temperature):
		self.__corona_temperature = corona_temperature

	def get_density(self):
		return self.__density

	def set_density(self, density):
		self.__density = density

	def get_escape_velocity(self):
		return self.__escape_velocity

	def set_escape_velocity(self, escape_velocity):
		self.__escape_velocity = escape_velocity

	def get_flattening(self):
		return self.__flattening

	def set_flattening(self, flattening):
		self.__flattening = flattening

	def get_luminosity(self):
		return self.__luminosity

	def set_luminosity(self, luminosity):
		self.__luminosity = luminosity

	def get_mass(self):
		return self.__mass

	def set_mass(self, mass):
		self.__mass = mass

	def get_metallicity(self):
		return self.__metallicity

	def set_metallicity(self, metallicity):
		self.__metallicity = metallicity

	def get_moment_of_inertia_factor(self):
		return self.__moment_of_inertia_factor

	def set_moment_of_inertia_factor(self, moment_of_inertia_factor):
		self.__moment_of_inertia_factor = moment_of_inertia_factor

	def get_radius(self):
		return self.__radius

	def set_radius(self, radius):
		self.__radius = radius

	def get_rotation_period(self):
		return self.__rotation_period

	def set_rotation_period(self, rotation_period):
		self.__rotation_period = rotation_period

	def get_standard_gravitational_parameter(self):
		mu = 6.6743e-11 * self.__mass
		return mu

	def get_surface_area(self):
		return self.__surface_area

	def set_surface_area(self, surface_area):
		self.__surface_area = surface_area

	def get_surface_gravity(self):
		return self.__surface_gravity

	def set_surface_gravity(self, surface_gravity):
		self.__surface_gravity = surface_gravity

	def get_surface_temperature(self):
		return self.__surface_temperature

	def set_surface_temperature(self, surface_temperature):
		self.__surface_temperature = surface_temperature

	def get_volume(self):
		return self.__volume

	def set_volume(self, volume):
		self.__volume = volume

	# Orbital parameter methods
	def get_obliquity(self):
		return self.__obliquity

	def set_obliquity(self, obliquity):
		self.__obliquity = obliquity

	# Coordinate parameter methods
	def get_x_position(self):
		return self.__x

	def get_y_position(self):
		return self.__y

if __name__ == "__main__":

	# Example star
	sun = Star()

	sun.set_circumference(4.379e+06) # km
	sun.set_core_density(162.2) # g/cm^3
	sun.set_core_temperature(1.57e+07) # K
	sun.set_corona_temperature(5e+06) # K
	sun.set_density(1.408) # g/cm^3
	sun.set_escape_velocity(617.7) # km/s
	sun.set_flattening(9e-06)
	sun.set_luminosity(3.828e26) # W
	sun.set_mass(1.9884e+30) # kg
	sun.set_metallicity(0.0122)
	sun.set_moment_of_inertia_factor(0.070)
	sun.set_radius(69)
	sun.set_rotation_period(25.05) # d
	sun.set_surface_area(6.09e+12) # km^2
	sun.set_surface_gravity(274) # m/s^2
	sun.set_surface_temperature(5772) # K
	sun.set_volume(1.41e+18) # km^3

	sun.set_obliquity(7.25) # deg to ecliptic

	sun.set_luminosity_class("V")
	sun.set_name("Sol")
	sun.set_spectral_type("G2")

	name = sun.get_name()
	print(" Star: Sol")

	spectral_type = sun.get_spectral_type()
	print(" Spectral type:", spectral_type)

	luminosity_class = sun.get_luminosity_class()
	print(" Luminosity class:", luminosity_class)

	print()
	print("--- BULK PARAMETERS ---")

	circumference = sun.get_circumference()
	print(" Circumference:", circumference)

	core_density = sun.get_core_density()
	print(" Core density:", core_density)

	core_temperature = sun.get_core_temperature()
	print(" Core temperature:", core_temperature)

	corona_temperature = sun.get_corona_temperature()
	print(" Corona temperature:", corona_temperature)

	density = sun.get_density()
	print(" Density:", density)

	escape_velocity = sun.get_escape_velocity()
	print(" Escape velocity:", escape_velocity)

	flattening = sun.get_flattening()
	print(" Flattening:", flattening)

	luminosity = sun.get_luminosity()
	print(" Luminosity:", luminosity)

	mass = sun.get_mass()
	print(" Mass:", mass)

	metallicity = sun.get_metallicity()
	print(" Metallicity:", metallicity)

	moment_of_inertia_factor = sun.get_moment_of_inertia_factor()
	print(" Moment of inertia factor:", moment_of_inertia_factor)

	radius = sun.get_radius()
	print(" Radius:", radius)

	rotation_period = sun.get_rotation_period()
	print(" Rotation period:", rotation_period)

	surface_area = sun.get_surface_area()
	print(" Surface area:", surface_area)

	surface_gravity = sun.get_surface_gravity()
	print(" Surface gravity:", surface_gravity)

	surface_temperature = sun.get_surface_temperature()
	print(" Surface temperature:", surface_temperature)

	volume = sun.get_volume()
	print(" Volume:", volume)

	print()
	print("--- ORBITAL PARAMETERS ---")

	obliquity = sun.get_obliquity()
	print(" Obliquity:", obliquity)