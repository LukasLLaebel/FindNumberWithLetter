from num2words import num2words

def find_letters_numbers(limit=1000):
    numbers_with_letter = []  # List to store numbers that contain the specified letter
    
    # Prompt the user to input the letter they are searching for
    number_letter = input("What letter are you looking for: ").lower()

    # Iterate through numbers from 0 to the given limit
    for num in range(limit + 1):
        # Convert the number to its word representation and convert it to lowercase
        num_name = num2words(num).lower()
        
        # Check if the user-specified letter is present in the word representation
        if number_letter in num_name:
            numbers_with_letter.append((num, num_name))  # Store the number and its word form

    return numbers_with_letter  # Return the list of matching numbers

if __name__ == "__main__":
    # Ask the user for the upper limit of numbers to check
    limit = int(input("Where do you want to count to: "))
    
    # Call the function to find numbers containing the specified letter
    result = find_letters_numbers(limit)
    
    # Print out the matching numbers and their word representations
    for num, name in result:
        print(f"{num}: {name}")
