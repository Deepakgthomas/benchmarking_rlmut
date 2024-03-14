try:
    import Box2D
    from lunarlander_folder.envs.lunarlander_modified import myLunarLanderEnv
except ImportError:
    Box2D = None
