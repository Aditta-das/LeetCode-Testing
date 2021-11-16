def tournamentWinner(competitions, results):
	home_team = 1
	currentBest = ""
	scores = {
		currentBest: 0
	}

	for idx, competition in enumerate(competitions):
		team = results[idx]
		home, away = competition
		winner = home if team == home_team else away
		currentBestTeam(winner, 3, scores)
		if scores[winner] > scores[currentBest]:
			currentBest = winner
	return currentBest

def currentBestTeam(team, points, score):
	if team not in score:
		score[team] = 0
	score[team] += points



competitions = [
    ["HTML", "Java"],
    ["Java", "Python"],
    ["Python", "HTML"],
    ["C#", "Python"],
    ["Java", "C#"],
    ["C#", "HTML"]
]
results = [0, 1, 1, 1, 0, 1]

print(tournamentWinner(competitions, results))