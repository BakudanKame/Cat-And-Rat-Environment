from gym.envs.registration import register

register(
    id='CatAndRatEnvironment-v0',
    entry_point='CatRatEnvironment.envs:CatAndRatEnvironment',
)
