# List of professors' names
professors = ["Dr. Sharma", "Prof. Kumar", "Dr. Patel", "Mr. Rao"]

# Step 1: Filter names with 'Dr'
phd_professors = list(filter(lambda name: True if "Dr. " in name else False, professors))

# Step 2: Append '(PhD)' to filtered names
professors_with_phd = [f"{name} (PhD)" for name in phd_professors]

# Output the result
print(professors_with_phd)
