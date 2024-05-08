from game_logic import *

def execute():
    
    win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    clock = pygame.time.Clock()
    base = Base(730)
    pipes = [Pipe(450)]
    bird = Bird(230,350)
    score = 0
    run = True

    while(run):
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                    quit()
            if event.type == pygame.KEYDOWN:
                bird.jump()

        bird.move()
        base.move()
        rem = []
        add_pipe = False

        for pipe in pipes:
            pipe.move()
            if pipe.collide(bird):
                run = False
                break

            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True

            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                rem.append(pipe)

        if bird.y + bird.img.get_height() > 730 or bird.y < 0:
            run = False
            break

        if add_pipe:
            score += 1
            pipes.append(Pipe(600))
        for r in rem:
            pipes.remove(r)

        draw_window(win, [bird], pipes, base, score)
    return score

