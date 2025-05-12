#This goes through the code to see all the study partners and their availabilty. 
def find_matches(user, all_users):
    matches = []
    for potential_match in all_users:
        if set(user.courses).intersection(set(potential_match.courses)) and user.availability == potential_match.availability:
            matches.append(potential_match)
    return matches
#Returns a list of all the peopele that match up with one another
