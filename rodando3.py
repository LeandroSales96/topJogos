import pygame
import random

#cores
azul = (0,127,255)
preto = (0,0,0)
vermelho = (255,0,0)
cinza = (100,100,100)
branco = (255,255,255)

class Peixe(pygame.sprite.Sprite):

    def __init__(self,color,width,height):
        super().__init__()
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        self.rect = self.image.get_rect()

    def update(self):
        #move_peixe
        direcao = random.randrange(-2,2)
        if direcao == -1:
            self.rect.x -= 10
        elif direcao == 0:
            self.rect.y -= 10
        elif direcao == 1:
            self.rect.x += 10
        else:
            self.rect.y += 10
        
            
        #nao deixar passar dos limites de Y
        if self.rect.y > 641 | self.rect.y < 0:
            self.rect.y = 0
        elif self.rect.x > 641 | self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 641 & self.rect.y > 641:
            self.rect.x,self.rect.y = 0,0

class Tubarao(Peixe):

    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        

#def main():
#variaveis
pygame.init()
tela_width,tela_height =  640,640
tela = pygame.display.set_mode([640,640])
#new changes
block_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
for i in range(50):
    posicao_X = random.randrange(0,tela_width,10)
    posicao_Y = random.randrange(0,tela_height,10)
    peixe = Peixe(vermelho,10,10)
    peixe.rect.x = posicao_X
    peixe.rect.y = posicao_Y
    block_list.add(peixe)
    all_sprites_list.add(peixe)
        
#defincoes do game
pygame.display.set_caption("Jogo do tubarao")
relogio = pygame.time.Clock()
    
#objetos
grid = [[1]*8 for n in range(8)]
#tubarao = pygame.Rect(10,10,10,10)
#peixe = pygame.Rect(50,10,10,10)
tubarao = Tubarao(cinza,10,10)
all_sprites_list.add(tubarao)
    
    
    
    
sair = False

while sair != True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sair = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                tubarao = tubarao.move(10,0) 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tubarao = tubarao.move(-10,0)
                if event.key == pygame.K_RIGHT:
                    tubarao = tubarao.move(10,0)
                


        #fps        
        relogio.tick(10)
        
        #tabuleiro
        tela.fill(azul)
        x,y = 10,640
        for linha in grid:
            for coluna in linha:
                pygame.draw.line(tela, (0, 0, 0), (x,0), (x, y))
                pygame.draw.line(tela, (0, 0, 0), (0,x), (y, x))
                x += 10
                y += 10
                
        #tubarao sem sprite
        #if tubarao.colliderect(peixe):
         #   print("Houve colisao")
          #  tubarao.x = peixe.x
           # print("Tubarao comeu")
        #pygame.draw.rect(tela,cinza,tubarao)
        #pygame.draw.rect(tela,vermelho,peixe)

        #colisao
        all_sprites_list.update()
        blocks_hit_list = pygame.sprite.spritecollide(tubarao,block_list,False)
        for peixe in blocks_hit_list:  
            all_sprites_list.remove(peixe)
        
        
        
           
        #tela_on
        all_sprites_list.draw(tela)
        #pygame.display.update()
        pygame.display.flip()
 
        
pygame.quit()


#main()


