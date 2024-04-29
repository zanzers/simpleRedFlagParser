
#OR = R;
#AND = A;
#INPUT = I:A,B,C,D;
#NOT = N:A,B,C,D;
#DNI = DN: A,B,C,D;
#();
#CONSTANT = 1 OR 0;

#OR = R;
#AND = A;
#INPUT = I:A,B,C,D;
#NOT = N:A,B,C,D;
#DNI = DN: A,B,C,D;
#();
#NUMBER = 1 OR 0;

class TokensType:
    I = 'I'
    R = 'R'
    A = 'A'
    LP = 'LP'
    RP = 'RP'
    U = 'U'
    N = 'N'
    EOF = 'EOF'

def lexi(expression):
    print("lexi input: ",expression)
    tokens = []
    currentPosition = 0

    while currentPosition < len(expression):
        char = expression[currentPosition]

        if char.isspace():
            currentPosition += 1
            continue

        if char.isalpha():
            input_str = ''
            while char.isalnum() and currentPosition < len(expression):
                input_str += char
                currentPosition += 1
                if currentPosition >= len(expression):
                    break
                char = expression[currentPosition]            
                next_char = expression[currentPosition] if currentPosition < len(expression) else ''
            
            if next_char == "'":
                currentPosition += 1
                tokens.append({
                    "type": TokensType.N,
                    "value": input_str
                })
            else:
                for i in range(len(input_str)):
                    tokens.append({
                        "type": TokensType.I,
                        "value": input_str[i]
                    })
            continue
# change the 'type' to token.type.U.....
# I just put that thier cause js and python work differently......
        if char in ['1', '0']:
            tokens.append({
                "type": char, 
                "value": char
            })
            currentPosition += 1
            continue

        if char in ['+', '*']:
            gate_type = TokensType.R if char == '+' else TokensType.A
            tokens.append({
                "type": gate_type,
                "value": char
            })
            currentPosition += 1
            continue

        if char in ['(', ')']:
            tokens.append({
                "type": TokensType.LP if char == '(' else TokensType.RP,
                "value": char
            })
            currentPosition += 1
            continue

        raise ValueError('Warning:: Invalid Character: ' + char)

    tokens.append({
        "type": TokensType.EOF
    })
    return tokens


def parser_lexi(parser_output, tokens):
    print("parser initial value: ", parser_output)
    
    if parser_output == '1' or parser_output == '0':
        x = {"type": 'U', "value": parser_output}
        return x
    elif parser_output == 'I':
        for token in tokens:
            if token["type"] == 'I':
                return {"type": 'I', "value": token["value"]}
    else:
        print("Nothing For now. I don't know what the heck to put in here....")
        return None



# test = "A+A"
# tokens = lexi(test)

# for token in tokens:
#     print(token)






# def lexer (contents): 
#     lines = contents.split("\n")
  
    
#     # for line in lines: 
#     #     line = line.replace(' ', '')
#     #     chars = list(line)
#     #     print(chars)
#     for line in lines:
#         chars = list(line)
#         tokens = []
#         temp_str = ""
#         for char in chars:
#             if char == " ":
#                 continue
#             elif char.isalpha(): 
#                 temp_str += char
#             else:
#                 tokens.append(temp_str) if temp_str else None
#                 temp_str = "" 
#                 tokens.append(char)
#         tokens.append(temp_str)  if temp_str else None
#         print(tokens)

# def lexer(contents):
#     lines = contents.split("\n")
#     tokens_list = []
    
#     for line in lines:
#         chars = list(line)
#         tokens = []
#         temp_str = ""
#         for char in chars:
#             if char == " ":
#                 continue
#             elif char.isalpha():
#                 temp_str += char
#             elif char.isdigit() or char in ['0', '1']:
#                 temp_str += char
#             elif char == '"':
#                 if temp_str:
#                     tokens.append(temp_str)
#                     temp_str = ""
#                 string = '"'
#                 for next_char in chars[chars.index(char)+1:]:
#                     string += next_char
#                     if next_char == '"':
#                         break
#                 tokens.append(string)
#                 temp_str = ""
#             else:
#                 if temp_str:
#                     tokens.append(temp_str)
#                     temp_str = ""
#                 tokens.append(char)
#         if temp_str:
#             tokens.append(temp_str)
#         tokens_list.append(tokens)
    
#     return tokens_list

          


# def parse(input): 
#     # contents = open(file, "r").read()
#     tokens = lexer(input)
#     return tokens