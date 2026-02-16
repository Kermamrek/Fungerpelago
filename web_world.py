from BaseClasses import Tutorial
from worlds.AutoWorld import WebWorld

from .options import option_groups, option_presets


class FungerWebWorld(WebWorld):
    game = "Fear & Hunger"

    theme = "stone"

    # title, description, language, filepath, link, authors
    # For potential other languages, don't translate the title and description
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "How to set up Fungerpelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["Kerma"],
    )

    tutorials = [setup_en]  # noqa: RUF012

    option_groups = option_groups
    options_presets = option_presets
