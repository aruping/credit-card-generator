# Credit Card Generator and Recorder

This Python program is an application that generates random credit card numbers and saves them to a specified file. Additionally, the generated card numbers are validated using the Luhn algorithm, and valid card numbers are recorded in the file.

## Techniques Used

### 1. Credit Card Number Generation

Steps for generating a credit card number:

- A predefined prefix ("494577") is used.
- 10 random digits are selected.
- The expiration date is randomly determined (month and year).
- A security code (CVV) is randomly generated.

### 2. Luhn Algorithm Check

The generated credit card numbers are validated using the Luhn algorithm. This algorithm is used to verify the validity of the card number. The check involves the following steps:

- The digits of the card number are reversed.
- Digits in even positions are doubled.
- Subtract 9 from doubled digits greater than 9.
- Sum all digits.
- The remainder of the sum divided by 10 gives the check digit.
- The check digit is compared with the last digit of the card number.

### 3. Writing to File and Validation

- Before writing the generated card number to the file, the existence of the file is checked.
- If the file exists, each generated card number is compared with previous card numbers to ensure uniqueness.

## Usage

The program runs in an infinite loop until it is closed by the user with Ctrl+C. When closed, the last generated card numbers are saved to the file.
