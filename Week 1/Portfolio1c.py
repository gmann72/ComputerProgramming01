# Define the stats
matches_played = 609
times_batted = 1014
not_out = 162
runs_scored = 48426

# Batting average
completed_innings = times_batted - not_out
batting_average = runs_scored / completed_innings

# Display the batting average
print(f"Geoffrey Boycott's batting average is {batting_average:.2f}")
