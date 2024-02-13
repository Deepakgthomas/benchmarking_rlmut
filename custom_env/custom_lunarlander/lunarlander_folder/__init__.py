import os
import sys
from gym.envs.registration import register
register(
    id="myLunarLander-v1",
    entry_point="lunarlander_folder.envs:myLunarLanderEnv",
    max_episode_steps=1000,
    reward_threshold=200,
)
