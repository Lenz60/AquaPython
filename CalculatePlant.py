
# ? Dictionary
tankSpec = {
    "size": "30W",
    "type": "large"
}

recPlants = {
    "foreground": [],
    "midground": [],
    "background": []
}

plantNeeds = {
    "substrate": ["ADA Amazonia","Any Soil", "Gravel", "Sand"],
    "light": 30,
    "co2": True
}

selectedStyle = {
    "code": 0,
    "name": "Dutch Style",
}

plantSpec = {
    "spec": "high"
}

recomendedDisplay = {
    "tankSize": "",
    "styleCode": 0,
    "selectedStyle": "",
    "spec": "",
    "substrate": "",
    "light": 0,
    "co2": False,
    "foreground": [],
    "midground": [],
    "background": []
}

# ? Tuple

lightData = (18,24,42,75,150)

# ? List
# v Plant Selections

#  v Lowtec
lowTecBackground = ["Valisneria Nana", "Valisneria Nathan", "Pogostemon Erectus", "Limnophila Aquatica", "Hygrophila Polysperma" ]
lowTecMidground = ["Cryptocoryne Wendtii", "Cryptocoryne Parvula", "Juncus Repens", "Anubias Nana", "Eriocaulon sp. Vietnam"]
lowTecForeround = ["Eleocharis Acicularis", "Eleocharis Parvula", "Micranthemum 'Monte Carlo'", "Sagitaria Subulata" ]

# v Medium
mediumTecBackground = ["Eleocharis Montevidensis", "Eleocharis Vivipara","Rotala Green", "Rotala HRA" ]
mediumTecMidground = ["Blyxa Japonica", "Echinodorus Tenellus", "Eriocaulon sp. Vietnam"]
mediumTecForeground = ["Hemianthus Callitrichoides", "Micranthemum 'Monte Carlo'", "Eleocharis Parvula", "Eleocharis Acicularis Mini", "Glossostigma Elatinodes"]

# v HighTec
highTecBackground = ["Rotala Blood Red", "Rotala Hra", "Rotala Green", "Ludwigia rubin", "Ludwigia sp Red", "Ludwigia sp White"]
highTecMidground = ["Alternanthera Reineckii Mini", "Staurogyne Repens", "Hygrophila sp. chai", "Rotala florida sunset", "Alternanthera reineckii 'Rosanervig'"]
highTecForeground = ["Eleocharis Acicularis", "Eleocharis Parvula", "Hemianthus Callitrichoides", "Micranthemum 'Monte Carlo'"]

# ? Set
# v Wildcard
iwagumiBackground = {"Eleocharis Vivipara", "Eleocharis Montevidensis", "Eleocharis Acicularis Mini"}
jungleMidground = {"Anubias Barteri", "Bucepelandra sp.", "Juncus Repens", "Anubias Nana", "Microsorum Trident", "Microsorum ptepropus"}

def proceed_tank_choice():
    tank = dict.fromkeys(tankSpec)
    # v Checkin input then continue input when invalid input
    while True:
        tank_choice = input("Enter your choice: ")
        # v S̶w̶i̶t̶c̶h̶  match case
        match tank_choice:
            case "1":
                tank["size"] = "30W"
                tank["type"] = "small"
            case "2":
                tank["size"] = "45P"
                tank["type"] = "medium"
            case "3":
                tank["size"] = "60P"
                tank["type"] = "medium"
            case "4":
                tank["size"] = "75P"
                tank["type"] = "large"
            case "5":
                tank["size"] = "90P"
                tank["type"] = "large"
            case _:
                print("Invalid choice. Please enter a number between 1 and 5.")
                continue  # Continue the loop to prompt again
        break 
    
    recomendedDisplay.update({"tankSize": tank["size"]})


def proceed_style_choice():
    style_choice = input("Enter your choice: ");
    needs = dict.fromkeys(plantNeeds)
    style_chosen = dict.fromkeys(selectedStyle)
    # v If else statement
    if style_choice == "1":
        style_chosen["code"] = 1
        style_chosen["name"] = "Dutch Style"
        needs["substrate"] = ["ADA Amazonia"]
    elif style_choice == "2":
        style_chosen["code"] = 2
        style_chosen["name"] = "Iwagumi Style"
        needs["substrate"] = ["ADA Amazonia", "Any Soil"]
    elif style_choice == "3":
        style_chosen["code"] = 3
        style_chosen["name"] = "Nature Style"
        needs["substrate"] = ["ADA Amazonia", "Any Soil", "Gravel", "Sand"]
    elif style_choice == "4":
        style_chosen["code"] = 4
        style_chosen["name"] = "Jungle Style"
        needs["substrate"] = ["ADA Amazonia", "Any Soil", "Gravel", "Sand"]
    else: 
        print("Invalid choice")
    recomendedDisplay.update({"styleCode": style_chosen["code"],"selectedStyle": style_chosen["name"], "substrate": needs["substrate"]})

