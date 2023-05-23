'''Module 4: Individual Programming Assignment 1

Parsing Data

This assignment covers your ability to manipulate data in Python.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    15 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data    

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    from_member_following = social_graph[from_member]["following"]
    to_member_following = social_graph[to_member]["following"]

    if from_member in to_member_following and to_member in from_member_following:
        return "friends"
    elif from_member in to_member_following:
        return "followed by"
    elif to_member in from_member_following:
        return "following"
    else:
        return "no relationship"


def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
# Check rows
    for row in board:
        if all(x == "X" for x in row):
            return "X"
        elif all(x == "O" for x in row):
            return "O"

# Check columns
    for col in range(len(board[0])):
        if all(board[row][col] == "X" for row in range(len(board))):
            return "X"
        elif all(board[row][col] == "O" for row in range(len(board))):
            return "O"
        
# Check diagonals
    if all(board[i][i] == "X" for i in range(len(board))):
        return "X"
    elif all(board[i][i] == "O" for i in range(len(board))):
        return "O"
    elif all(board[i][len(board)-i-1] == "X" for i in range(len(board))):
        return "X"
    elif all(board[i][len(board)-i-1] == "O" for i in range(len(board))):
        return "O"

    return "NO WINNER"


def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circular route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
# Transform route_map into an adjacency matrix
    route_matrix = {}

    for leg, info in route_map.items():
        start, end = leg
        travel_time = info["travel_time_mins"]
        if start not in route_matrix:
            route_matrix[start] = {}
        route_matrix[start][end] = travel_time

 # Perform a BFS to find the shortest path
    queue = [(first_stop, 0)]
    visited = set()

    while queue:
        stop, time = queue.pop(0)
        visited.add(stop)
        if stop == second_stop:
            return time
        for neighbor, travel_time in route_matrix[stop].items():
            if neighbor not in visited:
                queue.append((neighbor, time + travel_time))

    return -1
