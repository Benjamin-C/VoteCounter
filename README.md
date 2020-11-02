# Vote Counter v1.0 by Benjamin Crall<br/>
Simple script to count ranked votes
### Usage:
`python votecounter.py count <source> [dest]`<br/>
`python votecounter.py gen <count> <dest>`<br/>
`python votecounter.py <count|gen|help>`
### Function:
This script counts ranked votes by eliminating the lease favorite candidate. Each round, each voters' first choices are counted, and the candidate with the least votes is eliminated from the pool. Any vote for them is removed from the vote pool, sliding subsequent votes up. This is repeated until there are no candidates left, and the reults are then printed and optionally saved to a file.
### File Format:
The script expects and saves votes in a comma seperated value (.csv) file format, where each line represents one voter, with their ordered list of candidates in orderof 1st,2nd,3rd... choices. Candidates are seperated by commas only, not spaces. The list of candidates is generated automatically by gathering any name that was voted for. The output of the counter is in a human-readable text format listing the places one per line with any candidates in that place including ties on that line
### Author
This script was written by Benjamin Crall with the help of the kind people of the internet. Contact me at bencrall@gmail.com
