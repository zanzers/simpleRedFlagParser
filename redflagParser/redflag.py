
#OR = R;
#AND = A;
#INPUT = I:A,B,C,D;
#NOT = N:A,B,C,D;
#DNI = DN: A,B,C,D;
#();
#NUMBER = 1 OR 0;

#HS: single Output OR input;
#RHS: more than one input OR output;
# Still On Process;

class Fail(Exception):
    def __init__(self, message="Default Error Message"):
        super().__init__(message)

def redFlags(input_str):
    print("input from redflag: ",input_str)
    count = 0
    hash_table = {}

    def eval():
        nonlocal count
        try:
            return Goal(0)["num"]
        except Fail as e:
            if isinstance(e, Fail):
                return "Cannot parse input"
            else:
                raise e

    def say(msg):
        nonlocal count
        print(msg)
        print("STEPS:", count)
        print()

    def Goal(position):
        result = And(position)
        eof(result["position"])
        return result

# GRAMMAR RULES || PRODUCTION START HERE!
    def And(position):
        nonlocal count
        try:
            varA = packman('I', position)
            gate = packman('A', varA["position"])
            rhs = packman('I', gate["position"])
            return {"num": 'I', "position": rhs["position"]}
        except Fail:
            try:
                varA = packman('I', position)
                gate = packman('A', varA["position"])
                rhs = packman('N', gate["position"])
                return {"num": '0', "position": rhs["position"]}
            except Fail:
                try:
                    varA = packman('I', position)
                    gate = packman('A', varA["position"])
                    rhs = packman('1', gate["position"])
                    return {"num": 'I', "position": rhs["position"]}
                except Fail:
                    try:
                        varA = packman('I', position)
                        gate = packman('A', varA["position"])
                        rhs = packman('0', gate["position"])
                        return {"num": '0', "position": rhs["position"]}
                    except Fail:
                        return Or(position)

    def Or(position):
        nonlocal count
        try:
            varA = packman('I', position)
            gate = packman('R', varA["position"])
            rhs = packman('I', gate["position"])
            return {"num": 'I', "position": rhs["position"]}
        except Fail:
            try:
                varA = packman('I', position)
                gate = packman('R', varA["position"])
                rhs = packman('N', gate["position"])
                return {"num": '1', "position": rhs["position"]}
            except Fail:
                try:
                    varA = packman('I', position)
                    gate = packman('R', varA["position"])
                    rhs = packman('1', gate["position"])
                    return {"num": '1', "position": rhs["position"]}
                except Fail:
                    try:
                        varA = packman('I', position)
                        gate = packman('R', varA["position"])
                        rhs = packman('0', gate["position"])
                        return {"num": 'I', "position": rhs["position"]}
                    except Fail:
                       pass

  
# GRAMMAR RULES || PRODUCTION END HERE!

    def packman(c, position):
        nonlocal count, hash_table
        if position >= len(input_str):
            raise Fail()  
        if c in hash_table and position in hash_table[c]:
            return hash_table[c][position]
        if input_str[position] == c:
            result = {"num": 1, "position": position + 1}
            if c not in hash_table:
                hash_table[c] = {}
            hash_table[c][position] = result
            return result
        raise Fail()

    def eof(position):
        nonlocal count
        if position <= len(input_str):
            return {"num": 1, "position": position}
        raise Fail()

    return {"eval": eval, "count": count}


# Example usage:
# input_str = "IR1"
# parser = redFlags(input_str)
# print(input_str)
# print("Result:", parser["eval"]())
# print("Steps:", parser["count"])