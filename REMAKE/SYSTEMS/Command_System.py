def Validate_Enumbered_Choice(Possible_Choices, Choice):
    if Choice.isdigit():
        Index = int(Choice) - 1
        if 0 <= Index < len(Possible_Choices):
            return True
        return False
    return False
        
    
def Loop_Input():
    while True:
        Raw_Input = (input("> ").strip())
        
        Parts = Raw_Input.split()
        if not Parts:
            continue
        
        Command_Name = Parts[0]
        Parameters = Parts[1:]
        
        if Command_Name.lower() in Valid_Commands:
            try:
                Valid_Commands[Command_Name.lower()](*Parameters)
                
            except TypeError:
                print("INVALID COMMAND, TYPING ERROR.")
            except ValueError:
                print("INVALID COMMAND, VALUE ERROR.")
                
            continue
        
        return Raw_Input

def Target_Choice(Possible_Targets):
    while True:
        for Order, Target in enumerate(Possible_Targets):
            print(f"[ {Order + 1} ] - {Target.Name}")
        Choosed_Target = Loop_Input()
        if Validate_Enumbered_Choice(Possible_Targets, Choosed_Target):
            return Possible_Targets[int(Choosed_Target) - 1]
        print("INVALID")
        continue

def calculation(*args):
    Calculation = ("".join(args))
    
    Allowed_Characters = "0123456789+-*/().% "
    
    if any(Char not in Allowed_Characters for Char in Calculation):
        print("INVALID OPERATOR.")
        return
    try:
        Result = eval(Calculation)
        print(f">> {Result}")
        
    except Exception as Error:
        print(f"INVALID COMMAND, {type(Error).__name__.upper()}.")

Code_Context = {}

def command(*args):
    if args:
        Code = " ".join(args)
    else:
        Code_Lines = []
        print("MULTILINE CONSOLE MODE. Type 'endcons' to execute.")
        while True:
            Line = input(">> ")
            
            if Line.strip().lower() == "endcons":
                break
            Code_Lines.append(Line)
            
            Code = "\n".join(Code_Lines)
    try:
        Result = eval(Code, Code_Context)
        if Result is not None:
            print(f">> {Result}")
            
    except SyntaxError:
        
        try:
            exec(Code, Code_Context)
            
        except Exception as Error:
            print(f"INVALID COMMAND, {type(Error).__name__.upper()}.")
            
    except Exception as Error:
        print(f"INVALID COMMAND, {type(Error).__name__.upper()}.")
        
        

Valid_Commands = {
    "calc": calculation,
    "cons": command
}