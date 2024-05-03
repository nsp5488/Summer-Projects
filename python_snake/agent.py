import torch
import random
import numpy as np
from snake import SnakeGame, Direction, Point
from collections import deque
from model import Linear_DQN, QTrainer
from helper import plot

MAX_MEM = 100000
BATCH_SIZE = 1000
LR = .001

class Agent:
    
    def __init__(self):
        self.n_games = 0
        self.epsilon = 0
        self.gamma = 0.9
        self.memory = deque(maxlen=MAX_MEM)
        self.model = Linear_DQN(11, 256, 3)
        self.trainer = QTrainer(self.model, LR, self.gamma)


    def get_state(self, game):
        head = game.snake[0]
        danger_left = Point(head.x - 20, head.y)
        danger_right = Point(head.x + 20, head.y)
        danger_down = Point(head.x, head.y + 20)
        danger_up = Point(head.x, head.y - 20)
        dangers = [danger_left, danger_right, danger_down, danger_up]

        dir_left = game.direction == Direction.LEFT
        dir_right = game.direction == Direction.RIGHT
        dir_up = game.direction == Direction.DOWN
        dir_down = game.direction == Direction.UP
        directions = [dir_left, dir_right, dir_up, dir_down]

        straight_danger = 0
        left_danger = 0
        right_danger = 0

        for i in range(len(directions)):
            if directions[i] and game.is_collision(dangers[i]):
                straight_danger = 1
            right_i = (i + 1) % 4
            if directions[i] and game.is_collision(dangers[right_i]):
                right_danger = 1
            left_i = (i - 1) % 4
            if directions[i] and game.is_collision(dangers[left_i]):
                left_danger = 1
        
        food_l = game.food.x < head.x
        food_r = game.food.x > head.x
        food_u = game.food.y < head.y
        food_d = game.food.y > head.y

        state = [
            straight_danger, right_danger, left_danger, # Will die if a move is taken that has a 1
            dir_left, dir_right, dir_up, dir_down, # Currect direction of travel
            food_l, food_r, food_u, food_d, # Where the food is relative to head
        ]
        return np.array(state, dtype=int)

    def remember(self, state, action, reward, next_state, game_over):
        self.memory.append((state, action, reward, next_state, game_over))

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            mini_sample = random.sample(self.memory, BATCH_SIZE)
        else:
            mini_sample = self.memory
        states, actions, rewards, next_states, game_overs = zip(*mini_sample)
        self.trainer.train_step(states, actions, rewards, next_states, game_overs)

    def train_short_memory(self, state, action, reward, next_state, game_over):
        self.trainer.train_step(state, action, reward, next_state, game_over)

    def get_action(self, state):
        self.epsilon = 80 - self.n_games
        final_move = [0,0,0]
        if random.randint(0, 200) < self.epsilon:
            move = random.randint(0,2)
            final_move[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item()
            final_move[move] = 1
        return final_move

def train():
    scores = []
    mean_scores = []
    total_score = 0
    best_score = 0
    agent = Agent()
    game = SnakeGame()
    while True:
        state = agent.get_state(game) # Get current game state
        move = agent.get_action(state) # Get action from the model
        reward, game_over, score = game.play_step(move) # advance game state
        new_state = agent.get_state(game) # See what the new state is
        agent.train_short_memory(state, move, reward, new_state, game_over) # Train the model (basic Q-learning)
        agent.remember(state, move, reward, new_state, game_over) # Add this move/action pair to long term memory

        if game_over:
            game.reset() # reset for new episode of training

            agent.train_long_memory() # Replay training
            agent.n_games += 1
            
            if score > best_score:
                best_score = score
                agent.model.save()
            print(f"Game {agent.n_games} conluded with score {score}, best score so far: {best_score}")

            scores.append(score)
            total_score += score

            mean_scores.append(total_score / agent.n_games)
            plot(scores, mean_scores)

if __name__ == '__main__':
    train()
