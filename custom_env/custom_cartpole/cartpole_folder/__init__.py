import os
import sys
from gym.envs.registration import register
register(
    id="myCartPole-v1",
    entry_point="cartpole_folder.envs:myCartPoleEnv",
    max_episode_steps=500,
    reward_threshold=475.0,
)
