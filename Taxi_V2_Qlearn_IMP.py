import gym
import numpy as np

env = gym.make('Taxi-v3')

#make Qtable

Q = np.zeros((env.observation_space.n,env.action_space.n))

alpha = 0.1
gamma = 0.8
num_of_episodes = 1000

for i in range(num_of_episodes):
    state = int(env.reset()[0])
    done = False
    penalties,success = 0,0
    while not done:
        if np.random.uniform(0,1) < 0.5:
            action = env.action_space.sample()
        else:
            action = np.argmax(Q[state, :])

        next_state , reward , done , info , _ = env.step(action)
        Q[state, action] = Q[state, action] + alpha * (reward + gamma * np.max(Q[next_state, :]) - Q[state, action])
        state = int(next_state)
        if reward==-10:
            penalties+=1
        if reward==20:
            success+=1    
    print("Episode ",i," ended Total penalties , successes : ",penalties,success)

print("\nTraining Complete")

test_episodes = 100

for i in range(test_episodes):
    state = int(env.reset()[0])
    done = False
    penalties,success,steps=0,0,0
    while not done and steps<test_episodes:
        steps+=1
        action = np.argmax(Q[state, :])
        next_state,reward,done,info,_=env.step(action)
        state = int(next_state)
        if reward == -10:
            penalties+=1
        if reward == 20:
            success+=1
    print("Penalty rate : ",penalties/test_episodes)
    print("Success rate : ",success/test_episodes)
             
