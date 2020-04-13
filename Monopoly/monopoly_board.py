import numpy as np

class Chance:
    def no_move(self, arg):
        return arg
    
    # ride reading railroad
    def rrr_move(self, arg):
        return 4
    
    def go_jail_move(self, arg):
        return 10
    
    # nearest utility
    def n_u_move(self, space):
        if space < 12:
            return 12
        elif space < 28:
            return 28
        else:
            return 12
    
    # nearest railroad
    def n_r_move(self, space):
        if space < 5:
            return 5
        elif space < 15:
            return 15
        elif space < 25:
            return 25
        elif space < 35:
            return 35
        else:
            return 5
        
    def gb3_move(self, space):
        return space - 3
    
    def g2g_move(self, arg):
        return 0
    
    # Illinois Ave.
    def ia_move(self, arg):
        return 24
    
    # St. Charles Place
    def scp_move(self, arg):
        return 11
    
    # Boardwalk
    def b_move(self, arg):
        return 39
    
    deck = {
        0: {
            "name": "Reading Railroad",
            "move": rrr_move
        },
        1: {
            "name": "Property Repairs",
            "move": no_move
        },
        2: {
            "name": "Go To Jail",
            "move": go_jail_move
        },
        3: {
            "name": "Poor Tax",
            "move": no_move
        },
        4: {
            "name": "Nearest Utility",
            "move": n_u_move
        },
        5: {
            "name": "Nearest Railroad",
            "move": n_r_move
        },
        6: {
            # yes there are two of these cards
            "name": "Nearest Railroad 2",
            "move": n_r_move
        },
        7: {
            "name": "Go Back 3",
            "move": gb3_move
        },
        8: {
            "name": "Go to Go",
            "move": g2g_move
        },
        9: {
            "name": "Illinois Ave.",
            "move": ia_move
        },
        10: {
            "name": "St. Charles Place",
            "move": scp_move
        },
        11: {
            "name": "Receive Dividend",
            "move": no_move
        },
        12: {
            "name": "Building and Loan",
            "move": no_move
        },
        13: {
            "name": "Get Out of Jail Free",
            "move": no_move,
            "gojf": True
        },
        14: {
            "name": "Go to Boardwalk",
            "move": b_move
        },
        15: {
            "name": "Elected Chairman",
            "move": no_move
        }
    }
    
    deck_order = np.arange(len(deck))
    position_in_deck = 0
    
    def shuffle_deck(self):
        np.random.shuffle(self.deck_order)
    
    def pick_card(self, space):
        if self.position_in_deck > len(self.deck_order)-1:
            self.shuffle_deck()
            self.position_in_deck = 0
        
        # handle card picking and iterating tasks
        card_index = self.deck_order[self.position_in_deck]
        self.position_in_deck +=1
        
        # handle card resolution tasks
        new_space = self.deck[card_index]["move"](self, space)
        
        return new_space, self.deck[card_index]

class CommunityChest:
    def no_move(self, arg):
        return arg
    
    def go_jail_move(self, arg):
        return 10
    
    def g2g_move(self, arg):
        return 0
    
    deck = {
        0: {
            "name": "Life Insurance",
            "move": no_move
        },
        1: {
            "name": "Bank Error",
            "move": no_move
        },
        2: {
            "name": "Go To Jail",
            "move": go_jail_move
        },
        3: {
            "name": "Collect $50 From Every Player",
            "move": no_move
        },
        4: {
            "name": "Pay Hospital",
            "move": no_move
        },
        5: {
            "name": "XMAS Fund Matures",
            "move": no_move
        },
        6: {
            "name": "Get Out of Jail Free",
            "move": no_move,
            "gojf": True
        },
        7: {
            "name": "Pay School Tax",
            "move": no_move
        },
        8: {
            "name": "Inherit $100",
            "move": no_move
        },
        9: {
            "name": "Go to Go",
            "move": g2g_move
        },
        10: {
            "name": "Doctor's Fee",
            "move": no_move
        },
        11: {
            "name": "Receive For Services",
            "move": no_move
        },
        12: {
            "name": "Assessed Street Repairs",
            "move": no_move
        },
        13: {
            "name": "Beauty Contest",
            "move": no_move
        },
        14: {
            "name": "Sale of Stock",
            "move": no_move
        },
        15: {
            "name": "Income Tax Refund",
            "move": no_move
        }
    }
    
    deck_order = np.arange(len(deck))
    position_in_deck = 0
    
    def shuffle_deck(self):
        np.random.shuffle(self.deck_order)
    
    def pick_card(self, space):
        if self.position_in_deck > len(self.deck_order)-1:
            self.shuffle_deck()
            self.position_in_deck = 0
        
        # handle card picking and iterating tasks
        card_index = self.deck_order[self.position_in_deck]
        self.position_in_deck +=1
        
        # handle card resolution tasks
        new_space = self.deck[card_index]["move"](self, space)
        
        return new_space, self.deck[card_index]


