// TODO: Update these to funger values
const gameName = "Fear & Hunger";
const URLVarID = 408; //archipelago URL variable ID
const codeVarID = 409; //archipelago 5 digits variable ID
const slotVarID = 410; //archipelago slot name variable ID
const itemGetEventID = 314; //the common event that will display any updated checks
const itemSendEventID = 315; //
const itemListVarID = 413; //incoming item names are pushed to this variable to display in game
const sendListVarID = 414; //outgoing item names are pushed to this variable to display in game
const runItemGetSwitchID = 3584; //if this switch is flipped, autorun event itemGetEventID.
const runItemSendSwitchID = 3585; //same

// switchName = { //if you want a check to flip a switch, put it in here
// 	362: "OpenPhrase123",
// 	363: "test2"
// }

// get_actor_id_skill = function(id){ //if you want skills to be checks
// 	if ((id < 21 && id > 9) ||(id < 158 && id > 154)){
// 		return 1;
// 	} else if (id < 31){
// 		return 2;
// 	} else if (id < 41){
// 		return 3;
// 	} else if (id < 51){
// 		return 4;
// 	}
// 	return -1;
// }


var Rando = Rando || {}
Rando.openApClient = function(){
	console.log("opening in game " + $gamePlayer);
	Rando.client = new window.ArchipelagoModules.Client();

	client = Rando.client;

	client.messages.on("message", (content) => {
		console.log(content);
	});


	//client.login($gameVariables.value(URLVarID) + $gameVariables.value(codeVarID), $gameVariables.value(slotVarID), gameName)
	client.login("ws://localhost", "Kerma", "Fear & Hunger")
    .then(() => console.log("Connected to the Archipelago server!"))
    .catch(console.error);
	Rando.initializeItemArray();


	Rando.client.items.on("itemsReceived", (items, index) => {
		if (!$gameParty.inBattle()){
			Rando.checkForItems();
		}
	});

	//Rando.client.deathEvents.on("deathReceived", (items, index) => {
	//	Rando.deathlink();
	//});


	Rando.client.items.on("hintsInitialized", (items, index) => {
		console.log('Archipelago hints have been initialized.')
	});

	/*Rando.client.messages.on("itemSent", (text) => {
		var textArray = text.split(",");
		console.log(textArray);
		console.log('heya');
		$gameMessage.add(text);
		if (item.receiver.name == client.players.self.name){
			$gameVariables._data[itemListVarID].push(item.name);
		}
	});*/
}



Rando.initializeItemArray = function(){
	if (!$gamePlayer.APItemsReceived) {
		$gamePlayer.APItemsReceived = {};
	}
	$gameVariables._data[itemListVarID] = []
}

Rando.initializeItemGameArray = function(player){
	if (!$gamePlayer.APItemsReceived[player]) {
		$gamePlayer.APItemsReceived[player] = {};
	}
}



