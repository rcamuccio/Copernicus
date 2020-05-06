# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copernicus - Planet class

Version 1.0.0 - 19 Apr 2020
	Added planet class

Version 1.1.0 - 6 May 2020
	Added star class

"""

__author__ = "Richard Camuccio"
__version__ = "1.1.0"

import math

class Planet:

	def __init__(self):

		# Identification parameters
		self.__name = "unknown"
		
		# Bulk parameters
		self.__bond_albedo = 0
		self.__density = 0
		self.__escape_velocity = 0
		self.__flattening = 0
		self.__geometric_albedo = 0
		self.__mass = 0
		self.__moment_of_inertia_factor = 0
		self.__radius = 0
		self.__rotation_period = 0
		self.__surface_area = 0		
		self.__surface_gravity = 0
		self.__surface_temperature = 0
		self.__volume = 0

		# Orbital parameters
		self.__aphelion = 0
		self.__argument_of_perihelion = 0
		self.__eccentricity = 0
		self.__inclination = 0
		self.__longitude_of_ascending_node = 0
		self.__mean_anomaly = 0
		self.__obliquity = 0
		self.__orbital_period = 0
		self.__orbital_speed = 0
		self.__perihelion = 0
		self.__semimajor_axis = 0

		# Satellite parameters
		self.__satellites = []

		# Coordinate parameters
		self.__x = 0
		self.__y = 0
		self.__x_velocity = 0
		self.__y_velocity = 0

	# Identification parameter methods
	def __str__(self):
		return self.__name

	def get_name(self):
		return self.__name

	def set_name(self, name):
		self.__name = name

	# Bulk parameter methods
	def get_bond_albedo(self):
		return self.__bond_albedo

	def set_bond_albedo(self, bond_albedo):
		self.__bond_albedo = bond_albedo

	def get_circumference(self):
		circumference = 2 * math.pi * self.__radius
		return circumference

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

	def get_geometric_albedo(self):
		return self.__geometric_albedo

	def set_geometric_albedo(self, geometric_albedo):
		self.__geometric_albedo = geometric_albedo

	def get_mass(self):
		return self.__mass

	def set_mass(self, mass):
		self.__mass = mass

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
	def get_aphelion(self):
		return self.__aphelion

	def set_aphelion(self, aphelion):
		self.__aphelion = aphelion

	def get_argument_of_perihelion(self):
		return self.__argument_of_perihelion

	def set_argument_of_perihelion(self, argument_of_perihelion):
		self.__argument_of_perihelion = argument_of_perihelion

	def get_eccentricity(self):
		return self.__eccentricity

	def set_eccentricity(self, eccentricity):
		self.__eccentricity = eccentricity

	def get_inclination(self):
		return self.__inclination

	def set_inclination(self, inclination):
		self.__inclination = inclination

	def get_longitude_of_ascending_node(self):
		return self.__longitude_of_ascending_node

	def set_longitude_of_ascending_node(self, longitude_of_ascending_node):
		self.__longitude_of_ascending_node = longitude_of_ascending_node

	def get_mean_anomaly(self):
		return self.__mean_anomaly

	def set_mean_anomaly(self, mean_anomaly):
		self.__mean_anomaly = mean_anomaly

	def get_obliquity(self):
		return self.__obliquity

	def set_obliquity(self, obliquity):
		self.__obliquity = obliquity

	def get_orbital_period(self):
		return self.__orbital_period

	def set_orbital_period(self, orbital_period):
		self.__orbital_speed = orbital_period

	def get_orbital_speed(self):
		return self.__orbital_speed

	def set_orbital_speed(self, orbital_speed):
		self.__orbital_speed = orbital_speed

	def get_perihelion(self):
		return self.__perihelion

	def set_perihelion(self, perihelion):
		self.__perihelion = perihelion

	def get_semimajor_axis(self):
		return self.__semimajor_axis

	def set_semimajor_axis(self, semimajor_axis):
		self.__semimajor_axis = semimajor_axis
	
	# Satellite parameter methods
	def get_satellite_system(self):
		return self.__satellites

	def set_satellite_system(self, satellites):
		self.__satellites = satellites

	def add_satellite(self, satellite):
		self.__satellites.append(satellite)

	# Coordinate parameter methods
	def get_x_position(self):
		return self.__x

	def set_x_position(self, x):
		self.__x = x

	def get_y_position(self):
		return self.__y

	def set_y_position(self, y):
		self.__y = y

	def move_to(self, x, y):
		self.__x = x
		self.__y = y

	def get_x_velocity(self):
		return self.__x_velocity

	def set_x_velocity(self, x_velocity):
		self.__x_velocity = x_velocity

	def get_y_velocity(self):
		return self.__y_velocity

	def set_y_velocity(self, y_velocity):
		self.__y_velocity = y_velocity

if __name__ == "__main__":

	# Example planet
	earth = Planet()

	earth.set_bond_albedo(0.306)
	earth.set_density(5514) # kg/m^3
	earth.set_escape_velocity(11186) # m/s
	earth.set_flattening(0.0033528)
	earth.set_geometric_albedo(0.367)
	earth.set_mass(5.97237e+24) # kg
	earth.set_moment_of_inertia_factor(0.3307)
	earth.set_radius(6371000) # m
	earth.set_rotation_period(86164.100352)	# s
	earth.set_surface_area(5.10072000e+14) # m^2
	earth.set_surface_gravity(9.80665) # m/s^2
	earth.set_surface_temperature(287.16) # K
	earth.set_volume(1.08321e+21) # m^3

	earth.set_aphelion(1.521e+11) # m
	earth.set_argument_of_perihelion(114.20783) # deg
	earth.set_eccentricity(0.0167086)
	earth.set_inclination(0.00005) # deg to J2000 ecliptic
	earth.set_longitude_of_ascending_node(-11.26064) # deg to J2000 ecliptic
	earth.set_mean_anomaly(358.617)	# deg
	earth.set_obliquity(23.4392811)	# deg to ecliptic
	earth.set_orbital_period(31558149.7635456) # s
	earth.set_orbital_speed(29780) # m/s
	earth.set_perihelion(1.47095e+11) # m
	earth.set_semimajor_axis(1.49598023e+11) # m

	earth.set_name("Earth")
	name = earth.get_name()
	print(" Planet: Earth")

	print()
	print("--- BULK PARAMETERS ---")

	bond_albedo = earth.get_bond_albedo()
	print(" Bond albedo:", bond_albedo)

	circumference = earth.get_circumference()
	print(" Circumference:", circumference)

	density = earth.get_density()
	print(" Density:", density)

	escape_velocity = earth.get_escape_velocity()
	print(" Escape velocity:", escape_velocity)

	flattening = earth.get_flattening()
	print(" Flattening:", flattening)

	geometric_albedo = earth.get_geometric_albedo()
	print(" Geometric albedo:", geometric_albedo)

	mass = earth.get_mass()
	print(" Mass:", mass)

	moment_of_inertia_factor = earth.get_moment_of_inertia_factor()
	print(" Moment of inertia factor:", moment_of_inertia_factor)

	radius = earth.get_radius()
	print(" Radius:", radius)

	rotation_period = earth.get_rotation_period()
	print(" Rotation period:", rotation_period)

	standard_gravitational_parameter = earth.get_standard_gravitational_parameter()
	print(" Standard gravitational parameter:", standard_gravitational_parameter)

	surface_area = earth.get_surface_area()
	print(" Surface area:", surface_area)

	surface_gravity = earth.get_surface_gravity()
	print(" Surface gravity:", surface_gravity)

	surface_temperature = earth.get_surface_temperature()
	print(" Surface temperature:", surface_temperature)

	volume = earth.get_volume()
	print(" Volume:", volume)

	print()
	print("--- ORBITAL PARAMETERS ---")

	aphelion = earth.get_aphelion()
	print(" Aphelion:", aphelion)

	argument_of_perihelion = earth.get_argument_of_perihelion()
	print(" Argument of perihelion:", argument_of_perihelion)

	eccentricity = earth.get_eccentricity()
	print(" Eccentricity:", eccentricity)

	inclination = earth.get_inclination()
	print(" Inclination:", inclination)

	longitude_of_ascending_node = earth.get_longitude_of_ascending_node()
	print(" Longitude of ascending node:", longitude_of_ascending_node)

	mean_anomaly = earth.get_mean_anomaly()
	print(" Mean anomaly:", mean_anomaly)

	obliquity = earth.get_obliquity()
	print(" Obliquity:", obliquity)

	orbital_period = earth.get_orbital_period()
	print(" Orbital period:", orbital_period)

	orbital_speed = earth.get_orbital_speed()
	print(" Orbital speed:", orbital_speed)

	perihelion = earth.get_perihelion()
	print(" Perihelion:", perihelion)

	semimajor_axis = earth.get_semimajor_axis()
	print(" Semimajor axis:", semimajor_axis)

	print()
	print("--- SATELLITE PARAMETERS ---")

	# Test satellite methods
	satellite_system = []
	earth.set_satellite_system(satellite_system)
	earth.add_satellite("Moon")

	satellites = earth.get_satellite_system()
	print(" Satellites:", len(satellites), satellites)