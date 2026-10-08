URGENT:
* Fix randomization on items (so they are the same every time)
* Implement proper name/server entry
* Clean up fungerpelago plugin more, most of the old code from previous repos have been cleaned but could use some extra clarification
* Fix display for random items so you always know what you're getting. Additionally, getting stuff like blue herbs from barrels and crates says "nothing left here"
* I've noticed that getting items sent to you all at once (IE, when you continue a game or potentially if you got sent multiple things at once) bugs out and only sends one. This was obvious when I looted 4 rooms fully, died, then respawned and noticed that I only had 6 items total. I think the dialogue box is causing this with `Random ____ item` specifically, as things that are just generic items you get successfully. The message box blocks even you getting one item depending on if you get one when you wake up. Hard to phrase correctly, but for example if you sleep and wake up in the prison bed there will be a message box saying "you didn't get very good sleep" or something and that will block you from even getting the first random item. This is a bit of a larger issue because I was actually planning on "fixing" the non-random items you get by having them properly give dialogue boxes, but now dialogue boxes seem pretty bugged and an alternative solution might be needed. At first I was thinking a queue system, but not sure what the best way to program that would be and it would create an alternative problem where dying after doing a huge portion of the game and continuing would make you have to mash through 30 dialogue boxes. In some extreme cases I could see this creating a death loop where the dogs maul you to death at the start before you're even allowed to move. So might be worth figuring out ways to avoid this sort of thing

Following items I noticed weren't added:
* Table with list of inmates and random item (captain's room) (C, but could be more)


Considerations:

* How does saving work?
* How do endings work? Should the player have to choose what ending they need to get to release all checks before they start the game? If not, runs could last a total of 10 minutes by getting the legarde escape ending.
* How does randomization of items work? The current idea is to have the "RANDOM FOOD ITEM", "RANDOM BOOK", etc sent instead of sending specific items. But how can we ensure that the player receives the exact same roll every time so they don't have drastically different gameplay experiences upon relaunching the game? Should another method be taken instead?
* How do coin flips work? I think it would be funny if sending something that would send a coin flip check (bookcase, etc), but how do we ensure that this coinflip stays saved? Should it be seeded and predetermined (but the player wouldn't know)
* Dream rondon loot? Currently ignored it, but should it be a toggle? It's completely missable (however there is other missable items that we added and the game is short enough)

Items:

* Empty scroll needs to be rebalanced. The plan is to remove most things that could make the game trivial, even if this slightly tampers with the original spirit of the game. To this end, the hints also need to be adjusted so no hint is given for invalid items.
* Should we give the player 3 torches or so if they start in Terror & Starvation/Hard Mode? Or at least make it an option?
* Book of enlightenment does not work in hard mode. We might be able to remove it from the item pools when hard mode is not being played, but would something more interesting be a better option? Can we let the player use it as a sort of archipelago hint similar to an empty scroll text input?
* In the mines levels, add a way to see what item is there before using the tinderbox. That way you can decide if you want to sacrifice the item or not (could this be savescummed? can we prevent that?)
* Crow mauler?

Shops:

* Solve Pocketcat needing the girl to trade for AP items. Immediate thought is a setting that allows him to take your limbs instead. Should you be forced to save?
* Suspicious merchant selling trap items for other players disguised as regular items?

Options:

* Random seed option? Should all randomization take from this? Does archipelago client have support for "random" button or would players have to enter a random int? This could solve a lot of the game's randomization issues, such as areas, items, etc
* "Start with Dash"
* Shop options, such as pocketcat limbs/girl, and pocketcat dropdown of "includes any item/only useful+filler/only filler"
* Chosen ending (see considerations, we both think that having to choose your ending in advance is a good approach)

Etc:

* Archipelago logo sprite needs to be made
* Can the book of forgotten memories maybe contain memories relating to other games? "Memories of your past life flash before your eyes. But some of these memories are not of yours." This will take a lot of work as a snippet would have to be written for most games currently released, but would be fun to do (I think at least)
* Some things like the empty scroll will require new written dialogue, the plan is to introduce a tongue-in-cheek ish god while still retaining the original game's flavour. The current idea is "Saa'risto" which is finnish for "Archipelago" (and also a name in finland), but this can be subject to change
