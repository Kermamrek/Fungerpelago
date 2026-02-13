from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets

class FungerWebWorld(WebWorld):
    game = "Fear & Hunger"

    theme = "stone"

    # title, description, language, filepath, link, authors
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up APQuest for MultiWorld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kerma"],
    )

    # Leaving in case we add a finnish guide or something
    # Do not translate the title and description!
    # setup_de = Tutorial(
    #     "Multiworld Setup Guide",
    #     "A guide to setting up APQuest for MultiWorld.",
    #     "German",
    #     "setup_de.md",
    #     "setup/de",
    #     ["NewSoupVi"],
    # )
    tutorials = [setup_en]

    option_groups = option_groups
    options_presets = option_presets