class GameBoard:
    c_deck = Chance()
    cc_deck = CommunityChest()

    game_board = {
        0: {
            "name": "Go",
            "color": "Black"
        },
        1: {
            "name": "Mediteranean Ave",
            "color": "Purple"
        },
        2: {
            "name": "Community Chest",
            "color": "pink"
        },
        3: {
            "name": "Baltic Ave",
            "color": "Purple"
        },
        4: {
            "name": "Income Tax",
            "color": "Black"
        },
        5: {
            "name": "Reading Railroad",
            "color": "gray"
        },
        6: {
            "name": "Oriental Ave", 
            "color": "cyan"
        },
        7: {
            "name": "Chance",
            "color": "pink"
        },
        8: {
            "name": "Vermont Ave",
            "color": "cyan"
        },
        9: {
            "name": "Connecticut Ave",
            "color": "cyan"
        },
        10: {
            "name": "Jail",
            "color": "black"
        },
        11: {
            "name": "St. Charles Place",
            "color": "magenta"
        },
        12: {
            "name": "Electric Company",
            "color": "brown"
        },
        13: {
            "name": "States Ave",
            "color": "magenta"
        },
        14: {
            "name": "Virginia Ave",
            "color": "magenta"
        },
        15: {
            "name": "Pensylvania Railroad",
            "color": "gray"
        },
        16: {
            "name": "St. James Place",
            "color": "orange"
        },
        17: {
            "name": "Community Chest",
            "color": "pink"
        },
        18: {
            "name": "Tennessee Ave",
            "color": "orange"
        },
        19: {
            "name": "New York Ave",
            "color": "orange"
        },
        20: {
            "name": "Free Parking",
            "color": "black"
        },
        21: {
            "name": "Kentucky Ave",
            "color": "red"
        },
        22: {
            "name": "Chance",
            "color": "pink"
        },
        23: {
            "name": "Indiana Ave",
            "color": "red"
        },
        24: {
            "name": "Illinois Ave",
            "color": "red"
        },
        25: {
            "name": "B&O Railroad",
            "color": "gray"
        },
        26: {
            "name": "Atlantic Ave",
            "color": "yellow"
        },
        27: {
            "name": "Ventnor Ave",
            "color": "yellow"
        },
        28: {
            "name": "Water Works",
            "color": "brown"
        },
        29: {
            "name": "Marvin Gardens",
            "color": "yellow"
        },
        30: {
            "name": "Go To Jail",
            "color": "black"
        },
        31: {
            "name": "Pacific Ave",
            "color": "green"
        },
        32: {
            "name": "North Carolina Ave",
            "color": "green"
        },
        33: {
            "name": "Community Chest",
            "color": "pink"
        },
        34: {
            "name": "Pennsylvania Ave",
            "color": "green"
        },
        35: {
            "name": "Short Line Railroad",
            "color": "gray"
        },
        36: {
            "name": "Chance",
            "color": "pink"
        },
        37: {
            "name": "Park Place",
            "color": "blue"
        },
        38: {
            "name": "Luxury Tax",
            "color": "black"
        },
        39: {
            "name": "Boardwalk",
            "color": "blue"
        }
    }

    jail=True
    chance=True
    community_chest=True
    jail_doubles=True
    jail_gojf=True

    x_labels = []
    x_label_colors = []
    for i in range(40):
        x_labels.append(game_board[i]["name"])
        x_label_colors.append(game_board[i]["color"])

    def check_special_rules(self, space):
        # Jail
        new_space = space
        in_jail = 0
        card = {}

        if self.jail:
            if space == 30:
                new_space = 10
                in_jail = 1
        
        # Chance
        if self.chance:
            if space in [7, 22, 36]:
                new_space, card = self.c_deck.pick_card(space)
                if new_space != space:
                    new_space, in_jail, card = self.check_special_rules(new_space)
            
        # Community Chest
        if self.community_chest:
            if space in [2, 17, 33]:
                # pick a card from community chest
                new_space, card = self.cc_deck.pick_card(space)
                if new_space != space:
                    new_space, in_jail, card = self.check_special_rules(new_space)
        
        new_space = new_space % 40
        return new_space, in_jail, card

    # Helper for dice rolls
    def roll_dice(self, nrolls = 10000):
        # creates a list nrolls long of 2 dice dice rolls
        rng = np.random.default_rng()
        samples_a = rng.integers(low = 1, high = 6, size = nrolls, endpoint=True)
        samples_b = rng.integers(low = 1, high = 6, size = nrolls, endpoint=True)
        samples_sum = samples_a+samples_b
        doubles = []
        for i in range(len(samples_a)):
            if samples_a[i] == samples_b[i]:
                doubles.append(1)
            else:
                doubles.append(0)

        return samples_sum, doubles

    def walk_piece_get_histo(self, nrolls):

        dice_rolls, doubles = self.roll_dice(nrolls)

        space = 0
        board_positions = [0]
        in_jail = 0
        play = True
        gojf_cards = 0
        gojf_count = 0

        for i in np.arange(len(dice_rolls)):
            roll = dice_rolls[i]

            # assuming we are playing with "get out of jail free" cards, and you have one, you will use it
            # for now we're assuming an infinite number of gojf cards
            if self.jail_gojf and gojf_cards > 0:
                gojf_cards -= 1
                play = True
                in_jail = 0

            # either you didn't have a GOJF card or didn't use it. now let's see if you roll doubles
            # playing with "roll doubles to get out of jail" rules
            elif self.jail_doubles:
                if in_jail > 0:
                    if in_jail > 2:
                        in_jail = 0
                        play = True
                    else:
                        in_jail += 1
                        play = False
                        if doubles[i] == 1:
                            in_jail = 0
                            play = True

            if play:
                space, in_jail, card = self.check_special_rules(space + roll)
                board_positions.append(space)
                # check for get out of jail free cards
                if "gojf" in card.keys():
                    gojf_cards+=1
                    gojf_count+=1
            else:
                # you're stuck in jail
                pass

        print("gojf_cards"+str(gojf_cards))
        print("gojf_count"+str(gojf_count))
        return np.histogram(board_positions, bins=np.arange(41))

    def update_play_options(self, jail=True, chance=True, community_chest=True, jail_doubles=True, jail_gojf=True):
        self.jail = jail
        self.chance = chance
        self.community_chest = community_chest
        self.jail_doubles = jail_doubles
        self.jail_gojf = jail_gojf