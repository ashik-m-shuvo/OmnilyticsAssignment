
# User configurable variables

input_file = 'challenge_a_output.txt'
output_file = 'challenge_b_output.txt'


# Define object type

def get_object_type(str1):
	if str1.isalpha():
		return 'alphabetical strings'
	elif str1.isdecimal():
		return 'integer'
	elif '.' in str1: # here real number contains a '.'
		return 'real numbers'
	elif str1.isalnum():
		return 'alphanumeric'
	else:
		return 'error'


if __name__ == '__main__' :

	print('Starting... ')

	with open(input_file, 'r') as file_input:
		with open(output_file, 'w') as file_output:
			for line1 in file_input:
				object_list = line1.split(',')
				for obj in object_list:
					obj = obj.strip()
					str_out = obj + ' - ' + get_object_type(obj)
					print(str_out)
					file_output.write(str_out + '\n')
			file_output.close()
		file_input.close()

	print('Output File: ' + output_file)
	print('Exiting... ')
