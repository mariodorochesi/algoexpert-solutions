def tournamentWinner(competitions, results):
    points = {}

    for i in range(len(competitions)):
        if competitions[i][0] not in points:
            points[competitions[i][0]] = 0
        if competitions[i][1] not in points:
            points[competitions[i][1]] = 0

        if results[i] == 1:
            points[competitions[i][0]] += 3
        elif results[i] == 0:
            points[competitions[i][1]] += 3

    max_points = 0
    winner = None

    for team, score in points.items():
        if score >= max_points:
            max_points = score
            winner = team
            
    return winner
