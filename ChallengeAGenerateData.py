import os
import time
import string
import random

# User configurable variables

output_file = 'challenge_a_output.txt'
max_output_file_size = 10485760 # (In Bytes)  ;  10485760 Bytes = 10 MB


# Custom functions to get 4 types object data

def get_alphabetical():
	data_type = string.ascii_letters
	object = ''.join(random.choice(data_type) for i in range(random.randint(5,10), random.randint(25,30)))
	return object

def get_integer():
	object = random.randint(random.randint(5,10), random.randint(1000,100000000))
	return object

def get_real_number():
	object = round(random.uniform(random.uniform(1.1,100.1), random.uniform(10000.111,10000000.111)), random.randint(2, 5))
	return object

def get_alphanumeric():
	data_type = string.ascii_letters + string.digits
	temp_object = ''.join(random.choice(data_type) for i in range(random.randint(5,10), random.randint(25,30)))

	# Adding random number of whitespace (not greater than 10)
	object = ' '*random.randint(1, 5) + temp_object + ' '*random.randint(1, 5)
	return object

def get_random_object():
	object_function_list = [get_alphabetical, get_integer, get_real_number, get_alphanumeric]
	object_function = random.choice(object_function_list)
	return str(object_function()) + ', '

if __name__ =='__main__' :

	print('Starting... ')

	# Create an empty output file
	file_out = open(output_file, 'w')
	file_out.write('')
	curr_file_size = file_out.tell()
	file_out.close()

	# Append objects in the output file
	with open(output_file, 'a') as file_out:
		while curr_file_size < max_output_file_size:
			file_out.write(get_random_object()) # Append single object in file
			curr_file_size = file_out.tell() # Recheck the file size
		file_out.close()

	# Removing last comma
	with open(output_file, 'rb+') as file_out2:
		file_out2.seek(-2, os.SEEK_END)
		file_out2.truncate()
		file_out2.close()


	print('Output File: ' + output_file + ', Current file size: ' , curr_file_size)
	print('Exiting... ')
