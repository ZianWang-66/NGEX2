participants = [
    "Alice Wong",
    "Chen Wei",
    "David Kim",
    "Fatima Ali",
    "George Smith",
    "Hana Lee",
    "Audrey Hepburn",
    "James Stewart",
    "George Scott"
]

scores = [78, 92, 64, 87, 55, 73, 69, 96, 90]

qualification_score = 70
distinction_score = 90


# Make sure the lists have the same number of elements



# First, display all the current participants with their scores. Use zip()
zipped_data = zip(participants, scores)
participants_with_scores = list(zipped_data)
print(participants_with_scores)



# Write the logic to accept a new participant's name and their score. 
# While entering, also check if they are already in the list of participants. 
# If the participant is already registered, display a message and do not add them to the list.
# If the name is empty, then print an error saying that the name cannot be empty, and don't add them to the list.
# If the score is not a number, then print an error saying that the score must be a number, and don't add them to the list.
# If the score is less than 0 or greater than 100, then print an error saying that the score must be between 0 and 100, and don't add them to the list.
# Otherwise, add the participant and their score to the lists and display a message saying that they have been successfully registered.


new_name = input("Enter the new participant's name: ")
if new_name in participants:
    print(f"{new_name} is already registered.")
elif new_name.strip() == "":
    print("Error: Name cannot be empty.")
else:
    try:
        new_score = int(input("Enter the new participant's score: "))
        if new_score < 0 or new_score > 100:
            print("Error: Score must be between 0 and 100.")
        else:
            participants.append(new_name)
            scores.append(new_score)
            print(f"{new_name} has been successfully registered with a score of {new_score}.")
    except ValueError:
        print("Error: Score must be a number.")






# Write the logic to search for a specific participant.
# If the participant is found, display their name, score, and whether they are qualified or not.
# If the score is more than the distinction score, display that they have a DISTINCTION.
# If the score is more than the qualification score, display that they are QUALIFIED.
# Otherwise, display that they are NOT QUALIFIED.
# If the participant is not found, display a message saying that they are not found.

search_option = input("Do you want to search for a participant? (yes/no): ").strip().lower()
if search_option == "yes":
    search_name = input("Enter the participant's name to search: ")
    if search_name in participants:
        index = participants.index(search_name)
        score = scores[index]
        if score >= distinction_score:
            qualification_status = "DISTINCTION"
        elif score >= qualification_score:
            qualification_status = "QUALIFIED"
        else:
            qualification_status = "NOT QUALIFIED"
        print(f"Participant: {search_name}, Score: {score}, Status: {qualification_status}")
    else:
        print(f"{search_name} is not found in the list of participants.")


# Display every participant's name, score, and whether they are qualified or not. 


for name, score in zip(participants, scores):
    if score >= distinction_score:
        status = "DISTINCTION"
    elif score >= qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    print(f"Name: {name} | Score: {score} | Status: {status}")
print()





# Write the logic to find if there's even one participant that has a distinction, and if all the participants have passed (i.e., scored 50 or more).

has_distinction = any(score >= distinction_score for score in scores)
all_passed = all(score >= 50 for score in scores)

if has_distinction:
    print("There is at least one participant with a DISTINCTION.")
else:
    print("There are no participants with a DISTINCTION.")

if all_passed:
    print("All participants have passed.")
else:
    print("Not all participants have passed.")








# Write the logic to update a participant's score.
# Ensure that the participant exists in the list before updating their score. 
# Also ensure that the new score is a valid number between 0 and 100.

update_option = input("Do you want to update a participant's score? (yes/no): ").strip().lower()
if update_option == "yes":
    update_name = input("Enter the participant's name to update: ").strip()
    if update_name not in participants:
        print(f"{update_name} is not found in the list.")
    else:
        try:
            new_score_val = int(input(f"Enter the new score for {update_name}: "))
            if new_score_val < 0 or new_score_val > 100:
                print("Error: Score must be between 0 and 100.")
            else:
                index = participants.index(update_name)
                scores[index] = new_score_val
                print(f"Success: {update_name}'s score has been updated to {new_score_val}.")
        except ValueError:
            print("Error: Score must be a valid number.")


# Write the logic to withdraw (remove) a participant from the list.
# Ensure that the score for that specific participant is also removed from the scores list

withdraw_option = input("Do you want to withdraw a participant? (yes/no): ").strip().lower()
if withdraw_option == "yes":
    remove_name = input("Enter the participant's name to withdraw: ").strip()
    if remove_name not in participants:
        print(f"{remove_name} is not found in the list.")
    else:
        remove_index = participants.index(remove_name)
        participants.pop(remove_index)
        scores.pop(remove_index)
        print(f"{remove_name} has been withdrawn from the list.")



# Create and display a scoreboard where all the participants and their scores are displayed in descending order.
# Display their rank alongside the participant name and score

ranking_list = sorted(zip(participants, scores), key=lambda x: x[1], reverse=True)

current_rank = 1
for i, (name, score) in enumerate(ranking_list):
    if i >0 and score != ranking_list[i-1][1]:
        current_rank = i + 1
    print(f"Rank: {current_rank} | Name: {name} | Score: {score}")
    




# Calculate statistics: 
# Calculate what the highest score is, what lowest score is, what the average score is.
# Calculate how many participants have the highest score and the lowest score
# Calculate how many participants have distinctions, how many are qualified, and how many are not qualified

highest_score = max(scores)
lowest_score = min(scores)
average_score = sum(scores) / len(scores)

count_highest = scores.count(highest_score)
count_lowest = scores.count(lowest_score)

count_distinction = 0
count_qualified = 0
count_not_qualified = 0

for score in scores:
    if score >= distinction_score:
        count_distinction += 1
    elif score >= qualification_score:
        count_qualified += 1
    else:
        count_not_qualified += 1


# Generate a final report that displays the participant name, their rank, their score, and their qualification (DISTINCTION, QUALIFIED, NOT QUALIFIED)
# Also the display all the statistics you calculated above

current_rank = 1
for i, (name, score) in enumerate(ranking_list):
    if i > 0 and score != ranking_list[i-1][1]:
        current_rank = i + 1
    
    if score >= distinction_score:
        status = "DISTINCTION"
    elif score >= qualification_score:
        status = "QUALIFIED"
    else:
        status = "NOT QUALIFIED"
    
    print(f"{current_rank} {name} {score} {status}")

print(f"Total participants: {len(participants)}")
print(f"Highest score: {highest_score} (achieved by {count_highest} participant(s))")
print(f"Lowest score: {lowest_score} (achieved by {count_lowest} participant(s))")
print(f"Average score: {average_score:.2f}")
print()
print(f"Number of DISTINCTIONs (≥{distinction_score}): {count_distinction}")
print(f"Number of QUALIFIED (≥{qualification_score}): {count_qualified}")
print(f"Number of NOT QUALIFIED (<{qualification_score}): {count_not_qualified}")