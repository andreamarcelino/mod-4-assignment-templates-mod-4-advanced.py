'''Module 4: Individual Programming Assignment 1
Andrea Nicole Marcelino

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

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

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
    from_following = social_graph.get(from_member, {}).get('following', [])
    to_following = social_graph.get(to_member, {}).get('following', [])
    
    if to_member in from_following and from_member in to_following:
        return "friends"
    elif to_member in from_following:
        return "follower"
    elif from_member in to_following:
        return "followed by"
    else:
        return "no relationship"

'Sample Data'
social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":["@chums","@jobenilagan"]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":["@bongolpoc","@miketan","@rudyang","@joeilagan"]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":["@eeebeee","@joeilagan","@chums","@joaquin"]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":["@eeebeee","@jobenilagan","@chums"]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":["@jobenilagan","@joeilagan"]
    },
}

print(relationship_status("@bongolpoc", "@joaquin", social_graph)) # Output is no relationship
print(relationship_status("@joaquin", "@chums", social_graph)) # Output is follower
print(relationship_status("@chums", "@jobenilagan", social_graph)) # Output is followed by
print(relationship_status("@jobenilagan", "@joeilagan", social_graph)) # Output is friends
print(relationship_status("@joeilagan", "@eeebeee", social_graph)) # Output is friends
print(relationship_status("@eeebeee", "@bongolpoc", social_graph)) # Output is no relationship

def tic_tac_toe(board):
    '''Tic Tac Toe. 
    15 points.

    Tic Tac Toe is a common paper-and-pencil game. 
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Check rows for a win
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "":
            return row[0]

    # Check columns for a win
    for i in range(len(board)):
        col = [row[i] for row in board]
        if col.count(col[0]) == len(col) and col[0] != "":
            return col[0]

    # Check diagonals for a win
    diagonal1 = [board[i][i] for i in range(len(board))]
    if diagonal1.count(diagonal1[0]) == len(diagonal1) and diagonal1[0] != "":
        return diagonal1[0]
    diagonal2 = [board[i][len(board)-1-i] for i in range(len(board))]
    if diagonal2.count(diagonal2[0]) == len(diagonal2) and diagonal2[0] != "":
        return diagonal2[0]

    return "NO WINNER"

'Sample Data'
board1 = [    
    ['X','X','O'],
    ['O','X','O'],
    ['O','','X'],
]

result1 = tic_tac_toe(board1)
print(result1) # Output is X

board2 = [    
    ['X','X','O'],
    ['O','X','O'],
    ['','O','X'],
]

result2 = tic_tac_toe(board2)
print(result2) # Output is X

board3 = [    
    ['O','X','O'],
    ['','O','X'],
    ['X','X','O'],
]

result3 = tic_tac_toe(board3)
print(result3) # Output is O

board4 = [    
    ['X','X','X'],
    ['O','X','O'],
    ['O','','O'],
]

result4 = tic_tac_toe(board4)
print(result4) # Output is X

board5 = [    
    ['X','X','O'],
    ['O','X','O'],
    ['X','','O'],
]

result5 = tic_tac_toe(board5)
print(result5) # Output is O

board6 = [    
    ['X','X','O'],
    ['O','X','O'],
    ['X','',''],
]

result6 = tic_tac_toe(board6)
print(result6) # Output is NO WINNER

board7 = [    
    ['X','X','O',''],
    ['O','X','O','O'],
    ['X','','','O'],
    ['O','X','','']
]

result7 = tic_tac_toe(board7)
print(result7) # Output is NO WINNER

def eta(first_stop, second_stop, route_map):
    '''ETA. 
    20 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see the sample data file in this same folder for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

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
    total_time = 0
    for leg, travel_details in route_map.items():
        if (current_stop in leg) and (second_stop in leg):
            total_time += travel_details["travel_time_mins"]
            break
        elif current_stop in leg:
            total_time += travel_details["travel_time_mins"]
            current_stop = leg[1] if leg[0] == current_stop else leg[0]
    return total_time
    





