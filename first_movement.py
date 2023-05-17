from robotic import ry
import time

ry.params_add({'botsim/verbose': 1., 'physx/motorKp': 10000., 'physx/motorKd': 1000.})
ry.params_print()
C = ry.Config()
C.addFile(ry.raiPath('../rai-robotModels/scenarios/pandaSingle.g'))
C.view(False, 'this is your workspace data structure C -- NOT THE SIMULTATION')


bot = ry.BotOp(C, False)
#note that in sim, arms are going down! free floating...
# we need to control it somehow, e.g. to home
bot.home(C)

while bot.getTimeToEnd()>0:
    bot.sync(C, .1)

qHome = bot.get_q()
q = bot.get_q()
print(q)
q[1] = q[1] - .1
print(q)

bot.moveTo(q, 5)

while bot.getTimeToEnd()>0:
    bot.sync(C, .1)

time.sleep(2)

bot.home(C)
while bot.getTimeToEnd()>0:
    bot.sync(C, .1)

time.sleep(2)

bot.gripperClose(ry._left)
while bot.getTimeToEnd()>0:
    bot.sync(C, .1)

time.sleep(2)

bot.gripperOpen(ry._left)
while not bot.gripperDone(ry._left):
    bot.sync(C, .1)




del bot
del C