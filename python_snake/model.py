import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
import os

class Linear_DQN(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super().__init__()
        self.lin1 = nn.Linear(input_size, hidden_size)
        self.lin2 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = F.relu( self.lin1(x))
        x = self.lin2(x)
        return x
    
    def save(self, file_name='model.pth'):
        model_folder_path = './model'
        if not os.path.exists(model_folder_path):
            os.makedirs(model_folder_path)
        file_name = os.path.join(model_folder_path, file_name)
        torch.save(self.state_dict(), file_name)



class QTrainer:
    def __init__(self, model, lr, gamma):
        self.model = model
        self.lr = lr
        self.gamma = gamma
        self.optimizer = optim.Adam(model.parameters(), lr=self.lr)
        self.criterion = nn.MSELoss()
    
    def train_step(self, state, action, reward, new_state, game_over):
        state = torch.tensor(state, dtype=torch.float)
        action = torch.tensor(action, dtype=torch.float)
        reward = torch.tensor(reward, dtype=torch.float)
        new_state = torch.tensor(new_state, dtype=torch.float)

        if len(state.shape) == 1: # Reshape input to enable the trainer to handle one or multiple samples at once
            state = torch.unsqueeze(state, 0)
            action = torch.unsqueeze(action, 0)
            reward = torch.unsqueeze(reward, 0)
            new_state = torch.unsqueeze(new_state, 0)
            game_over = (game_over, )


        pred = self.model(state)

        # Q(s,a) = r + y(max(Q(s', a)))
        target = pred.clone()
        for idx in range(len(game_over)):
            Q_new = reward[idx]
            if not game_over[idx]:
                Q_new = reward[idx] + self.gamma * torch.max(self.model(new_state[idx]))

            target[idx][torch.argmax(action).item()] = Q_new

        self.optimizer.zero_grad()

        loss = self.criterion(target, pred)
        loss.backward()

        self.optimizer.step()




