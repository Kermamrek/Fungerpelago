from dataclasses import dataclass

from Options import Choice, OptionGroup, PerGameCommonOptions, Toggle

# For further reading on options, you can also read the Options API Document:
# https://github.com/ArchipelagoMW/Archipelago/blob/main/docs/options%20api.md
# And APQuest example:
# https://github.com/NewSoupVi/Archipelago/blob/apquest/worlds/apquest/options.py

class CharacterChoice(Choice):
    """
    The character you will choose to play as.
    This is dictated here instead of the in-game character select screen as some endings and items
    require certain characters to be chosen.
    """

    display_name = "Character"

    option_mercenary = 0
    option_knight = 1
    option_dark_priest = 2
    option_outlander = 3
    # Annoyingly, "option_random" is reserved, so putting in an extra m until I can figure out alternative
    option_randomm = 4

    default = option_mercenary


class DifficultyChoice(Choice):
    """
    Which difficulty you will play on. Each difficulty has various changes to gameplay and mechanics.
    You cannot save in Hard Mode. Fear & Hunger is recommended for new players.
    """

    display_name = "Difficulty"

    option_fear_and_hunger = 0
    option_terror_and_starvation = 1
    option_hard_mode = 2

    default = option_fear_and_hunger


class EndingChoice(Choice):
    """
    Which ending the player must complete to release all checks.
    Generally, the endings go from longest to shortest, with ending A being the most complete experience.
    Choosing "Any" will let you get any ending, which is recommended for brand new players.

    Ending "S" MUST be played on "Hard Mode" difficulty, varies based on the character chosen,
    and is only recommended for veterans.
    """

    display_name = "Ending"

    option_ending_a = 0
    option_ending_b = 1
    option_ending_c = 2
    option_ending_d = 3
    option_ending_e = 4
    option_ending_s = 5
    option_ending_any = 6

    default = option_ending_a


class StartDash(Toggle):
    """
    Dash is a skill that allows you to run faster.
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
class FungerOptions(PerGameCommonOptions):
    character: CharacterChoice
    difficulty: DifficultyChoice
    ending: EndingChoice
    start_with_dash: StartDash
    skip_coin_flip: SkipCoinFlip


option_groups = [
    OptionGroup(
        "Important Gameplay Options",
        [CharacterChoice, DifficultyChoice, EndingChoice],
    ),
    OptionGroup(
        "Other Gameplay Options",
        [StartDash],
    ),
    OptionGroup(
        "Quality of Life",
        [SkipCoinFlip],
    ),
]

option_presets = {
    "Recommended": {
        "character": CharacterChoice.option_randomm,
        "difficulty": DifficultyChoice.option_fear_and_hunger,
        "ending": EndingChoice.option_ending_a,
        "start_with_dash": True,
        "skip_coin_flip": False,
    },
    "Vanilla": {
        "character": CharacterChoice.option_mercenary,
        "difficulty": DifficultyChoice.option_fear_and_hunger,
        "ending": EndingChoice.option_ending_any,
        "start_with_dash": False,
        "skip_coin_flip": False,
    },
}
