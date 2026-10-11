room_temp = float(input("Room temperature: "))
print(room_temp, "˚C")

surface_areas = {
	"mug": 0.029,
	"cup": 0.030,
	"bowl":0.035 ,
	"deep_plate": 0.038,
	"flat_plate": 0.030,
	"baking_pan":0.076,
}

volumes = {
	"mug": 0.00030,
	"cup": 0.00022,
	"bowl": 0.00050,
	"deep_plate": 0.00040,
	"flat_plate": 0.00015,
	"baking_pan": 0.00230
}

FOOD_PROFILES = {
	"tea_coffee": {
		"label": "Tea/Coffee",
		"state": "liquid",
		"density": 1000,		# kg/m^3 (Water at room temperature)
		"specific_heat": 4180,		# J / (kg * ˚C) = c = (heat capacity)
		"alpha": 12.0,			# W /(m^2 * K) =  U (thermal transmittance)
		"area": surface_areas["mug"],	# m^2
		"volume": volumes["mug"],	# m^3
		"start_temp": 100.0
	},

	"soup": {
		"label": "Soup",
		"state": "liquid",
		"density": 1050,
		"specific_heat": 3950,
		"alpha": 14.0,
		"area": surface_areas["bowl"],
		"volume": volumes["bowl"],
		"start_temp": 85.0
	},

	"stew": {
		"label": "Stew",
		"state": "semi_solid",
		"density": 1100,
		"specific_heat": 3400,
		"alpha": 10.0,
		"area": surface_areas["deep_plate"],
		"volume": volumes["deep_plate"],
		"start_temp": 80.0
	},

	"pasta": {
		"label": "Pasta",
		"state": "solid",
		"density": 600,
		"specific_heat": 3100,
		"alpha": 8.0,
		"area": surface_areas["flat_plate"],
		"volume": volumes["flat_plate"],
		"start_temp": 75.0
	},

	"meat": {
		"label": "Meat",
		"state": "solid",
		"density": 1060,
		"specific_heat": 2800,
		"alpha": 7.5,
		"area": surface_areas["flat_plate"],
		"volume": volumes["flat_plate"],
		"start_temp": 70.0
	}
}

choice = 0
while choice < 1 or choice > 5:
	choice = int(input(f''' 
	1 - {FOOD_PROFILES["tea_coffee"]["label"]} 	 - 1
	2 - {FOOD_PROFILES["soup"]["label"]}		 - 2 
	3 - {FOOD_PROFILES["stew"]["label"]}		 - 3
	4 - {FOOD_PROFILES["pasta"]["label"]}		 - 4
	5 - {FOOD_PROFILES["meat"]["label"]}		 - 5

	Type of food: '''))

match choice:
	case 1:
		type_of_food = FOOD_PROFILES["tea_coffee"]["start_temp"] 
		current_profile = "tea_coffee"
	case 2:
		type_of_food = FOOD_PROFILES["soup"]["start_temp"]
		current_profile = "soup"
	case 3:
		type_of_food = FOOD_PROFILES["stew"]["start_temp"]
		current_profile = "stew"
	case 4:
		type_of_food = FOOD_PROFILES["pasta"]["start_temp"]
		current_profile = "pasta"
	case 5:
		type_of_food = FOOD_PROFILES["meat"]["start_temp"]
		current_profile = "meat"

print(type_of_food)

def simulate_cooling_step(profile_key: str, current_temp: float, env_temp: float, volume_m3: float, surface_area: float, dt_seconds: float = 60.0) -> float:
	profile = FOOD_PROFILES[profile_key]

	mass = profile["density"] * profile["volume"]
	heat_capacity = mass * profile["specific_heat"]

	# temp change: delta_T = (alpha * A * (T = T_env) * dt) / (m * c)
	delta_temp = (profile["alpha"] * profile["area"] * (current_temp - env_temp) * dt_seconds) / heat_capacity

	return current_temp - delta_temp

current_temp = type_of_food
#volume = 0.00025						# 250 ml = 0.00025 m^3

print(f"Starting temperature: {current_temp:.2f} ˚C")

for min in range(1, 61):
	current_temp = simulate_cooling_step(
		profile_key = current_profile,
		current_temp = current_temp,
		env_temp = room_temp,
		volume_m3 = volumes,
		surface_area = "area",
		dt_seconds = 60.0				# 1 minute step
	)
print(f"After {min}. minutes: {current_temp:.2f} ˚C")
