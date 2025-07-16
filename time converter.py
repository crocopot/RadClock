from clock import radian_clock
from datetime import datetime

checkme = input("What time would you like to convert into radtime?")
checkme2 = datetime.strptime(checkme, "%H%M")
print(f"{checkme}hrs is {radian_clock(checkme2)} in radtime.")
