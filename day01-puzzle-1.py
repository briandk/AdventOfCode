puzzle_inputs = [item.strip() for item in """ 
	R5, R4, R2, L3, R1, R1, L4, L5, R3, L1, L1, R4, L2, R1, R4, R4, L2, L2, R4, L4, R1, R3, L3, L1, L2, R1, R5, L5, L1, L1, R3, R5, L1, R4, L5, R5, R1, L185, R4, L1, R51, R3, L2, R78, R1, L4, R188, R1, L5, R5, R2, R3, L5, R3, R4, L1, R2, R2, L4, L4, L5, R5, R4, L4, R2, L5, R2, L1, L4, R4, L4, R2, L3, L4, R2, L3, R3, R2, L2, L3, R4, R3, R1, L4, L2, L5, R4, R4, L1, R1, L5, L1, R3, R1, L2, R1, R1, R3, L4, L1, L3, R2, R4, R2, L2, R1, L5, R3, L3, R3, L1, R4, L3, L3, R4, L2, L1, L3, R2, R3, L2, L1, R4, L3, L5, L2, L4, R1, L4, L4, R3, R5, L4, L1, L1, R4, L2, R5, R1, R1, R2, R1, R5, L1, L3, L5, R2
""".split(',')]

displacement_direction = {
	'0': 'N_displacement',
	'1': 'E_displacement',
	'2': 'S_displacement',
	'3': 'W_displacement'
}
	
initial_state = {key: int(0) for key in displacement_direction.keys()}

def create_delta(input):
	# inputs are strings of the form L5 or R25
	delta = {
		'heading': 1 if input.startswith('R') else -1, 
		'displacement': int(input[1:])
	}
	
	return delta
	
def update_state(old_state, delta):
	
	
	new_state = {key: value for (key, value) in old_state.items()}
	new
	new_state = (old_state[heading] + delta[heading]) % 4
	new_state['d']

deltas = [
	{'heading': direction_map[input[0]], 
	 'displacement': int(input[1:])} 
	 for input in puzzle_inputs]

initial_state = {
	'heading': 0,
	'0': 0,
	'1': 0,
	'2': 0,
	'3': 0
}

print(initial_state)


def update_state(state, delta):
	new_heading = (state['heading'] + delta['heading']) % 4
	new_displacement = str(new_heading)
	
	state['heading'] = new_heading
	state[new_displacement] = state[new_displacement] + delta['displacement']
	
	return state
	
current_state = initial_state
for delta in deltas:
	current_state = update_state(current_state, delta)
	print(current_state)
	
def determine_final_position(state):
	up = state['0'] - state['2']
	over = state['1'] - state['3']
	print((up, over))
	
determine_final_position(current_state)