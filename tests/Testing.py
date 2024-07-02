import re

import self

paragraph_text = """The order number is ABC123456 and the total amount is $125.00.

213112

Gotogowhere:

The customer ID is 789012. Please process the order as soon as possible."""
# print(paragraph_text)

# //android.view.View[@text="848771"]
# -android uiautomator :new UiSelector().className("android.view.View").instance(38)


# Split the paragraph into individual sentences
sentences = paragraph_text.split('.')

# Search for the 6-digit number in each sentence
for sentence in sentences:
    six_digit_number = re.search(r'\b\d{6}\b', sentence)
    if six_digit_number:
        print(f"Found 6-digit number: {six_digit_number.group()}")
        break  # Exit the loop if a 6-digit number is found
else:
    print("No 6-digit number found in the paragraph.")

    # self.driver.tap([(102, 1567)])
    # self.driver.tap([(102, 1567)])
    # time.sleep(3)
    # self.driver.tap([(409, 1476)])
    # time.sleep(5)