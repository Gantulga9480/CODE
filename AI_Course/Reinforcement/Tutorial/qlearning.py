import gym
import numpy as np
import matplotlib.pyplot as plt

env = gym.make("MountainCar-v0")
env.reset()

LEARNING_RATE = 0.1
DISCOUNT = 0.95
EPISODES = 2000

SHOW_EVERY = 500

print(env.observation_space.high)
print(env.observation_space.low)
print(env.action_space.n)

DISCRETE_OS_SIZE = [20] * len(env.observation_space.high)
DISCRETE_OS_WIN_SIZE = (env.observation_space.high - env.observation_space.low) / DISCRETE_OS_SIZE

epsilon = 0.5
START_EPSILON_DECAYING = 1
END_EPISLON_DECAYING = EPISODES // 2

epsilon_decay_value = epsilon / (END_EPISLON_DECAYING - START_EPSILON_DECAYING)



q_table = np.random.uniform(low=-2, high=0, size=(DISCRETE_OS_SIZE + [env.action_space.n]))

ep_reward = []
aggr_ep_reward = {'ep': [], 'avg': [], 'min': [], 'max': []}

def get_discrete_state(state):
    discrete_state = (state - env.observation_space.low) / DISCRETE_OS_WIN_SIZE
    return tuple(discrete_state.astype(np.int))

for episode in range(EPISODES):
    episode_reward = 0
    if episode % SHOW_EVERY == 0:
        print(episode)
        render = True
    else:
        render = False  
    discrete_state = get_discrete_state(env.reset())
    done = False
    while not done:
        if np.random.random() > epsilon:
            action = np.argmax(q_table[discrete_state])
        else:
            action = np.random.randint(0, env.action_space.n)
        new_state, reward, done, _ = env.step(action)
        episode_reward += reward
        new_discrete_state = get_discrete_state(new_state)
        if render:
            env.render()

        if not done:
            max_future_q = np.max(q_table[new_discrete_state])
            current_q = q_table[discrete_state + (action, )]

            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
            q_table[discrete_state + (action, )] = new_q
        elif new_state[0] >= env.goal_position:
            print(f"We made it on episode {episode}")
            q_table[discrete_state + (action, )] = 0
        discrete_state = new_discrete_state
    if END_EPISLON_DECAYING >= episode>= START_EPSILON_DECAYING:
        epsilon -= epsilon_decay_value

    ep_reward.append(episode_reward)
    if not episode % SHOW_EVERY:
        average_reward = sum(ep_reward[-SHOW_EVERY:])/len(ep_reward[-SHOW_EVERY:])
        aggr_ep_reward['ep'].append(episode)
        aggr_ep_reward['avg'].append(average_reward)
        aggr_ep_reward['min'].append(min(ep_reward[-SHOW_EVERY:]))
        aggr_ep_reward['max'].append(max(ep_reward[-SHOW_EVERY:]))

        print(f"Episode: {episode} avg: {average_reward} min: {min(ep_reward[-SHOW_EVERY:])} max: {max(ep_reward[-SHOW_EVERY:])}")

env.close() 

plt.plot(aggr_ep_reward['ep'], aggr_ep_reward['avg'], label="avg")
plt.plot(aggr_ep_reward['ep'], aggr_ep_reward['min'], label="min")
plt.plot(aggr_ep_reward['ep'], aggr_ep_reward['max'], label="max")
plt.legend(loc=4)
plt.show()
