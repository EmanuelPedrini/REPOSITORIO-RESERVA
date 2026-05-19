from SYSTEMS.Command_System import Loop_Input, Validate_Enumbered_Choice
from PUBLIC.Public_Standards import *
from PUBLIC.Public_Enums import _DAMAGE_TYPE
from PUBLIC.Public_Classes import DAMAGE


class EVENT_TARGETING:

    @staticmethod
    def Random_Member(Party, Event_Targets=None):
        if not Party:
            return []
        return [random.choice(Party)]

    @staticmethod
    def All_Members(Party, Event_Targets=None):
        return Party

    @staticmethod
    def Event_Targets(Party, Event_Targets):
        return Event_Targets

    @staticmethod
    def No_Target(Party, Event_Targets=None):
        return []


class EVENT:
    def __init__(
        self,
        Name: str,
        Text: str,
        Choices: list,
        Scene_Targeting=EVENT_TARGETING.No_Target
    ):
        self.Name = Name
        self.Text = Text
        self.Choices = Choices
        self.Scene_Targeting = Scene_Targeting

    @staticmethod
    def Resolve_Text(Text, Interacted):
        if callable(Text):
            return Text(Interacted)
        return Text

    def Event_Screen(self, Interacted):
        Log = []

        Log.append(f"EVENT: {self.Resolve_Text(self.Name, Interacted)}")
        Log.append(self.Resolve_Text(self.Text, Interacted))

        for Order, (Choice_Text, _, _) in enumerate(self.Choices, 1):
            Log.append(
                f"[ {Order} ] - {self.Resolve_Text(Choice_Text, Interacted)}"
            )
        return "\n".join(Log)

    def Render_Event_Screen(self, Interacted):
        print(self.Event_Screen(Interacted))

    def Trigger(self, Party):
        Scene_Targets = self.Scene_Targeting(Party)
        Interacted = Scene_Targets[0] if Scene_Targets else None
        while True:
            self.Render_Event_Screen(Interacted)
            Choice = Loop_Input()
            if Choice.isdigit():
                if Validate_Enumbered_Choice(self.Choices, Choice):
                    Choice_Index = int(Choice) - 1
                    _, Effect, Choice_Targeting = self.Choices[Choice_Index]
                    Targets = Choice_Targeting(Party, Scene_Targets)
                    Result = Effect(Targets)
                    if Result:
                        print(Result)
                    break
                print("INVALID")
                continue
            print("INVALID")

def Avoid(Targets):
    Log = []
    for Target in Targets:
        Roll = random.randint(1, 100)
        if Roll <= 40:
            Damage = random.randint(30, 60)
            Damage_Taken = Target.Take_Damage(
                DAMAGE(Damage, _DAMAGE_TYPE.SLASHING, None)
            )
            Log.append(
                f"{Target.Name} accidentally stepped on the trap "
                f"and took {Damage_Taken} damage!"
            )
        else:
            Log.append(
                f"{Target.Name} avoided the trap in an involuntary reflex!"
            )
    return "\n".join(Log)


def Drink_Fountain(Targets):
    Log = []
    for Target in Targets:
        Heal = random.randint(50, 65)
        Real_Heal = Target.Heal(Heal)
        Log.append(
            f"{Target.Name} drinks from the fountain "
            f"and heals {Real_Heal} HEALTH!"
        )
    return "\n".join(Log)

def Nothing(Targets):
    return "NOTHING HAPPENS!"

Stones_on_the_Path = EVENT(
    Name="STONES IN THE PATH",
    Text="You encounter different rocks in the path and decide to take a look.",
    Choices=[
        ("Look under the rocks", Nothing, EVENT_TARGETING.No_Target)
    ],
    Scene_Targeting=EVENT_TARGETING.No_Target
)


Stepping_on_Bear_Trap = EVENT(
    Name="BEAR TRAP?!!",

    Text=lambda Interacted:
        f"{Interacted.Name} is distracted and is about to step on a BEAR TRAP!",

    Choices=[
        (lambda Interacted: f"Tell {Interacted.Name} to avoid it!", Avoid, EVENT_TARGETING.Event_Targets)
        ],
    Scene_Targeting=EVENT_TARGETING.Random_Member
)


Healing_Fountain = EVENT(
    Name="HEALING FOUNTAIN",
    Text="The party finds an imposing fountain with healing magic symbols. Drink?",
    Choices=[
        ("Ignore", Nothing, EVENT_TARGETING.No_Target),
        ("Drink", Drink_Fountain, EVENT_TARGETING.All_Members)
    ],
    Scene_Targeting=EVENT_TARGETING.No_Target
)