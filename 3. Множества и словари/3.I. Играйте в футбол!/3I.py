# 3 I. Играйте в футбол! https://contest.yandex.ru/contest/59541/problems/I/

def main():

    from sys import stdin
    import re

    class Player:
        def __init__(self, name, club):
            self.name = name
            self.club = club
            self.goals = 0
            self.goals_per_min = [0 for i in range(91)]
            self.score_open = 0

    class Club:
        def __init__(self, name):
            self.name = name
            self.plays = 0
            self.goals = 0
            self.score_open = 0

    players, clubs = {}, {}
    data = stdin.readlines()
    # хэндлим строки данных

    i = 0
    while i < len(data):
        line = data[i]
        if line.startswith('"'):
            club1, club2 = re.findall(r'(".+").*(".+")', line)[0]
            points1, points2 = map(int, re.findall(r'(\d+):(\d+)', line)[0])
            clubs.setdefault(club1, Club(club1))
            clubs.setdefault(club2, Club(club2))
            clubs[club1].plays += 1
            clubs[club2].plays += 1
            clubs[club1].goals += points1
            clubs[club2].goals += points2

            open_minute, open_player, open_club = 100, None, None

            for k in range(points1):
                i += 1
                player = ' '.join(data[i].split()[0:-1])
                minute = int(data[i].split()[-1][:-1])
                players.setdefault(player, Player(player, club1))
                if not k and minute < open_minute:
                    open_minute, open_player, open_club = minute, player, club1
                players[player].goals += 1
                players[player].goals_per_min[minute] += 1

            for k in range(points2):
                i += 1
                player = ' '.join(data[i].split()[0:-1])
                minute = int(data[i].split()[-1][:-1])
                players.setdefault(player, Player(player, club2))
                if not k and minute < open_minute:
                    open_minute, open_player, open_club = minute, player, club2
                players[player].goals += 1
                players[player].goals_per_min[minute] += 1

            if open_player != None:
                players[open_player].score_open += 1
                clubs[open_club].score_open += 1

            i += 1

        elif line.startswith('Total goals for'):
            club = re.search(r'(?<=Total goals for ).*', line)[0]
            try: print(clubs[club].goals)
            except: print(0)
            i += 1

        elif line.startswith('Mean goals per game for'):
            club = re.search(r'(?<=Mean goals per game for ).*', line)[0]
            try: print(clubs[club].goals / clubs[club].plays)
            except: print(0)
            i += 1

        elif line.startswith('Total goals by'):
            player = re.search(r'(?<=Total goals by ).*', line)[0]
            try: print(players[player].goals)
            except: print(0)
            i += 1

        elif line.startswith('Mean goals per game by'):
            player = re.search(r'(?<=Mean goals per game by ).*', line)[0]
            try: print(players[player].goals / clubs[players[player].club].plays)
            except: print(0)
            i += 1

        elif line.startswith('Goals on minute'):
            player = re.search(r'(?<=by ).*', line)[0]
            minute = int(re.search(r'\b\d+\b', line)[0])
            try: print(players[player].goals_per_min[minute])
            except: print(0)
            i += 1

        elif line.startswith('Goals on first'):
            player = re.search(r'(?<=by ).*', line)[0]
            minute = int(re.search(r'\b\d+\b', line)[0])
            try: print(sum(players[player].goals_per_min[:minute+1]))
            except: print(0)
            i += 1

        elif line.startswith('Goals on last'):
            player = re.search(r'(?<=by ).*', line)[0]
            minute = int(re.search(r'\b\d+\b', line)[0])
            try: print(sum(players[player].goals_per_min[91-minute:]))
            except: print(0)
            i += 1

        elif line.startswith('Score opens by'):
            obj = re.search(r'(?<=Score opens by ).*', line)[0]
            try:
                print(clubs[obj].score_open)
            except:
                try:
                    print(players[obj].score_open)
                except:
                    print(0)
            i += 1

if __name__ == '__main__':
    main()  