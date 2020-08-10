import torch
from .Environment import Carrot_House
from .Agent import Agent
from .Hyperparams import PATH
from .Hyperparams import EPISODES
from .Hyperparams import MAX_STEPS



def get_Action(Humid, Temp):
    state = torch.tensor([Humid, Temp])
    agent = Agent()
    agent.brain.Q.load_state_dict(torch.load(PATH))
    action = agent.action_process(state)
    return action
