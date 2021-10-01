# temperature_conversion_program
A program that converts temperature. (C -> F &amp; vice versa).

Brief Overview: 
- Program converts input to a list. Program accesses the last index of the list to determine what unit type it is ("C" or "F" ). 
- There are two loops for conversion in either direction. 
- A third loop is used to print an error message if the input is invalid (e.g. invalid format). 
- Output is returned at the end, either a converted unit or error message. 

Inputs accepted: 

- "34C" , "74F", "20c", "52f" etc. 
- *If an invalid input is encountered, the program will just return an error message. 

Outputs: 

- The output will be the opposite of the unit that is inputed (e.g. "74C" > "54F"), do note that exact formatting is required for the program to produce an ouput. Otherwise an error message will be returned. 

Installation: 

- This program does not use any libraries or external modules. Only "main.py" is needed for this program to run. Download the whole repository and run your Terminal at the program's directory (in this case, "temperature_conversion_program"). 

How to run: 

- Run this in your Terminal. Script can be ran via Terminal in the directory where the file is located with the below Terminal Command:

    "python3 main.py" 
