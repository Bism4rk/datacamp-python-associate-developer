penguin_305_details = {'species': 'Adlie', 'flipper_length': 190.0, 'body_mass': 3050.0, 'tracked': True, 'sex': 'FEMALE'}

# Check the truthiness of penguin_305_details sex key
if penguin_305_details["sex"]:
	# If true, check if sex is True and store it as sex_is_true
    sex_is_true = penguin_305_details["sex"] is True
    # Print the sex key's value and sex_is_true
    print(f"{penguin_305_details['sex']}: {sex_is_true}")

# Check the truthiness of penguin_305_details tracked key
if penguin_305_details["tracked"]:
	# If true, check if tracked is True and store it as tracked_is_true
    tracked_is_true = penguin_305_details["tracked"] is True
    # Print the tracked key and tracked_is_true
    print(f"{penguin_305_details['tracked']}: {tracked_is_true}")