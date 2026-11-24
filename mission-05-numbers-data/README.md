# Mission 5 - Numbers and data

## 1. Task / objective
In this mission, I had to convert numbers between decimal, binary and hexadecimal. I also had to check the answers using Python and create a small converter program.

## 2. Work completed

### Task 5.1 - Manual conversions

| Question | Working | Answer |
|---|---|---|
| Decimal 13 to binary | 8 + 4 + 1 | `1101` |
| Decimal 25 to binary | 16 + 8 + 1 | `11001` |
| Binary 1010 to decimal | 8 + 0 + 2 + 0 | `10` |
| Binary 1101 to decimal | 8 + 4 + 0 + 1 | `13` |
| Hexadecimal A to decimal | A = 10 | `10` |
| Hexadecimal 1F to decimal | 1 x 16 + 15 | `31` |
| Binary 1111 to hexadecimal | 1111 is decimal 15 | `F` |

### Task 5.2 - Checking with Python

I can check the conversions using these Python expressions:

```python
bin(13)
bin(25)
int("1010", 2)
int("1101", 2)
hex(10)
int("1F", 16)
hex(int("1111", 2))
```

**My test results:** [Run these in Python and confirm the results.]

### Task 5.3 - Number converter

I created `number_converter.py`. It asks for a decimal number and shows the binary and hexadecimal forms.

Example test cases:

| Input | Binary | Hexadecimal |
|---|---|---|
| 13 | `0b1101` | `0xd` |
| 25 | `0b11001` | `0x19` |
| 31 | `0b11111` | `0x1f` |

Run the program using:

```bash
python3 mission-05-numbers-data/number_converter.py
```

The `bin()` function converts an integer to binary. The `hex()` function converts it to hexadecimal. The `int()` function converts the input text into a whole number.

### Task 5.4 - How text is stored

- Uppercase `A` has ASCII decimal value 65.
- Lowercase `a` has ASCII decimal value 97.
- Computers need character encoding so that text can be stored as numbers and understood correctly.
- An example of a character outside basic ASCII is `😊`.

## 3. Commands / tools used
- `python3` - opens Python.
- `input()` - takes input from the user.
- `int()` - converts text into an integer.
- `bin()` - converts a number to binary.
- `hex()` - converts a number to hexadecimal.
- `print()` - displays the result.

## 4. My understanding
Binary uses only 0 and 1. Decimal uses numbers from 0 to 9. Hexadecimal uses 0 to 9 and A to F. I found that Python already has functions for these conversions, which makes checking the answers easier.

## 5. Difficulties faced
[Write what you found confusing while doing the conversions or program, or write "No major difficulties".]

## 6. How I resolved them
[Explain how you fixed it, or write "Not applicable".]

## 7. Evidence / files
- `number_converter.py`
- Conversion table in this README
- [Add your three actual test outputs.]

## 8. Commit details
Commit message: `Build number converter and practise data representation`

Commit and push status: [Update after doing it.]
