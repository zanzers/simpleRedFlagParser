from interpreter import lexi, parser_lexi
from redflag import redFlags

input_str = "A*A"
tokens = lexi(input_str)

# Extracting Tokens type:        
token_types = [token['type'] for token in tokens if token['type'] != 'EOF']
concatenated_types = ''.join(token_types)

# Note the parser only feed by the tokens type base on the lexi tokens stream:
# the parser["eval"] are part of the redflag  function.....
#the ouput of parser["eval"]() will feed to the parser_lexi to get
# the initial value of the ouput.

parser = redFlags(concatenated_types)
result = parser["eval"]()
token_result = parser_lexi(result,tokens)


print()
for token in tokens:
    if token['type'] == 'EOF':
        print(f"Type: {token['type']}")
    else:
        print(f"Type: {token['type']}, Value: {token['value']}")

print()
print("Result:", result)
print("Parser Result: ", token_result)



