import numpy as np
from numba import njit

@njit
def getActionSize():
  return 18
@njit
def getAgentSize():
  return 4
@njit
def getStateSize():
  return 32

@njit
def initEnv():
  all = np.arange(52) % 13
  np.random.shuffle(all)

  env = np.zeros(118)
  env[: 52] = all

  for i in range(20):
    idx = i%4
    laBai = env[i]
    env[53 + idx * 15 + laBai] += 1

  env[52] = 32
  for i in range(4):
    arr = env[53 + 15*i: 66 + 15*i]
    env[67 + i*15] = np.where( arr == 4)[0].size
    env[66 + i*15] = 5 - env[67 + i*15]*4

  env[116] = -1
  return env

print(initEnv())