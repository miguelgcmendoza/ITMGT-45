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
    if from_member in social_graph.get(to_member, {}).get('following', []):
        if to_member in social_graph.get(from_member, {}).get('following', []):
            return "friends"
        return "follower"
    elif to_member in social_graph.get(from_member, {}).get('following', []):
        return "followed by"
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
    size = len(board)

    # Check rows
    for row in board:
        if len(set(row)) == 1 and row[0] != '':
            return row[0]

    # Check columns
    for col in range(size):
        if len(set(board[row][col] for row in range(size))) == 1 and board[0][col] != '':
            return board[0][col]

    # Check diagonals
    if len(set(board[i][i] for i in range(size))) == 1 and board[0][0] != '':
        return board[0][0]
    if len(set(board[i][size - i - 1] for i in range(size))) == 1 and board[0][size - 1] != '':
        return board[0][size - 1]

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
    current_stop = first_stop
    travel_time = 0

    while current_stop != second_stop:
        next_stop = route_map.get(current_stop)
        if next_stop is None:
            return -1  # Invalid route

        travel_time += next_stop.get('travel_time_mins', 0)
        current_stop = next_stop.get('next_stop')

        if current_stop == first_stop:
            return -1  # Infinite loop detected

    return travel_time


# Sample data for Relationship Status
social_graph = {
    "@bongolpoc": {
        "first_name": "Joselito",
        "last_name": "Olpoc",
        "following": []
    },
    "@joaquin": {
        "first_name": "Joaquin",
        "last_name": "Gonzales",
        "following": ["@chums", "@jobenilagan"]
    },
    "@chums": {
        "first_name": "Matthew",
        "last_name": "Uy",
        "following": ["@bongolpoc", "@miketan", "@rudyang", "@joeilagan"]
    },
    "@jobenilagan": {
        "first_name": "Joben",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@joeilagan", "@chums", "@joaquin"]
    },
    "@joeilagan": {
        "first_name": "Joe",
        "last_name": "Ilagan",
        "following": ["@eeebeee", "@jobenilagan", "@chums"]
    },
    "@eeebeee": {
        "first_name": "Elizabeth",
        "last_name": "Ilagan",
        "following": ["@jobenilagan", "@joeilagan"]
    },
}

# Sample data for Tic Tac Toe
board1 = [
    ['X', 'X', 'O'],
    ['O', 'X', 'O'],
    ['O', '', 'X'],
]

# Sample data for ETA
route_map = {
    'a1': {'next_stop': 'a2', 'travel_time_mins': 10},
    'a2': {'next_stop': 'b1', 'travel_time_mins': 10230},
    'b1': {'next_stop': 'a1', 'travel_time_mins': 1},
}

# Test the functions with the sample data
print(relationship_status("@joaquin", "@chums", social_graph))
print(tic_tac_toe(board1))
print(eta('a1', 'a2', route_map))