import pygame
 
 
 
class Mouse(pygame.sprite.Sprite): 
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('mouse.png')
        self.rect = self.image.get_rect() 
 
 
 
 
class Udar(pygame.sprite.Sprite): 
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('udar2.png')
        self.rect = self.image.get_rect() 
 
 
 
 
class Maneken(pygame.sprite.Sprite): 
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('maneken.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.down_states = { 0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (128, 0, 64, 64), 3: (192, 0, 64, 64) }
 
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
 
    def handle_event(self, event):
        self.clip(self.down_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
  
  
  
        
class Fakel(pygame.sprite.Sprite): #ïðîñòî òåñòîâàÿ ïîñòîÿííàÿ àíèìàöèÿ
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('fakel.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.down_states = { 0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (128, 0, 64, 64), 3: (192, 0, 64, 64) , 4: (256, 0, 64, 64), 5: (320, 0, 64, 64), 6: (384, 0, 64, 64), 7: (448, 0, 64, 64) }
 
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
    
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
    
 
    def handle_event(self, event):
        self.clip(self.down_states)
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        



class Player(pygame.sprite.Sprite): #èãðîê
    def __init__(self, position):
        pygame.sprite.Sprite.__init__(self)
        self.sheet = pygame.image.load('player.png')
        self.sheet.set_clip(pygame.Rect(0, 0, 64, 64))
        self.image = self.sheet.subsurface(self.sheet.get_clip())
        self.rect = self.image.get_rect()
        self.rect.topleft = position
        self.frame = 0
        self.left_states = { 0: (0, 64, 64, 64), 1: (64, 64, 64, 64), 2: (128, 64, 64, 64), 3: (192, 64, 64, 64) }
        self.right_states = { 0: (0, 128, 64, 64), 1: (64, 128, 64, 64), 2: (128, 128, 64, 64), 3: (192, 128, 64, 64) }
        self.up_states = { 0: (0, 192, 64, 64), 1: (64, 192, 64, 64), 2: (128, 192, 64, 64), 3: (192, 192, 64, 64)  }
        self.down_states = { 0: (0, 0, 64, 64), 1: (64, 0, 64, 64), 2: (128, 0, 64, 64), 3: (192, 0, 64, 64) }
 
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
 
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
       
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            self.rect.y += 5
 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])
        self.image = self.sheet.subsurface(self.sheet.get_clip())
 
    def handle_event(self, event): 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')
 
 
pygame.init()
 
 
screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
player = Player((150, 150))
fakel = Fakel((100, 100))
mouse = Mouse((50, 50))
maneken = Maneken((350, 350))
udar = Udar((player.rect.x, player.rect.y))
 
 
fakel_test = pygame.sprite.Group()
fakel_test.add(maneken)
 
 
pygame.key.set_repeat(1,10)
 
 
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                    pass
        screen.fill(pygame.Color(0, 180, 160))
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            screen.blit(udar.image, udar.rect)
            if pygame.sprite.spritecollide(udar, fakel_test, False):
                maneken.handle_event(event)
 
           
        screen.blit(fakel.image, fakel.rect)
        screen.blit(maneken.image, maneken.rect)
        screen.blit(player.image, player.rect)
        fakel.handle_event(event)
        player.handle_event(event)
        screen.blit(mouse.image, mouse.rect)
 
        mouse_pos = pygame.mouse.get_pos()
        mouse.rect.x = mouse_pos[0]
        mouse.rect.y = mouse_pos[1]
 
        udar.rect.x = player.rect.x + 8
        udar.rect.y = player.rect.y - 32
        
        
        pygame.mouse.set_visible(0) 

        pygame.display.flip()              
        clock.tick(16)
 
pygame.quit ()