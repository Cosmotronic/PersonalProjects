# Console substitution cypher.  Features user-selectable offset.

upper_offset = 65 # ord('A') = 65, marking the beginning of capital letters in ascii
lower_offset = 97 # ord('a') = 97, marking the beginning of lowercase letters in ascii
test_map_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
test_map_lower = "abcdefghijklmnopqrstuvwxyz"

running = True

def main():
	global running
	mod_selector = input("Enter first character of modified alphabet (ie. A = N for a Rot13 cypher) ")
	mod_selector = ord(mod_selector.lower()) - lower_offset #this allows the user to select what rotation the substitution cypher uses

	cypher_string = input("Input encyphered string:" )

	def new_char(char,selector):
		new_char = (char - selector) % 26
		return new_char

	def substitution(string):
		text_result = ""

		for i in string:
		    if ord(i) == 32: # if the character is a space, then just append to output
		        text_result += i
		    elif i in test_map_upper or test_map_lower: # if it's an alphabetical character, substitute
		        if i in test_map_upper:
		            char = ord(i) - upper_offset
		            new_char(char,mod_selector)
		            result = new_char + upper_offset
		            text_result += chr(result)
		        elif i in test_map_lower:
		            char = ord(i) - lower_offset
		            new_char(char,mod_selector)
		            result = new_char + lower_offset
		            text_result += chr(result)
		    else: #if it's not al alphabetical character, just append to output
		        text_result += i

		return text_result

	output = substitution(cypher_string)

	print(output)

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
