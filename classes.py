class Bet:
    """general data class for easier access from DataFrame"""
    def __init__(self, user_id: str, stake: float, lot: float):
        self.user_id = user_id
        self.stake = stake
        self.lot = lot

    def __str__(self):
        s = str({
            "user_id": self.user_id,
            "stake": self.stake,
            "lot": self.lot
        })
        return s

    def to_dict(self):
        return {
                    "user_id": self.user_id,
                    "bet": self.stake,
                    "lot": self.lot
                }
        # return s


