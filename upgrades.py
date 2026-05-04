class UpgradeCard:
    def __init__(self, name, rarity):
        self.name = name
        self.rarity = rarity

class CardSelectionScreen:
    def __init__(self):
        self.rarity_tiers = self.create_rarity_tiers()

    def create_rarity_tiers(self):
        return ["Common", "Uncommon", "Rare", "Epic", "Legendary"]

    def display_cards(self):
        # Code to display cards according to rarity
        pass
