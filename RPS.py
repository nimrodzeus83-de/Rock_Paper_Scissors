import random

opponent_history = []
my_history = []
abbey_plays = {
    "RR": 0, "RP": 0, "RS": 0,
    "PR": 0, "PP": 0, "PS": 0,
    "SR": 0, "SP": 0, "SS": 0,
}


def player(prev_play):
    global opponent_history, my_history, abbey_plays
    response = {'R': 'P', 'P': 'S', 'S': 'R'}

    if prev_play == "":
        opponent_history = []
        my_history = []
        abbey_plays = {
            "RR": 0, "RP": 0, "RS": 0,
            "PR": 0, "PP": 0, "PS": 0,
            "SR": 0, "SP": 0, "SS": 0,
        }
        first_movement = random.choice(["R", "P", "S"])
        my_history.append(first_movement)
        return first_movement

    opponent_history.append(prev_play)

    if len(my_history) >= 2:
        last_two = my_history[-2] + my_history[-1]
        if last_two in abbey_plays:
            abbey_plays[last_two] += 1


    quincy_order = ["R", "R", "P", "P", "S"]
    if len(opponent_history) >= 5:
        is_quincy = all(
            opponent_history[-i] == quincy_order[(-i + len(opponent_history)) % 5]
            for i in range(1, 6)
        )
        if is_quincy:
            next_quincy_movement = quincy_order[len(opponent_history) % 5]
            guess = response[next_quincy_movement]
            my_history.append(guess)
            return guess

    if len(opponent_history) >= 5:
        is_kris = all(
            opponent_history[-i] == response[my_history[-i - 1]]
            for i in range(1, 5)
        )
        if is_kris:
            kris_next_move = response[my_history[-1]]
            guess = response[kris_next_move]
            my_history.append(guess)
            return guess

    if len(my_history) >= 10:
        last_ten = my_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        predicted_mrugesh_move = response[most_frequent]

        if opponent_history[-1] == predicted_mrugesh_move:
            next_window = my_history[-9:]
            next_most_frequent = max(set(next_window), key=next_window.count)
            mrugesh_next_move = response[next_most_frequent]
            guess = response[mrugesh_next_move]
            my_history.append(guess)
            return guess

    last_move = my_history[-1]
    potential_plays = [last_move + "R", last_move + "P", last_move + "S"]
    sub_order = {k: abbey_plays[k] for k in potential_plays if k in abbey_plays}
    max_val = max(sub_order.values())
    top_choices = [k for k, v in sub_order.items() if v == max_val]
    predicted_our_move = random.choice(top_choices)[-1:]
    abbey_predicted_move = response[predicted_our_move]
    guess = response[abbey_predicted_move]
    my_history.append(guess)
    return guess