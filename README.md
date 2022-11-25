# Sistema-Solar
Cria um mini sistema solar personalizavel, sem físicas realistas, usando PyGame.

![Screenshot_1478](https://user-images.githubusercontent.com/44853524/204062042-dd014192-5801-4d92-a257-4a70d51c75ec.png)

## Usage

```py

#Cria o espaço com a taxa de atualização de 60 frames por segundo
space = Space(fps=60)

#Seta o tamanho do espaço para 1000px de largura e 950px de altura, com a cor de fundo preto
space.config(size=(1000,950), color=(0,0,0))


#Cria o planeta chamado "Earth", com o raio de 6.3px, com a orbita de 162px, com a velocidade de 3px por frame, e com a cor azul 
space.create_planet(name="Earth",
                    planet_radius=6.3,
                    orbit_radius=162,
                    velocity = 3.0,
                    color=(47, 106, 105)) 

```
