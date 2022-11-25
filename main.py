"""
Created by: Lucas Rocha

At: 25/11/2022 - 13:30

This is the main file to configurate our universe
"""

from src.space import Space


space = Space(fps=60)


space.config(size=(1000,950))

space.create_planet(name="Sun",
                    planet_radius=69,
                    orbit_radius=1,
                    velocity = 0,
                    color=(240, 239, 14))
                    
                    
space.create_planet(name="Venus",
                    planet_radius=6,
                    orbit_radius=136,
                    velocity = 3.5,
                    color=(230, 230, 230)) 

space.create_planet(name="Earth",
                    planet_radius=6.3,
                    orbit_radius=162,
                    velocity = 3.0,
                    color=(47, 106, 105))  

space.create_planet(name="Mars",
                    planet_radius=3.3,
                    orbit_radius=209,
                    velocity = 2.4,
                    color=(153, 61, 0)) 

space.create_planet(name="Jupiter",
                    planet_radius=69,
                    orbit_radius=300,
                    velocity = 1.3,
                    color=(176, 127, 53))    


               
space.create_universe()