Rando.checkForItems = function(){
			client.items.received.forEach((item) => {
				//console.log(item);
					var playerId = item.receiver;
					Rando.initializeItemArray();
					Rando.initializeItemGameArray(playerId);
					if (!$gamePlayer.APItemsReceived[playerId][item.locationId]){
						var get = item.id;
						//console.log("Getting Item");
						$gameParty._receivedItemName = 0;
						if (get < 1000){
							$gameParty.gainItem($dataArmors[get], 1);
							$gameParty._receivedItemName = $dataArmors[get].name;
							$gameVariables._data[itemListVarID].push($dataArmors[get].name);//if you wanta symbol to appear in these, add "'[' + $dataArmors[get].iconIndex + ']' + "here
						}
						if (get > 1000 && get < 2000){
							$gameParty.gainItem($dataWeapons[get - 1000], 1);
							$gameParty._receivedItemName = $dataWeapons[get - 1000].name;
							$gameVariables._data[itemListVarID].push($dataWeapons[get - 1000].name);
						}
						if (get > 2000 && get < 3000){
							$gameParty.gainItem($dataItems[get - 2000], 1);
							$gameParty._receivedItemName = $dataItems[get - 2000].name;
							$gameVariables._data[itemListVarID].push($dataItems[get - 2000].name);
						}
						if (get > 3000 && get < 4000){//fix also give item if switch corosponds to item
							$gameSwitches.setValue(get - 3000,true);
							$gameParty._receivedItemName = switchName[get - 3000];
							$gameVariables._data[itemListVarID].push(switchName[get - 3000]);
						}
						if (get > 4000 && get < 5000){
							if ($gameActors.actor(get_actor_id_skill(get - 4000))){
								$gameActors.actor(get_actor_id_skill(get - 4000)).learnSkill(get - 4000);
							}
							$gameParty._receivedItemName = $dataSkills[get - 4000].name;
							$gameVariables._data[itemListVarID].push($dataSkills[get - 4000].name);
						}
						if (get == 3000){
							randomItemGet();
						}
						$gameSwitches.setValue(runItemGetSwitchID,true);
						$gamePlayer.APItemsReceived[playerId][item.locationId] = true;
					} else {
						//console.log("Double checking item")
							if (get < 1000){
								if (!$gameParty.hasItem($dataArmors[get])){
									$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
									Rando.itemDoubleCheck();
								}
							}
							if (get > 1000 && get < 2000){
								if (!$gameParty.hasItem($dataWeapons[get - 1000])){
									$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
									Rando.itemDoubleCheck();
								}
							}
							if (get > 2000 && get < 3000){
								if (!$gameParty.hasItem($dataItems[get - 2000])){
									$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
									Rando.itemDoubleCheck();
								}
							}
							if (get > 3000 && get < 4000){
								if (!$gameParty.members().contains($gameActors.actor(get - 3000))){
									$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
									Rando.itemDoubleCheck();
								}
							}
							if (get > 4000 && get < 5000){
								if (!$gameParty.hasItem($dataSkills[get - 4000])){
									$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
									Rando.itemDoubleCheck();
								}
							}
					}
				//}
			});
			//var blah = 0;
			var winkys = [0,0,0];
			//winkys is for progessive
			//blah is for a bunch of the same item
			client.items.received.forEach((item) => {
				var id = item.id;
				//if (id == 3000){blah++;}
				if (id == 4017){
					winkys[0] ++;
				} else if (id == 4018){
					winkys[1] ++;
				} else if (id == 4035){
					winkys[2] ++;
				}
			})
			if (!$gameParty.hasItem($dataSkills[115]) && winkys[0] > 1){
				$gameParty.hasItem($dataSkills[115]);
			}
			if (!$gameParty.hasItem($dataSkills[116]) && winkys[1] > 1){
				$gameParty.hasItem($dataSkills[116]);
			}
			if (!$gameParty.hasItem($dataSkills[39]) && winkys[2] > 1){
				$gameParty.hasItem($dataSkills[39]);
			}
			/* if ($gameParty.numItems($dataItems[40]) < blah){
				while (blah > 0){
					$gameParty.gainItem($dataItems[40], 1);
					$gameParty._receivedItemName = $dataItems[40].name;
					$gameVariables._data[itemListVarID].push('\\i[' + $dataItems[40].iconIndex + ']' + $dataItems[40].name);

					$gameSwitches.setValue(runItemGetSwitchID,true);
					blah -= 1;
				}
			} */
}

Rando.itemDoubleCheck = function(){
	client.items.received.forEach((item) => {
		var playerId = item.receiver;
		var get = (item.id);
		if (get < 1000){
			if (!$gameParty.hasItem($dataArmors[get]) && !$gameParty.isAnyMemberEquipped($dataArmors[get])){
				$gameParty.gainItem($dataArmors[get], 1);
				$gamePlayer.APItemsReceived[playerId][item.locationId] = true;
			}
		}
		if (get > 1000 && get < 2000){
			if (!$gameParty.hasItem($dataWeapons[get - 1000]) && !$gameParty.isAnyMemberEquipped($dataWeapons[get - 1000])){
				$gameParty.gainItem($dataWeapons[get - 1000], 1);
				$gamePlayer.APItemsReceived[playerId][item.locationId] = true;
			}
		}
		if (get > 2000 && get < 3000){
			if (!$gameParty.hasItem($dataItems[get - 2000])){
				$gameParty.gainItem($dataItems[get - 2000], 1);
				$gamePlayer.APItemsReceived[playerId][item.locationId] = true;
			}
		}
		if (get > 3000 && get < 4000){
			if (!$gameSwitches.value(get - 3000)){
				$gameSwitches.setValue(get - 3000,true);
				$gamePlayer.APItemsReceived[playerId][item.locationId] = false;
			}
		}
		if (get > 4000 && get < 5000){
			if (!$gameParty.hasItem($dataSkills[get - 4000]) && !$gameParty.isAnyMemberEquipped($dataSkills[get - 4000])){
				$gameActors.actor(get_actor_id_skill(get - 4000)).learnSkill(get - 4000);
				$gamePlayer.APItemsReceived[playerId][item.locationId] = true;
			}
		}
	})
}

