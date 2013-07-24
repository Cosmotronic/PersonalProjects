# usr/bin/python
# Console substitution cypher.  Features user-selectable offset.

upper_offset = 65 # ord('A') = 65, marking the beginning of capital letters in ascii
lower_offset = 97 # ord('a') = 97, marking the beginning of lowercase letters in ascii

running = True

def main():
	global running
	cypher_selector = input("Select either encypher or decypher [D] or [E]: ")
	cypher_selector = cypher_selector.lower()
	cypher_selection = False

	if cypher_selector == "d":
		cypher_selection = True
	else:
		cypher_selection = False

	mod_selector = input("Enter first character of modified alphabet (ie. A = N for a Rot13 cypher) ")
	mod_selector = ord(mod_selector.lower()) - lower_offset #this allows the user to select what rotation the substitution cypher uses

	cypher_string = input("Input encyphered string:" )

	def new_char_decypher(char,selector):
		new_char = (char - selector) % 26
		return new_char

	def new_char_encypher(char,selector):
		new_char = (char + selector) % 26
		return new_char

	def substitution(string):
		text_result = ""

		for i in string:
			char = ord(i)
			if char == 32: # if the character is a space, then just append to output
				text_result += i
			elif char in range(65,123): # if it's an alphabetical character, substitute
				if cypher_selection == True:
					if char in range(65,96):
						result = new_char_decypher((char - upper_offset),mod_selector) + upper_offset
						text_result += chr(result)
					elif char in range(97,123):
						result = new_char_decypher((char - lower_offset),mod_selector) + lower_offset
						text_result += chr(result)
				elif cypher_selection == False:
					if char in range(65,96):
						result = new_char_encypher((char - upper_offset),mod_selector) + upper_offset
						text_result += chr(result)
					elif char in range(97,123):
						result = new_char_encypher((char - lower_offset),mod_selector) + lower_offset
						text_result += chr(result)
			else: #if it's not an alphabetical character, just append to output
				text_result += i

		return text_result

	# output = substitution(cypher_string)

	print(substitution(cypher_string))

	opt_continue = input("Continue? [Y/N]")
	if opt_continue.lower() == "y" or "n":
		if opt_continue.lower() == "y":
			running = True
		elif opt_continue.lower() == "n":
			running = False
		else:
			opt_continue = input("Continue? [Y/N]")

while running:
	main()


# rot 13 encrypted message from The Secret World mmo; inspired this project.  
# using it as a sample to test the logic.
# CNGU BS GURFHA - ERYNGRF ABGWHFG GB GURFBYNE OBQL, OGH GUR GENIRY BS GUR UHZNA OBQL - OVEGU GB ORLBAQ
