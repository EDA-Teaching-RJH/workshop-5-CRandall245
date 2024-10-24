import random 
# Constants 
MISSION_TYPES = ["Exploration", "Diplomacy", "Combat", "Rescue", "Scientific Research"] 
# Ship systems, resources, and crew 
ship = { 
		"systems": { 
		"shields": 100, 
		"weapons": 100, 
		"engines": 100, 
		"sensors": 100 
		}, 
		"resources": { 
			"energy": 1000, 
			"torpedoes": 10 
		}, 
		"crew": { 
			"Picard": "Command", 
			"Riker": "Command", 
			"Data": "Operations", 
			"Worf": "Operations", 
			"La Forge": "Operations", 
			"Crusher": "Sciences", 
			"Troi": "Sciences" 
		} 
	} 

def main(): 
	print("Welcome to the Star Trek: TNG Mission Simulator!") 
	score = 0 
	turns = 0 

	while True: 
		display_status() 
		action = get_user_action() 
		if action == "1": 
			score += run_mission() 
		elif action == "2": 
			repair_system() 
		elif action == "3": 
			add_crew_member() 
		elif action == "4": 
			print(f"Simulation ended. Final score: {score}") 
			break 
		else: 
			print("Invalid action. Please try again.") 
		
	turns += 1 
	handle_random_event() 

	if turns % 3 == 0: 
		replenish_resources() 

def display_status(): 
# TODO: Implement function to display ship status, resources, and crew 
	l = True
	while l == True:
		usStatus = input("What part of the ship do you want to check 'systems', ,resources', 'crew'. to leave type'exit':")
		print(ship[usStatus])
		if usStatus.strip() == 'exit':
			l = False
		else:
			l = True


def get_user_action(): 
# TODO: Implement function to get and return user's chosen action 
	usInput = input("What actions would you like to do?\n 1. mission\n 2. repair system\n 3. add crew member\n 4. end simulation\n").strip()
	return(usInput)


def run_mission(): 
	mission_type = random.choice(MISSION_TYPES) 
	print(f"\nNew mission: {mission_type}") 
	# TODO: Implement mission logic for different mission types 
	# Return the score earned from the mission 

def repair_system(): 
# TODO: Implement system repair functionality
	loop = True
	while loop == True:
		userInp = input("What system would you like to repair?\n 1. Sheilds\n 2. weapons\n 3. engines\n 4. sensors\n 5. exit\n").strip()
		if userInp == '1':
			sheild = ship["systems"]["sheilds"]
			energy = ship["resources"]["energy"]
			if sheild == 100:
				print("Sheilds fully functional")
			elif sheild < 100:
				sheiDiff = 100 - sheild
				restCost = sheiDiff * 2
				dec = input("The cost to restore the sheild is" , restCost , "and you have" , energy ,"\n do you want to proceed?\n Y/N\n").strip()
				if restCost > energy and dec == 'Y':
					print("Insufficient Energy")
				elif restCost <= energy and dec == 'Y':
					ship["resources"]["energy"] = (energy - restCost)
					ship["systems"]["sheild"] = 100
					print("repair complete")
				elif dec == 'N':
					waste = True
		elif userInp == '2':
			weap = ship["systems"]["weapons"]
			energy = ship["resources"]["energy"]
			if weap == 100:
				print("Weapons fully functional")
			elif weap < 100:
				weapDiff = 100 - weap
				restCost = weapDiff * 2
				dec = input("The cost to restore the sheild is" , restCost , "and you have" , energy ,"\n do you want to proceed?\n Y/N\n").strip()
				if restCost > energy and dec == 'Y':
					print("Insufficient Energy")
				elif restCost <= energy and dec == 'Y':
					ship["resources"]["energy"] = (energy - restCost)
					ship["systems"]["weapons"] = 100
					print("repair complete")
				elif dec == 'N':
					waste = True
		elif userInp == '3':
			eng = ship["systems"]["engines"]
			energy = ship["resources"]["energy"]
			if eng == 100:
				print("Enginess fully functional")
			elif eng < 100:
				engDiff = 100 - eng
				restCost = engDiff * 2
				dec = input("The cost to restore the sheild is" , restCost , "and you have" , energy ,"\n do you want to proceed?\n Y/N\n").strip()
				if restCost > energy and dec == 'Y':
					print("Insufficient Energy")
				elif restCost <= energy and dec == 'Y':
					ship["resources"]["energy"] = (energy - restCost)
					ship["systems"]["engines"] = 100
					print("repair complete")
				elif dec == 'N':
					waste = True
		elif userInp == '4':
			sens = ship["systems"]["sensors"]
			energy = ship["resources"]["energy"]
			if sens == 100:
				print("Sensors fully functional")
			elif sens < 100:
				sensDiff = 100 - sens
				restCost = sensDiff * 2
				dec = input("The cost to restore the sheild is" , restCost , "and you have" , energy ,"\n do you want to proceed?\n Y/N\n").strip()
				if restCost > energy and dec == 'Y':
					print("Insufficient Energy")
				elif restCost <= energy and dec =='Y':
					ship["resources"]["energy"] = (energy - restCost)
					ship["systems"]["sensors"] = 100
					print("repair complete")
				elif dec == 'N':
					waste = True
		elif userInp == '5':
			loop == False
		else:
			print("Unknown Input")



 
def add_crew_member(): 
# TODO: Implement functionality to add a new crew member 
	name = input("What is the name of the new crew member:\n")
	spec = input("What is " + name + "'s specialisation:\n")
	ship["crew"][name] = spec

def handle_random_event():
# TODO: Implement random events that can occur during the simulation 

def use_resource(resource, amount): 
# TODO: Implement resource usage logic 

def replenish_resources(): 
# TODO: Implement resource replenishment logic 
	currentEn = ship['resources']['energy']
	currentTorp = ship['resources']['torpedoes']
	if currentEn < 1000:
		enDiff = 1000 - currentEn
		if enDiff < 250:
			ship['resources']['energy'] = 1000
		else:
			ship['resources']['energy'] = (currentEn + 250)
	else:
		waste = True
	
	if currentTorp < 10:
		torpDiff = 10 - currentTorp
		if torpDiff < 2:
			ship['resources']['torpedoes'] = 10
		else:
			ship['resources']['torpedoes'] = (currentTorp + 2)
	else:
		waste = True

main()
