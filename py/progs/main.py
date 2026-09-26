import sys

sys.path.append("E:\\REPOS_LOCAL\\python-exercise-world-cup\\py\\packages")

for p in sys.path:
    print(p)
print()


from world_cup.stadia.stadium_manager import *

print("******************* Welcome to the World Cup 2026 *******************")
print()
print(open())
print()

from world_cup.ticketing import corporate as corporate_ticketing
from world_cup.ticketing import standard as standard_ticketing

print(corporate_ticketing.corporate())
print(standard_ticketing.standard())
print()

from world_cup.hospitality import corporate as corporate_hospitality
from world_cup.hospitality import standard as standard_hospitality

print(corporate_hospitality.corporate())
print(standard_hospitality.standard())
print()

from world_cup.media.internet import view_game
from world_cup.media.radio import hear_game
from world_cup.media.tv import view_game as tv_game

print(view_game())
print(hear_game())
print(tv_game())
print()

print(close())

print("************* Thank you for visiting the World Cup 2026 *************")
