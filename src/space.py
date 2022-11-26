"""
Created by: Lucas Rocha

At: 25/11/2022 - 13:12

This file contains all the classes that create our universe
"""

if __name__ == "__main__":
    import pygame
    import math
    from exception_checkers import *
    
else:
    import pygame
    import math
    from src.exception_checkers import *


class Planet:
    """
    Create a planet
    """
    
    #Create the planet class init, that contains a dict containing the planet information
    def __init__(self):
        self.planets = {} #Id - configuration

        
    def create_planet(self, name:str, planet_radius, orbit_radius, velocity, color:int = (255,255,255)) -> None:
        #Checkers -
        str_checker(name, "Planet name")
        rgb_color_checker(color)
        #-
        
        self.planets[len(self.planets)] = {
                                           "Name": name,
                                           "Planet Radius": planet_radius,
                                           "Orbit Radius": orbit_radius,
                                           "Color": color,
                                           "Velocity": velocity,
                                           "x_pos": 0, #pre defined
                                           "y_os":0, #pre defined
                                           "Circule Orbit Radius": 0 #pre defined
                                           }

    #Make the function that plot the planets -=
    def update_planets_pos(self) -> None:
        for id_ in self.planets:
        
            #Calculate the velocity of the planet
            velocity = self.planets[id_]["Velocity"]
            orbit_radius = self.planets[id_]["Orbit Radius"]
            orbit_lenght = orbit_radius * math.pi * 2
            
            #Calculate how much the planet opening will be sum
            opening_sum = (velocity*360)/orbit_lenght
            #-------------------------------------
            
            self.planets[id_]["Circule Orbit Radius"] += opening_sum
            
            radius_opening = self.planets[id_]["Circule Orbit Radius"]
            rad_radius_opening = (self.planets[id_]["Circule Orbit Radius"] * math.pi)/180

            
            self.planets[id_]["x_pos"] = (math.cos(rad_radius_opening) * orbit_radius) + self.screen_x_center
            self.planets[id_]["y_pos"] = (math.sin(rad_radius_opening) * orbit_radius) + self.screen_y_center

        
    def plot_planets(self, screen) -> None:
        for id_ in self.planets:
            rgb_color = self.planets[id_]["Color"]
            planet_radius = self.planets[id_]["Planet Radius"]
            orbit_radius = self.planets[id_]["Orbit Radius"]
            x_pos = self.planets[id_]["x_pos"]
            y_pos = self.planets[id_]["y_pos"]
            
            #Plot the orbit
            pygame.draw.circle(screen, (255,255,255), (self.screen_x_center, self.screen_y_center), orbit_radius, 1) 
            
            #Plot the planet
            pygame.draw.circle(screen, rgb_color, (x_pos, y_pos), planet_radius, 0)
    
    def plot_planets_name(self, screen, textfont) -> None:
        for id_ in self.planets:
            nome = self.planets[id_]["Name"]
            rgb_color = self.planets[id_]["Color"]
            planet_radius = self.planets[id_]["Planet Radius"]
            x_pos = self.planets[id_]["x_pos"]
            y_pos = self.planets[id_]["y_pos"]

            #Plot the planet
            text = textfont.render(nome, True, rgb_color)
            screen.blit(text, (x_pos+(planet_radius), y_pos-(planet_radius)))


class Space(Planet):
    """
    Create a space object, that can accept planets
    """
    
    #Pre configurate our universe if we dont set the configurations
    def __init__(self, fps:int = 60) -> None:  
        super().__init__() 
        
        #Checkers -
        int_checker(fps, "FPS")
        #-
    
        #Screen
        self.x = 1000
        self.y = 600
        self.screen_x_center = self.x/2
        self.screen_y_center = self.y/2
        
        #Ticks
        self.fps = fps
        
        #background color
        self.background_color = (0,0,0)


    #Configurate our universe -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    def config(self, size:tuple, color:tuple = (0,0,0)) -> None:
        #Checkers -
        rgb_color_checker(color)
        pos_checker(size)
        #-        
    
        self.x = size[0]
        self.y = size[1]
        self.screen_x_center = self.x/2
        self.screen_y_center = self.y/2
        
                
        self.background_color = color 
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=    

    
    def create_universe(self) -> None:
        
        pygame.init()
        pygame.font.init()
        
        screen = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Universe")
        textfont = pygame.font.SysFont("Arial", 30)
        #--    
        running = True
        clock = pygame.time.Clock()
        while running:
            clock.tick(self.fps)
            screen.fill(self.background_color)
            
            #Plot the planets
            self.update_planets_pos()
            self.plot_planets(screen = screen)
            self.plot_planets_name(screen = screen, textfont = textfont)
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.update()     
        #--
        
        
        
        
        
        
        
        
        
        
    