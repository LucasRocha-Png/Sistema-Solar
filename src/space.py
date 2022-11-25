"""
Created by: Lucas Rocha

At: 25/11/2022 - 13:12
"""

class Space:
    """
    Create an space object, that can accept planets
    """

    
    #Pre configurate our universe if we dont set the configurations
    def __init__(self) -> None:    
        self.x = 1000
        self.y = 600

        self.color = (0,0,0)

    # Methods to configurate our universe -=-=-=-=-=-=-=-=-=-=-=
    def size(self, x:int, y:int) -> None:
        self.x = x
        self.y = y
    
    def color(self, rgb_tuple:tuple) -> None:
        if len(rgb_tuple) != 3:
            raise Exception("RGB tuple must have 3 int values")
        
        for value in rgb_tuple:
            if type(value) != int or value < 0 or value > 255:
                raise ValueError("The value must be a int between 0-255")
                
        self.color = rgb_tuple         
    #-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
    
    def create_universe(self) -> None:
        import pygame
    
        pygame.init()
        screen = pygame.display.set_mode((self.x, self.y))
        pygame.display.set_caption("Universe")
        
        running = True
        while running:
            screen.fill(self.color)
            
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    running = False

            pygame.display.update()     
        
        
        
        
        
        
        
        
        
        
        
    