import pygame

pygame.init()

j = pygame.joystick.Joystick(0)
j.init()

try:
    while True:
        events = pygame.event.get()
        for event in events:
            #if event.type == pygame.JOYAXISMOTION:
            #    print(event.dict, event.joy, event.axis, event.value)
            #elif event.type == pygame.JOYBALLMOTION:
            #    print(event.dict, event.joy, event.ball, event.rel)
            #elif event.type == pygame.JOYBUTTONDOWN:
            #    print(event.dict, event.joy, event.button, 'pressed')
            #elif event.type == pygame.JOYBUTTONUP:
            #    print(event.dict, event.joy, event.button, 'released')
            #elif event.type == pygame.JOYHATMOTION:
            #    print(event.dict, event.joy, event.hat, event.value)
            if event.type == pygame.JOYBUTTONDOWN:
                print("Button Pressed")
                if j.get_button(0):
                    print("SQUARE")
                elif j.get_button(1):
                    print("X")
                elif j.get_button(2):
                    print("CIRCLE")
                elif j.get_button(3):
                    print("TRIANGLE")
                elif j.get_button(4):
                    print("L1")
                elif j.get_button(5):
                    print("R1")
                elif j.get_button(6):
                    print("L2")
                    # Control Left Motor using L2
                elif j.get_button(7):
                    # Control Right Motor using R2
                    print("R2")
except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()