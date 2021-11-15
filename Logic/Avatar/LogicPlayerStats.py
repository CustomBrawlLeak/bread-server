class LogicPlayerStats:

    def getPlayerStats(self, accountData):

        playerStats = {

            '3v3Victories': 0,
            'ExperiencePoints': accountData['ExperiencePoints'],
            'Trophies': accountData['Trophies'],
            'HighestTrophies': accountData['HighestTrophies'],
            'UnlockedBrawlersCount': len(accountData['UnlockedBrawlers']),
            'Unknown2': 0,
            'ProfileIconID': 28000000 + accountData['ProfileIcon'],
            'SoloVictories': 0,
            'HighestRoboRumbleLvlPassed': 0,
            'Unknown3': 0,
            'DuoVictories': 0,
            'HighestBossFightLvlPassed': 0,
            'Unknown4': 0,
            'PowerPlayRank': 0,
            'MostChallengeWins': 0,
            'HighestRampageLvlPassed': 0

        }

        return playerStats
