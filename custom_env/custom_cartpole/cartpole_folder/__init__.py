from gym.envs.registration import (
    registry,
    register,
    make,
    spec,
    load_env_plugins as _load_env_plugins,
)

# Hook to load plugins from entry points
_load_env_plugins()



register(
    id="myCartPole-v1",
    entry_point="cartpole_folder.envs:myCartPoleEnv",
    max_episode_steps=500,
    reward_threshold=475.0,
)

# register(
#     id="CartPole-v1",
#     entry_point="gym.envs.classic_control:CartPoleEnv",
#     max_episode_steps=500,
#     reward_threshold=475.0,
# )