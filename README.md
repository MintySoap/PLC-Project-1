# PLC-Project-1
Instructions taken from: https://tinman.cs.gsu.edu/~raj/4330/sp22/project1/

Using Python PLY implement the RE to DFA conversion algorithm. 
Once the DFA is constructed, prompt the user for input strings and report "MATCH" if the string is accepted by the DFA and "NO MATCH" otherwise. 
Please refer to the notes on the algorithm at RegExp2DFA.pdf".

Here is a sample run:

Mac-mini:re raj$ python3 RE.py

REGEX: (a+b)*aa(a+b)*;

  INPUT STRING: aa;
  
  MATCH
  
  INPUT STRING: ababab;
  
  NO MATCH
  
  INPUT STRING: abaabbbb;
  
  MATCH
  
  INPUT STRING: bbbaabbbbbbb;
  
  MATCH
  
  INPUT STRING: exit;
  
REGEX: a(a+b)*b + b(a+b)*a;

  INPUT STRING: abba;
  
  NO MATCH
  
  INPUT STRING: abbb;
  
  MATCH
  
  INPUT STRING: baba;
  
  MATCH
  
  INPUT STRING: babb;
  
  NO MATCH
  
  INPUT STRING: aaaaaaaaabbbbbbbb;
  
  MATCH
  
  INPUT STRING: bbbbbbbaaaaaa;
  
  MATCH
  
  INPUT STRING: ab;
  
  MATCH
  
  INPUT STRING: ba;
  
  MATCH
  
  INPUT STRING: aa;
  
  NO MATCH
  
  INPUT STRING: bb;
  
  NO MATCH
  
  INPUT STRING: exit;
  
REGEX: exit;

Mac-mini:re raj$ python3 RE.py -dfa

REGEX: (a+b)*aa(a+b)*;

start_state({1, 2, 3}).

delta({1, 2, 3},a,{1, 2, 3, 4}).

delta({1, 2, 3},b,{1, 2, 3}).

delta({1, 2, 3, 4},a,{1, 2, 3, 4, 5, 6, 7}).

delta({1, 2, 3, 4},b,{1, 2, 3}).

delta({1, 2, 3, 4, 5, 6, 7},a,{1, 2, 3, 4, 5, 6, 7}).

delta({1, 2, 3, 4, 5, 6, 7},b,{1, 2, 3, 5, 6, 7}).

delta({1, 2, 3, 5, 6, 7},a,{1, 2, 3, 4, 5, 6, 7}).

delta({1, 2, 3, 5, 6, 7},b,{1, 2, 3, 5, 6, 7}).

delta(set(),a,set()).

delta(set(),b,set()).

final_state({1, 2, 3, 4, 5, 6, 7}).

final_state({1, 2, 3, 5, 6, 7}).

  INPUT STRING: abab;
  
  NO MATCH
  
  INPUT STRING: abaabb;
  
  MATCH
  
  INPUT STRING: exit;
  
REGEX: exit;

Mac-mini:re raj$ python3 RE.py

REGEX: (1+2+3+4+5+6+7+8+9)(0+1+2+3+4+5+6+7+8+9)*;

  INPUT STRING: 976;
  
  MATCH
  
  INPUT STRING: 0976;
  
  NO MATCH
  
  INPUT STRING: 123450;
  
  MATCH
  
  INPUT STRING: ab12;
  
  NO MATCH: Invalid input character
  
  INPUT STRING: exit;
  
REGEX: exit;
