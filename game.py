from bases import Bases

class Game:
    def __init__(self, away: object, home :object):
        # game stats
        self.inning = 1
        self.halfInn = "TOP"         #halfInn can be "TOP" or "BOTTOM"
        self.outs = 0
        self.gameState = None
        self.bases = [None, None, None, None]     # 0 index is batter, 1 is first base, 2 is second base, 3 is third

        # team stats  -- update to include score
        self.hTeam = home
        self.aTeam = away
        self.aTeamScore = 0
        self.hTeamScore = 0

    def clear_Out(self):
        """Updates number of outs and checks whether inning is over.  set_Out does not return anything"""
        self.outs = 0

    def inc_Out(self, out = 1):
        """Updates number of outs and checks whether inning is over.  set_Out does not return anything"""
        self.outs += out
        if self.outs >= 3:
            self.updateInning()

    def get_Out(self):
        """Returns number of outs"""
        return self.outs

    def updateInning(self):
        """updates inning to next available inning, calls gameState if end of top of 9th inning or bottom of 9th inning
        """
        if self.inning == 9:
            self.gameCheck()
            # if game is over return

        if self.halfInn == "BOTTOM":
            self.inning += inning
            self.halfInn =="TOP"
            self.clear_Out()
        else:
            self.halfInn == "BOTTOM"
            self.clear_Out()

    def clear_Bases(self):
        pass

    def update_Bases(self, update: list):
        pass

    def get_Bases(self):
        pass

    def gameCheck(self):
        pass

    def updateScore(self):
        pass