fungerRandomizeItem = function(itemType) {
	// The common events listed are only for reference, since this function replaces them more or less
	switch(itemType){
		// Random Minor Item - Common Event 23
		case 5001:
			break;
		// Random Minor Book - Common Event 25
		case 5002:
			break;
		// Random Rare Book - Common Event 26
		case 5003:
			break;
		// Random Food Item - Common Event 52
		case 5004:
			break;
		// Random Rare Item - Common Event 58
		case 5005:
			break;
		// Random Alchemy - Common Event 68
		case 5006:
			break;
		// Random Good Armor - Common Event 141
		case 5007:
			break;
		// Random Scroll Item - Common Event 149
		case 5008:
			break;
		// Random Rare Book (Ancient) - Common Event 178
		case 5009:
			break;
		// Random Minor Book (Ancient) - Common Event 179
		case 5010:
			break;
		// Random Weapon - Common Event 238
		case 5011:
			break;
		// Random Minor Weapon - Common Event 239
		case 5012:
			break;
		// case 5013:
			// break;
		// Guard Loot - Common Event 253
		case 5014:
			break;
		// Lizardman Loot - Common Event 254
		case 5015:
			break;
		// Lord of Flies Loot - Common Event 255
		case 5016:
			break;
		// Yellow Mage Loot - Common Event 256
		case 5017:
			break;
		default:
			break;
	}
	// TODO: after switch is resolved, run check for items again somehow? is it possible or will the code have to be copied here?
}

foundLocations = []