def calculate_specs():
    needs = dict.fromkeys(plantNeeds)
    spec = dict.fromkeys(plantSpec)
    # v S̶w̶i̶t̶c̶h̶  match case
    match recomendedDisplay['tankSize']:
        case "30W":
            match recomendedDisplay['styleCode']:
                # v Arithmetic operation
                case 1:
                    spec['spec'] = "high"
                    needs["co2"] = True
                    needs['light'] = lightData[0]*3
                case 2:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[0]*2
                case _:
                    needs["co2"] = False
                    spec['spec'] = "low"
                    needs['light'] = lightData[0]
        case "45P":
            match recomendedDisplay['styleCode']:
                case 1:
                    spec['spec'] = "high"
                    needs["co2"] = True
                    needs['light'] = lightData[1]*3
                case 2:
                    needs["co2"] = True
                    spec['spec'] = "high"
                    needs['light'] = lightData[1]*2
                case _:
                    needs["co2"] = False
                    spec['spec'] = "low"
                    needs['light'] = lightData[1]
        case "60P":
            match recomendedDisplay['styleCode']:
                case 1:
                    needs["co2"] = True
                    spec['spec'] = "high"
                    needs['light'] = lightData[2]*3
                case 2:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[2]*2
                case _:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[2]
        case "75P":
            match recomendedDisplay['styleCode']:
                case 1:
                    needs["co2"] = True
                    spec['spec'] = "high"
                    needs['light'] = lightData[3]*3
                case 2:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[3]*2
                case _:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[3]
        case "90P":
            match recomendedDisplay['styleCode']:
                case 1:
                    needs["co2"] = True
                    spec['spec'] = "high"
                    needs['light'] = lightData[4]*3
                case 2:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[4]*2
                case _:
                    needs["co2"] = True
                    spec['spec'] = "medium"
                    needs['light'] = lightData[4]
    recomendedDisplay.update({"spec": spec['spec'], "light": needs['light'], "co2": needs['co2']})                

def recommend_plants():
    plants = dict.fromkeys(recPlants)
    # v S̶w̶i̶t̶c̶h̶  match case
    match recomendedDisplay['spec']:
        case "low":
            match recomendedDisplay['styleCode']:
                case 1:
                    plants["foreground"] = lowTecForeround
                    plants["midground"] = highTecMidground
                    plants["background"] = mediumTecBackground
                case 2:
                    # v List Operation (Append)
                    plants["foreground"] = lowTecForeround
                    plants["midground"] = lowTecMidground
                    plants["background"] = lowTecBackground
                    plants["background"].append(iwagumiBackground)
                case 4:
                    # v List Operation (Extend)
                    plants["foreground"] = lowTecForeround
                    plants["midground"] = lowTecMidground
                    plants["background"] = lowTecBackground
                    plants["midground"].extend([set(jungleMidground)])
                case _:
                    plants["foreground"] = lowTecForeround
                    plants["midground"] = lowTecMidground
                    plants["background"] = lowTecBackground
        case "medium":
            match recomendedDisplay['styleCode']:
                case 1:
                    plants["foreground"] = highTecForeground
                    plants["midground"] = highTecMidground
                    plants["background"] = mediumTecBackground
                case 2:
                    # v List Operation (Append)
                    plants["foreground"] = mediumTecForeground
                    plants["midground"] = mediumTecMidground
                    plants["background"] = mediumTecBackground
                    plants["background"].append(iwagumiBackground)
                case 4:
                    # v List Operation (Extend)
                    plants["foreground"] = mediumTecForeground
                    plants["midground"] = mediumTecMidground
                    plants["background"] = mediumTecBackground
                    plants["midground"].extend([set(jungleMidground)])
                case _:
                    plants["foreground"] = mediumTecForeground
                    plants["midground"] = mediumTecMidground
                    plants["background"] = mediumTecBackground
        case "high":
            match recomendedDisplay['styleCode']:
                case 1:
                    plants["foreground"] = highTecForeground
                    plants["midground"] = highTecMidground
                    plants["background"] = highTecBackground
                case 2:
                    # v List Operation (Append)
                    plants["foreground"] = highTecForeground
                    plants["midground"] = highTecMidground
                    plants["background"] = highTecBackground
                    plants["background"].append(iwagumiBackground)
                case 4:
                    # v List Operation (Extend)
                    plants["foreground"] = highTecForeground
                    plants["midground"] = highTecMidground
                    plants["background"] = highTecBackground
                    plants["midground"].extend([set(jungleMidground)])
                case _:
                    plants["foreground"] = highTecForeground
                    plants["midground"] = highTecMidground
                    plants["background"] = highTecBackground
        case _:
            plants["foreground"] = mediumTecForeground
            plants["midground"] = mediumTecMidground
            plants["background"] = mediumTecBackground
    recomendedDisplay.update({"foreground": plants["foreground"], "midground": plants["midground"], "background": plants["background"]})
    
def loop_plants(plants, plant_type):
    # v Strin Manipulation
    print(f"Recomended {plant_type.capitalize()} plants:")
    for plant in plants:
        if isinstance(plant, set):
            print("  Recomended for this style:")
            for sub_plant in plant:
                print(f"    - {sub_plant}")
        else:
            print(f"  - {plant}")

def loop_substrate(substrate):
    print("Recomended substrate for your tank :")
    for sub in substrate:
        print(f"  - {sub}")
        
def check_co2(co2):
    if co2:
        print("Your tank require CO2 injection")
    else:
        print("Your tank can survive without CO2 injection")
        
def display_recommendation():
    calculate_specs()
    recommend_plants()
    print("Based on your tank size and style choice, \nWe recommend the following plants for your aquascape")
    print(f"{'='*50}")
    print(f"Your tank is a {recomendedDisplay['tankSize']} tank")
    print(f"Your style choice is {recomendedDisplay['selectedStyle']}")
    print(f"Your tank will require {recomendedDisplay['light']} watts of light")
    check_co2(recomendedDisplay['co2'])
    print(f"{'-'*30}")
    loop_substrate(recomendedDisplay['substrate'])
    loop_plants(recomendedDisplay['foreground'], "foreground")
    loop_plants(recomendedDisplay['midground'], "midground")
    loop_plants(recomendedDisplay['background'], "background")
    print(f"{'-'*30}")