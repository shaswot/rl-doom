import time

from stable_baselines3.common import evaluation

import config
from environments import utils as env_utils

from helpers import cli

if __name__ == '__main__':
    # Extract command line arguments
    parser = cli.get_parser()
    args = parser.parse_args()

    scenario = args.scenario
    load_from = args.load
    config_path = args.config

    # Load config for session
    conf = config.load(config_path)

    # Create environments.
    env = env_utils.get_evaluation_env(conf.environment_config)

    # Load agent
    agent = conf.get_agent(env=env, load_from=load_from)

    for i in range(10):
        obs = env.reset()
        done = False
        images = []
        while not done:
            action, _ = agent.predict(obs, deterministic=False)
            obs, reward, done, _ = env.step(action)
            time.sleep(1/35.0)

    env.close()
