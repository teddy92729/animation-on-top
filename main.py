import pygame
import sys
import win32api
import win32con
import win32gui


pygame.init()

path="" if (len(sys.argv)<=1) else f"{sys.argv[1]}\\"
print(path)
with open(path+"conf.py","r") as conf:
    exec(conf.read())

animation=[pygame.image.load((path+filenameFormat)%(i+startFrameIndex)) for i in range(endFrameIndex-startFrameIndex+1)]
animation_index=-1
print("read %d photos"%len(animation))

screen = pygame.display.set_mode(size,pygame.NOFRAME|pygame.SRCALPHA)
clock = pygame.time.Clock()

# transparent  = (255, 255, 255)
if(transparent!=None):
    hwnd = pygame.display.get_wm_info()["window"]
    win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                        win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
    win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparent), 0, win32con.LWA_COLORKEY)
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, *win32gui.GetWindowRect(hwnd)[0:2],*size, 0)

running = True
frame = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                frame=not frame
                pygame.display.set_mode(size,(0 if frame else pygame.NOFRAME)|pygame.SRCALPHA)
                if(transparent!=None): 
                    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, *win32gui.GetWindowRect(hwnd)[0:2],*size, 0)
    if(transparent):
        screen.fill(transparent)
    animation_index=(animation_index+1)%len(animation)
    screen.blit(animation[animation_index],offset)
    clock.tick(fps)
    pygame.display.update()

pygame.quit()