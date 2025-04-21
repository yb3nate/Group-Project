def find_matches(user, all_users):
#Within this function, it shows and explors different options for study partners
#This will bring out people that are matches within the same criteria
    matches = []
    for potential_match in all_users:
        if set(user.courses).intersection(set(potential_match.courses)) and user.availability == potential_match.availability:
            matches.append(potential_match)
    return matches