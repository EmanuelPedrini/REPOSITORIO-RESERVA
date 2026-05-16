def Validate_Enumbered_Choice(Possible_Choices, Choice):
    if Choice.isdigit():
        Index = int(Choice) - 1
        if 0 <= Index < len(Possible_Choices):
            return True
        return False
    return False
        
    
def Loop_Input():
    Input = input("> ")
    return Input

def Target_Choice(Possible_Targets):
    while True:
        for Order, Target in enumerate(Possible_Targets):
            print(f"[ {Order + 1} ] - {Target.Name}")
        Choosed_Target = Loop_Input()
        if Validate_Enumbered_Choice(Possible_Targets, Choosed_Target):
            return Possible_Targets[int(Choosed_Target) - 1]
        print("INVALID")
        continue