# StudyBuddy - UMD College Park - !Go Terps! - 

Hey there! Welcome to **StudyBuddy**, a Python app we built because, honestly, as students we really felt the need for something that makes finding the right study partner way easier. Sometimes studying solo just isn’t as fun or and can be harder at times, and finding someone with the same classes, habits, and free time isn’t always easy. So we created StudyBuddy to take the stress out of it and help you connect with compatible study buddies in a quick and fun way.

---

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [How to Run It](#how-to-run-it)
4. [Testing](#testing)
5. [Written Testing Procedures](#written-testing-procedures)
6. [File Structure](#file-structure)

---

## Overview

StudyBuddy is a command-line Python application where you can:
- Create your own student profile.
- Check out other students’ profiles.
- Find study partners that match your classes, study habits, and schedule.

The app is organized into multiple files to keep things clean and maintainable.

---

## Features

- **User Profiles** — Create and update profiles with your name, major, courses, study habits, and availability.
- **Matching Logic** — Automatically find study partners who share your attributes.
- **Random Profile Generation** — Generate fake profiles to test or demo the app.
- **Unit Testing** — Automated tests help make sure everything runs smoothly.

---

## How to Run It

Getting started is easy! Here’s what you need to do:

1. **Clone this repo to your computer**

   Open your terminal or command prompt and type:
https://github.com/yb3nate/Group-Project.git 

**Go into the project folder**

3. **Run the app**

Make sure Python 3.6 or later is installed on your computer. Then, type into the Terminal:

python app.py


This will launch the StudyBuddy program in your terminal, where you can follow the menu options to create a profile, view others, and find study partners.

## Written Testing Procedures

### 1. `view_profile`

- **What it does:** Shows the details of a user profile.
- **How to test:**
1. Run the program and create a profile with:
  - Name: Alice
  - Major: Computer Science
  - Courses: CS101, Math101
  - Study Habits: Night owl
  - Availability: Weekends
2. Use the `view_profile` option to display Alice’s profile.
3. Make sure the info shows up correctly and clearly.

### 2. `update_profile`

- **What it does:** Lets you interactively change profile details.
- **How to test:**
1. Create a profile with the same info as above.
2. Choose the `update_profile` option.
3. Follow prompts to:
  - Change name to "Bob"
  - Add course "Math101"
  - Change availability to "Evenings"
4. View the profile again to check if changes stuck.

### 3. Main Menu (`app.py`)

- **What it does:** The menu lets you navigate the app.
- **How to test:**
1. Run the program.
2. Test every menu option (create profile, view profiles, find matches, etc.)
3. Try entering invalid options (like “6” or a letter) and confirm you get a helpful error message.
4. Make sure exiting works smoothly.

---

## File Structure

Here’s a quick look at the important files in this project:
api.py
app.py
config.py
data.py
database.py
main.py
matching_logic.py
studdy_buddy.py
test_data.py
test_user.py
test_user_profile.py
testing_matching.py
user.py
user_profile.py
