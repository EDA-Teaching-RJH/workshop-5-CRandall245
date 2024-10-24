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
# TODO: Implement function to get and return user's chosen action 
	name = input("What is the name of the new crew member:\n")
	spec = input("What is " + name + "'s specialisation:\n")
	ship["crew"][name] = spec
	print(ship["crew"])
    
main()