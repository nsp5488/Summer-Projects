import os
import neat
from game_logic import *


""" 
This class represents an implementation of the NEAT algorithm for playing flappy bird.
It includes the game loop so that we can easily draw multiple birds simultaneously.
"""
class NeatBird:

    """
    Initializes the algorithm.
    """
    def __init__(self, show):
        local_dir = os.path.dirname(__file__)
        config_path = os.path.join(local_dir, "config-feedforward.txt")

        self.config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction, 
                                    neat.DefaultSpeciesSet, neat.DefaultStagnation, 
                                    config_path)
        self.pop = neat.Population(self.config)

        self.pop.add_reporter(neat.StdOutReporter(True))
        self.stats = neat.StatisticsReporter()
        self.pop.add_reporter(self.stats)
        self.gens = 0
        self.show = show
        self.training = True

    """
    Executes training
    """
    def execute(self):
        winner = self.pop.run(self.__train, 50)
        return winner
    
    """
    Allows a single bird to replay.
    """
    def replay(self, genome):
        genomes = [(1,genome)]
        self.training = False
        self.__train(genomes, self.config)

    """
    NEAT fitness function.
    """
    def __train(self, genomes, config):
        nets = []
        ge = []
        birds = []
        self.gens += 1

        for _, g in genomes:
            net = neat.nn.FeedForwardNetwork.create(g, config)
            nets.append(net)
            birds.append(Bird(230,350))
            g.fitness = 0
            ge.append(g)


        if self.show:
            win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
            clock = pygame.time.Clock()
        base = Base(730)
        pipes = [Pipe(450)]
        score = 0
        run = True

        while run:
            if self.show:
                clock.tick(30)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        pygame.quit()
                        quit()
            
            pipe_ind = 0
            if len(birds) > 0: 
                if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():
                    pipe_ind = 1
            else:
                run = False
                continue

            for i, bird in enumerate(birds):
                bird.move()
                ge[i].fitness += .1

                output = nets[i].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))

                if output[0] > 0.5:
                    bird.jump()
            
            base.move()
            rem = []
            add_pipe = False
            for pipe in pipes:
                pipe.move()
                for i, bird in enumerate(birds):
                    if pipe.collide(bird):
                        ge[i].fitness -= 1
                        birds.pop(i)
                        nets.pop(i)
                        ge.pop(i)

                    if not pipe.passed and pipe.x < bird.x:
                        pipe.passed = True
                        add_pipe = True

                if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                    rem.append(pipe)

                
            if add_pipe:
                score += 1
                for g in ge:
                    g.fitness += 5
                pipes.append(Pipe(600))
            
            for r in rem:
                pipes.remove(r)
            
            for i, bird in enumerate(birds):
                if bird.y + bird.img.get_height() > 730 or bird.y < 0:
                    birds.pop(i)
                    ge.pop(i)
                    nets.pop(i)

            if score > 150 and self.training:
                break
            
            if self.show:
                draw_window(win, birds, pipes, base, score, self.gens)





if __name__ == '__main__':
    nb = NeatBird()
    nb.execute()
