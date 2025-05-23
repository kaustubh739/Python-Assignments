# Voting Eligibility Checker Accept age from the user and check whether the person is eligible for the vote (Age should be 18 or above)

print("Enter the age of the voter")
No = int(input())

if No >= 18:
    print("eligible to vote")
else:
    print("Not eligible for the vote")