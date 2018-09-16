def comp(x, y):
    return (score[x] > score[y])

import gym
import random
from operator import itemgetter
mut = 0
pool_size = 200
time_l = 100
survivors = 20
pt = [[(random.randint(0,50)/25 - 1) for x in range(time_l)] for y in range(pool_size)]
env = gym.make('MountainCarContinuous-v0')
q = 1
while True:
    score = []
    rew = []
    ms = []
    for i_episode in range(pool_size):
        t_score = -1
        mrew = 0
        mk = 0
        observation = env.reset()
        for t in range(time_l):
            action = env.action_space.sample()
            observation, reward, done, info = env.step([pt[i_episode][t]])
            t_score = max(observation[0],t_score)
            mrew += reward
            mk += 1
            if done:
                print("Episode finished after ",(t+1)," timesteps, reward = ",mrew)
                file = open("Count.txt", "r")
                st = int(file.read())
                st = st + 1
                file.close()
                memory = open(str(st) + ".txt", "w")
                memory.write(" ".join(map(str,pt[i_episode])) + "%" + str(mrew))
                memory.close()
                file = open("Count.txt", "w")
                file.write(str(st))
                file.close()
                break
        score.append(t_score)
    print(str(q) + " Genration")
    print(score[0])
    g = []
    for x in range(pool_size):
        mg = []
        mg.append(score[x])
        mg.append(x)
        g.append(mg)
    g.sort(key = itemgetter(0), reverse = True)
    ts = list(range(pool_size))
    for i in range(pool_size):
        ts[i] = pt[g[i][1]]
    print(g[0][0])

    pt = ts[:survivors]
    observation = env.reset()
    mys = 0
    for t in range(time_l):
        env.render()
        action = env.action_space.sample()
        observation, reward, done, info = env.step([pt[0][t]])
    for i in range(pool_size - survivors):
        a = random.randint(0,survivors - 1)
        b = random.randint(0,survivors - 1)
        new = []
        for j in range(time_l):
            d = random.randint(0,1)
            if (mut == 0):
                m = 1
            else:
                m = random.randint(0,mut)
            if m == mut:
                new.append(random.randint(0,50)/25 - 1)
            else:
                new.append(pt[a][j]*d + pt[b][j]*(1-d))
        pt.append(new)
    q += 1
                
                
                
        
        
        
        
