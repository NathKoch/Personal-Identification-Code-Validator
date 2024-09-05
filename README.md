## Personal Identification Code Validator
This Python script is designed to verify the correctness of Estonian personal identification code (isikukood). The script performs several checks to ensure that the code is valid in format and content.

### Features

- Checks if the code exists and is not empty
- Verifies the pattern of the code (11 digits)
- Checks the gender, birth year, month, and day of the code
- Calculates and verifies the control number of the code
- If the code is entered incorrectly, the script will write about where the error is.

### How to use

- To use the script, simply run it and input the identification code you wish to verify:
```bash
python IkAndmekvaliteediScript.py
```
- The script will validate the code and print the result (either "Isikukood sisestatud õigesti" or "Isikukood sisestatud valesti")

- Type "exit" to close the program.

### Script Output

```bash

Programmi sulgemiseks sisestage "exit"

Sisestage isikukood:
gdsfgs
Sisestatud väärtus ei ole täisarv

Programmi sulgemiseks sisestage "exit"

Sisestage isikukood:
12345678909
Neljas ja viies number - sünnikuu number sisestatud valesti
Kuues ja seitsmes number - sünnikuupäev sisestatud valesti
Üheteistkümnes number – kontrollnumber sisestatud valesti
Isikukood sisestatud valesti

Programmi sulgemiseks sisestage "exit"

Sisestage isikukood:
50008120278
Üheteistkümnes number – kontrollnumber sisestatud valesti
Isikukood sisestatud valesti

Programmi sulgemiseks sisestage "exit"

Sisestage isikukood:
37605030299
Isikukood sisestatud õigesti

Programmi sulgemiseks sisestage "exit"

Sisestage isikukood:
exit
```

### Note
The script does not store or process any personal data.
