# Basic Calculator Program

A simple Python script that performs arithmetic operations on two numbers.

## Features
- Takes two numbers as input
- Performs five basic arithmetic operations:
  - Addition (+)
  - Subtraction (-)
  - Multiplication (×)
  - Division (÷)
  - Squaring (x²)
- Prints formatted results with emoji indicators

## Usage
1. Run the script:
   ```bash
   python calculator.py
   ```
2. Enter two numbers when prompted
3. View the calculated results

## Operations Performed
1. Sum (num1 + num2) ➕
2. Difference (num1 - num2) ➖
3. Product (num1 × num2) ✖️
4. Quotient (num1 ÷ num2) ➗
5. Square (num1² or num2²) 

## Example
```
Enter the first number: 5
Enter the second number: 3
Results of your two numbers:
Sum: 8.0 ✅
Difference: 2.0 ✅
Product: 15.0 ✅
Quotient: 1.6666666666666667 ✅
Square: 25.0 ✅
```

## Note
- The square operation currently shows num1² only (due to `or` operator behavior)
- Division by zero will raise an error
```

### Suggested Improvements:
1. The square operation is currently ambiguous - it only returns num1² because of how `or` works
2. Consider adding error handling for division by zero
3. You might want to clarify whether you want both squares or just one
