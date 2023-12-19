## Functions

### Simple Functions

#### `add(x, y)`

This function adds two numbers and returns the result.

#### `subtract(x, y)`

This function subtracts the second number from the first and returns the result.

### Complex Functions

#### `sum_of_digits(n)`

Given a number `n`, this function calculates and returns the sum of its digits.

#### `is_palindrome(n)`

This function checks if the given number `n` is a palindrome and returns `True` if it is, otherwise `False`.

#### `myzip(it1, it2)`

This function implements the `zip` function for two collections `it1` and `it2`. It takes two iterable objects (`it1` and `it2`) and returns a list of tuples, where each tuple contains the corresponding elements from the input iterables.

## Important Note

To ensure proper functionality, it is mandatory to call at least one function from the `simp` module before attempting to use any functions from the `comp` module.

## Usage

To use the package, follow these steps:

- Clone the repository:

   git clone https://github.com/Reouhaddad/lab1.git

- Navigate to the project directory:
    cd lab1
    
- Create a virtual environment:
 py -m venv env

- Activate the virtual environment:

    On Windows:
    .\env\Scripts\activate
    On macOS/Linux:
    source env/bin/activate

- Install the required dependencies:
 pip install -r requirements.txt

- Run the test script:
 py test_script.py
