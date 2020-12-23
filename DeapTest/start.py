from deap import base, creator, tools
from scipy.stats import bernoulli
from DeapTest import IP
import sys
import time



t0 = time.time()


test = IP.IP("C:\\Study\\TestCase\\2020_MEC\\Test1_Muti_Pro\\a20\\0000.xml")


# 定义问题
creator.create('FitnessMin', base.Fitness, weights=(-1.0,)) #优化目标：单变量，求最小值
creator.create('Individual', list, fitness = creator.FitnessMin) #创建Individual类，继承list

# 生成个体
IND_SIZE = 20
toolbox = base.Toolbox()
toolbox.register('Binary', bernoulli.rvs, 0.5)
toolbox.register('Individual', tools.initRepeat, creator.Individual, toolbox.Binary, n=IND_SIZE)

# 生成初始族群
N_POP = 100
toolbox.register('Population', tools.initRepeat, list, toolbox.Individual)
pop = toolbox.Population(n = N_POP)
# print(pop)

# 定义评价函数
def evaluate(individual):
  return (test.getIP(individual)), #注意这个逗号，即使是单变量优化问题，也需要返回tuple




def GA(pop,N):
    IP = (sys.maxsize),
    t = 0
    wai = 0
    nei = 0
    while(t<N):
        # 评价初始族群
        t1 = time.time()
        toolbox.register('Evaluate', evaluate)
        fitnesses = map(toolbox.Evaluate, pop)
        for ind, fit in zip(pop, fitnesses):
          ind.fitness.values = fit
          if IP > fit:
              IP = fit
          # print(ind.fitness.values)

        t2 = time.time()
        # 选择方式1：锦标赛选择
        toolbox.register('TourSel', tools.selTournament, tournsize = 2) # 注册Tournsize为2的锦标赛选择
        selectedTour = toolbox.TourSel(pop, 5) # 选择5个个体
        # print('锦标赛选择结果：')
        # for ind in selectedTour:
        #   print(ind)
        #   print(ind.fitness.values)

        toolbox.register('Best', tools.selBest) # 注册Tournsize为2的锦标赛选择
        newpop = toolbox.Best(pop+selectedTour, N_POP)
        # for ind in newpop:
        #   print(ind)
        #   print(ind.fitness.values)

        pop = toolbox.clone(newpop)

        # print("交叉之后")
        # 均匀交叉
        i = 0
        while i < N_POP:
            tools.cxUniform(newpop[i], newpop[i+1], 0.5)
            i += 2

        # print("突变之后")
        # 均匀整数突变
        for ind in newpop:
            tools.mutUniformInt(ind, 0, 1, 0.5)

        pop = toolbox.Best(pop+newpop, N_POP)

        t += 1
        t3 = time.time()
        wai += t3-t2
        nei += t2 - t1
    print("计算IP的时间")
    print(wai)
    print("遗传算法时间")
    print(nei)
    return IP


ip = GA(pop,5)
print(ip)

tt =time.time()

print("总时间")
print(tt-t0)