import CalculatePlant as cp
import os

# ? List
styleData = ["Dutch Style", "Iwagumi Style", "Nature Style", "Jungle Style"]
tankData = ["30W (30x18x24 cm)", "45P (45x27x30 cm)", "60P (60x30x36 cm)", "75P (75x45x45 cm)","90P (90x45x45 cm)"]

def loop_tank():
    print("Please enter the size of your tanks")
    # v For loop
    for tank in tankData:
        print(f"{tankData.index(tank)+1}. {tank}")

def loop_style():
    print("Select your style : ");
    # v Do While loop
    length = 0
    while length < len(styleData):
        print(f"{length+1}. {styleData[length]}")
        length+=1
    

os.system("cls")
print(f"{'='*30}")
print("Welcome to Aquascape Specification Calculator")
print(f"{'='*30}")
loop_tank()
cp.proceed_tank_choice()
print(f"{'='*20}")
loop_style()
cp.proceed_style_choice()
print(f"{'='*50}")
cp.display_recommendation();
print(f"{'='*50}")
