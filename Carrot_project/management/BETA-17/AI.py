import torch
from Environment import Carrot_House
from Agent import Agent
from Hyperparams import PATH
from Hyperparams import EPISODES
from Hyperparams import MAX_STEPS



def get_Action(Humid, Temp):
    state = torch.tensor([Humid, Temp])
    agent = Agent()
    agent.brain.Q.load_state_dict(torch.load(PATH))
    action = agent.action_process(state)
    return action

'''if __name__ == '__main__':
    env = Carrot_House()
    agent = Agent()
    agent.brain.Q.load_state_dict(torch.load(PATH))
    agent.brain.Q.eval()
    scores, episodes = [], []
    for E in range(EPISODES):
        state = env.reset()
        score = 0
        for S in range(MAX_STEPS):
            print(S)
            print(state)
            action = agent.action_process(state)
            if action == 0:
                print('급수')
            elif action == 1:
                print('온도상승')
            elif action == 2:
                print('온도하락')
            else:
                print('유지')
            next_state, reward, done = env.step(action)
            if done:
                print("step", S, "  episode:", E, "  score:", score)
                break
            else:
                score += reward
                state = next_state
    print('Task End')'''