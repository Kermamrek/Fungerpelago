from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Toggle


# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md
# And APQuest example:
# https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/options.py

class EndingChoice(Choice):
    """
    Which ending the player must complete to release all checks.
    Generally, the endings go from longest to shortest, with ending A being the intended experience.
    Choosing "Any" will let you get any ending, which is recommended for brand new players.
    """

    display_name = "Ending"

    ending_a = 0
    ending_b = 1
    ending_c = 2
    ending_d = 3
    ending_e = 4
    ending_any = 5

    default = ending_a

class StartDash(Toggle):
    """
    Dash is a skill that lets you hold a button down to run faster.
    Characters can start with it, but you need to know the options to pick at the start of the game.
    This option ensures you have dash at the start of the game, by auto-picking the option for you.
    """

    display_name = "Always Pick Dash"

class SkipCoinFlip(Toggle):
    """
    If an APItem is sent to you that would trigger a coin flip (bookshelf loot, etc), this option
    automatically skips it and gives you the result of the coin flip immediately.
    Turning this on does not alter the result at all, but is it really Fear & Hunger without coin flips?
    """

    display_name = "Skip Item Coin Flips"

# We must now define a dataclass inheriting from PerGameCommonOptions that we put all our options in.
# This is in the format "option_name_in_snake_case: OptionClassName".
@dataclass
class APQuestOptions(PerGameCommonOptions):
    ending_choice: EndingChoice
    start_with_dash: StartDash
    skip_coin_flip: SkipCoinFlip

option_groups = [
    OptionGroup(
        "Gameplay Options",
        [EndingChoice, StartDash],
    ),
    OptionGroup(
        "Quality of Life",
        [SkipCoinFlip],
    ),
]

option_presets = {
    "Recommended": {
        "ending_choice": EndingChoice.ending_a,
        "start_with_dash": True,
        "skip_coin_flip": False,
    },
    "Vanilla": {
        "ending_choice": EndingChoice.ending_any,
        "start_with_dash": False,
        "skip_coin_flip": False,
    },
}
