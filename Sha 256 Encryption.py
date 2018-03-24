import hashlib

# This is a function using the build in hash library by python.
def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature


# This is the main funtions which uses the encrypt funtion above 
def main():
	hash_string = input('Enter the string to be encrypted: ')
	print (hash_string)
	sha_signature = encrypt_string(hash_string)
	print(sha_signature)

	# This line is put to the output of the hash can be seen before programs is closed
	input('End of program\nGoodBye')


# This code calls the main fuuntion to execute the program
main()