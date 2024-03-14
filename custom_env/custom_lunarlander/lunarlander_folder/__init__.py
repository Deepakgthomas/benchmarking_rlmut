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
    id="myLunarLander-v1",
    entry_point="lunarlander_folder.envs:myLunarLanderEnv",
    max_episode_steps=1000,
    reward_threshold=200,
)
# register(
#     id="LunarLander-v2",
#     entry_point="gym.envs.box2d:LunarLander",
#     max_episode_steps=1000,
#     reward_threshold=200,
# )