gain = function(item) {//Run this as a script in game with the location name as the parameter.
		foundLocations.push(item)
		var get = -1;
		console.log($gamePlayer.locationsRaw)
		for(const i of $gamePlayer.locationsRaw){
			if (i.locationName == item){
				get = i.locationId;
				break;
			}
		}
		console.log("sent location " + item + " with ID " + get);
		//Ask the client to send the item in question; If it's a Silver Daze item, the client will send it to us.
		//We can do this by storing all of the items that are received by the player in an array, then checking every couple frames if that item has been sent/received.
		//This will prevent duplicates, as well as "duds" that don't send, if the player loses connection with the client.
		//If the game isn't Archipelago, then we'll give the item to the player through normal means.
		//We should also error log if the game isn't connected to the client.
		Rando.client.check(get);
		if ($gamePlayer.locationScout[get].receiver.name !== client.players.self.name && $gamePlayer.locationScout[get].receiver.name !== undefined ||
		    $gamePlayer.locationScout[get].game !== gameName){
			if ($gamePlayer.locationScout[get].receiver.name == undefined){
				$gameVariables._data[sendListVarID].push($gamePlayer.locationScout[get].name + ' for ' + 'someone else');
			}else{
				$gameVariables._data[sendListVarID].push($gamePlayer.locationScout[get].name + ' for ' + $gamePlayer.locationScout[get].receiver.name);
			}
			$gameSwitches.setValue(runItemGetSwitchID,true);

		}
		if ($gamePlayer.locationScout[get].offline){
			var id = $gamePlayer.locationScout[get].id;
				$gameParty._receivedItemName = 0;
				if (id < 1000){
					$gameParty.gainItem($dataArmors[id], 1);
					$gameParty._receivedItemName = $dataArmors[id].name;
					$gameVariables._data[itemListVarID].push($dataArmors[id].name);
				}
				if (id > 1000 && id < 2000){
					$gameParty.gainItem($dataWeapons[id - 1000], 1);
					$gameParty._receivedItemName = $dataWeapons[id - 1000].name;
					$gameVariables._data[itemListVarID].push($dataWeapons[id - 1000].name);
				}
				if (id > 2000 && id < 3000){
					$gameParty.gainItem($dataItems[id - 2000], 1);
					$gameParty._receivedItemName = $dataItems[id - 2000].name;
					$gameVariables._data[itemListVarID].push($dataItems[id - 2000].name);
				}
				if (id > 3000 && id < 4000){
					$gameSwitches.setValue(id - 4000,true);
					$gameParty._receivedItemName = switchName[id - 4000];
					$gameVariables._data[itemListVarID].push(switchName[id - 4000]);
				}
				if (id > 4000 && id < 5000){
					$gameParty.gainItem($dataSkills[id - 4000], 1);
					$gameParty._receivedItemName = $dataSkills[id - 4000].name;
					$gameVariables._data[itemListVarID].push($dataSkills[id - 4000].name);
				}
				if (id > 5000){//this is for errors I think?? Ask Sawer about it
					console.log('Archipelago');
					if (Archipelago[id - 5000]){
						$gameVariables._data[itemListVarID].push('\\i[193]' + Archipelago[id - 5000].name);
					} else {
						$gameVariables._data[itemListVarID].push('\\i[193] Archipelago Item');
					}
				}
				$gameTemp.reserveCommonEvent(itemGetEventID);
			}
}
Rando.initializeLocationScout = function(){ //locationScout is basically a way to get all info from any check.
	$gamePlayer.locationScout = $gamePlayer.locationScout || []
	$gamePlayer.locationsRaw.forEach((item) => {
         $gamePlayer.locationScout[item.locationId] = {};
         $gamePlayer.locationScout[item.locationId]['id'] = item.id;
         $gamePlayer.locationScout[item.locationId]['locationGame'] = item.locationGame;
         $gamePlayer.locationScout[item.locationId]['locationId'] = item.locationId;
         $gamePlayer.locationScout[item.locationId]['locationName'] = item.locationName;
         $gamePlayer.locationScout[item.locationId]['name'] = item.name;
         $gamePlayer.locationScout[item.locationId]['filler'] = item.filler;
         $gamePlayer.locationScout[item.locationId]['flags'] = item.flags;
         $gamePlayer.locationScout[item.locationId]['game'] = item.game;
         $gamePlayer.locationScout[item.locationId]['progression'] = item.progression;
         $gamePlayer.locationScout[item.locationId]['receiver'] = item.receiver;
         $gamePlayer.locationScout[item.locationId]['sender'] = item.sender;
         $gamePlayer.locationScout[item.locationId]['trap'] = item.trap;
         $gamePlayer.locationScout[item.locationId]['useful'] = item.useful;
})
	Object.entries(Location).forEach((place) => {
		if (!$gamePlayer.locationScout[place[1]]) {
			$gamePlayer.locationScout[place[1]] = {};
			$gamePlayer.locationScout[place[1]]['id'] = randoItem.id;
			$gamePlayer.locationScout[place[1]]['locationGame'] = gameName;
			$gamePlayer.locationScout[place[1]]['locationId'] = place[1];
			$gamePlayer.locationScout[place[1]]['locationName'] = place[0];
			$gamePlayer.locationScout[place[1]]['name'] = randoItem.name;
			$gamePlayer.locationScout[place[1]]['filler'] = true;
			$gamePlayer.locationScout[place[1]]['flags'] = [];
			$gamePlayer.locationScout[place[1]]['game'] = gameName;
			$gamePlayer.locationScout[place[1]]['progression'] = false;
			$gamePlayer.locationScout[place[1]]['receiver'] = client.name;
			$gamePlayer.locationScout[place[1]]['sender'] = client.name;
			$gamePlayer.locationScout[place[1]]['trap'] = false;
			$gamePlayer.locationScout[place[1]]['useful'] = false;
			$gamePlayer.locationScout[place[1]]['offline'] = true;
		} else {
		}
	})
	Object.freeze($gamePlayer.locationScout);
};

// Rando.hasBeenFound = function(name) {
// 	for (const i of foundLocations) {
// 		if (name == i) {
// 			return true;
// 		}
// 	}
// 	return false;
// }
//
// win = function(winCon) { //at every possible win, run this with the win index.
// 	if (!$gameSwitches._data[403]&&winCon==0){
// 		Rando.client.goal()
// 	}
// 	if ($gameSwitches._data[403]&&winCon==1){
// 		Rando.client.goal()
// 	}
// }
