# debug_log.md
# Author: Evan Russo 

## Bug 1 
Error type: KeyError
File + line: week8_buggy.py, line 12 (line 13 with the DEBUG print)
What the error means: python tried to access 'amount', but Alice's record had the misspelled key 'amout'.
What I told duck: My loop adds each record's amount to the total, but Alice's record uses 'amout', so Python cannot find the key. 
What I tried: I added a DEBUG print before acccessing the key and ran the program, The output showed the typo in Alice's record. 
How I fixed it: The DEBUG showed that Alice's record had 'amout' instead of 'amount'. I changed the key to 'amount' in the records list and removed the DEBUG print. 
## Bug 2
Error type: TyperError
File + line: week8_buggy.py, line 16
What the error means: The > operator cannot compare the integer amount with the string '1000'.
How I fixed it: I used int('1000') to convert the string to an integer so it could be compared with amount.

## After Fixing Both Bugs 
Final output:  Total amount: $5150.00 across 3 records 
               True
Did pytest pass? Yes

## AI Literacy Reflection 
Did I use AI? No
Why I didnt Use it: I knew exactly what the problem was as I was typing the buggy code and noticed those 2 bugs right away and knew exactly how to fix them. 
Can I explain every fixed line? Yes

## What I Learned 
I learned how to use the traceback and a DEBUG print to find misspelled dictionary key. I also leanred that python cannot compare an integer to a string yusing >, so I used int() to convert the string into an integer. These bugs showed me why checking spelling and data types matters when debugging. 