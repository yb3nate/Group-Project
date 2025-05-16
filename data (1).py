import random

# This file contains random data and a function to generate fake profiles for testing.

# Random data for matching
names= [
    "Jamal Washington", "Aaliyah Johnson", "Li Wei", "Sakura Tanaka", "Min-Jun Kim",
    "Mei Chen", "Arjun Patel", "Priya Sharma", "Rahul Gupta", "Anika Reddy",
    "Carlos Hernandez", "Sofia Lopez", "Diego Rivera", "Omar Al-Farouq", "Layla Hassan",
    "Khalid Nasser", "Liam O’Connor", "Emma Schmidt", "Lucas Rossi", "Chloe Dubois",
    "Kwame Mensah", "Amina Okafor", "Thabo Dlamini", "Fatimah Yusuf", "Tala Redbird", "Koda Black Elk"
]
majors = [
    "Computer Science", "Information Science", "Psychology", "Biology", "Business",
    "Criminology", "Public Health", "English", "Economics", "Engineering"
]
study_habits =[
    "Night owl", "Early bird", "Group study", "Solo study", "Visual learner",
    "Auditory learner", "Flashcards", "Practice problems", "Cramming", "Consistent daily study"
]

availability= [
    "Weekends", "Weekdays", "Evenings", "Mornings", "Flexible",
    "Monday-Wednesday", "Thursday-Friday", "Only afternoons", "Late nights", "Lunch breaks"
]
courses = [
    ["INST126", "INST201", "INST311", "INST314", "INST326"],
    ["INST327", "INST335", "INST346", "INST352", "INST362"],
    ["CMSC131", "PSYC100", "BSCI170", "MATH140", "ENGL101"],
    ["GVPT170", "ECON200", "PHIL140", "ARTH200", "MUSC130"],
    ["KNES287", "JOUR175", "HLTH200", "HIST156", "GEOG202"]
]

def generate_random_profiles(count=5):
    profiles= []
    for _ in range(count):
        profile = {
            "name":random.choice(names),
            "major": random.choice(majors),
            "study_habits":random.choice(study_habits),
            "availability": random.choice(availability),
            "courses": random.choice(courses),
        }
        profiles.append(profile)
    return profiles
