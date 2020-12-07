"""
--- Day 6: Custom Customs ---
As your flight approaches the regional airport where you'll 
switch to a much larger plane, customs declaration forms are distributed 
to the passengers.

The form asks a series of 26 yes-or-no questions marked a through z. 
All you need to do is identify the questions for which anyone in your 
group answers "yes". Since your group is just you, this doesn't take very long.

However, the person sitting next to you seems to be experiencing a 
language barrier and asks if you can help. For each of the people in 
their group, you write down the questions for which they answer "yes", 
one per line. For example:

abcx
abcy
abcz
In this group, there are 6 questions to which anyone answered 
"yes": a, b, c, x, y, and z. 
(Duplicate answers to the same question don't count extra; 
each question counts at most once.)

Another group asks for your help, then another, and eventually 
you've collected answers from every group on the plane (your puzzle input). 
Each group's answers are separated by a blank line, 
and within each group, each person's answers are on a single line. For example:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

The first group contains one person who answered "yes" to 3 questions: 
a, b, and c.
The second group contains three people; combined, they answered "yes" to 3 questions: 
a, b, and c.
The third group contains two people; combined, they answered "yes" to 3 questions: 
a, b, and c.
The fourth group contains four people; combined, they answered "yes" to only 1 question, a.
The last group contains one person who answered "yes" to only 1 question, b.
In this example, the sum of these counts is 3 + 3 + 3 + 1 + 1 = 11.

For each group, count the number of questions to which anyone answered "yes". 
What is the sum of those counts?
"""


with open("input.txt", 'r') as f:
    inp = f.readlines()
# transofr the input by stripping off the "\n" carriage, 
# replacing empty line with a special set of symbol to later use them 
# as separators
inp = [answer.strip() if len(answer) > 1 else '::' for answer in inp]

# use set() method to return unique answered questions and len() to 
# measure the size of the set.
unique_questions = [len(set(group_answers)) for group_answers in ''.join(inp).split('::')]

# sum the resulting list values to get the sum of total questions answered
# by all groups
total_questions = sum(unique_questions)
print('Total questions answered by all groups is: ', total_questions)

"""
--- Part Two ---
As you finish the last group's customs declaration, you notice that you 
misread one word in the instructions:

You don't need to identify the questions to which anyone answered "yes"; 
you need to identify the questions to which everyone answered "yes"!

Using the same example as above:

abc

a
b
c

ab
ac

a
a
a
a

b
This list represents answers from five groups:

In the first group, everyone (all 1 person) answered "yes" to 3 questions: 
a, b, and c.
In the second group, there is no question to which everyone answered "yes".
In the third group, everyone answered yes to only 1 question, a. 
    Since some people did not answer "yes" to b or c, they don't count.
In the fourth group, everyone answered yes to only 1 question, a.
In the fifth group, everyone (all 1 person) answered "yes" to 1 question, b.
In this example, the sum of these counts is 3 + 0 + 1 + 1 + 1 = 6.

For each group, count the number of questions to which everyone answered "yes". 
What is the sum of those counts?
"""
# This time I will use Counter from collections 
# A very useful class to count occurence of a each element in a list (string)
from collections import Counter

# rearrange the given input by the group answers, 
# by replacing the empty lines with a special symbol (:: in this case)
group_answers = [i.strip().replace(' ', '') for i in ' '.join(inp).split('::')]

# get how many people there are in each group
members_in_group = [len(i.strip().split()) for i in ' '.join(inp).split('::')]

# use Counter to get how many questions were answered by each group
counts = [list(Counter(i).values()) for i in group_answers]

# zip two lists and use list.count() to compare the number of members in each group 
# and how many questions have the same occurence and then sum the output
all_counts = sum([a.count(b) for a, b in zip(counts, members_in_group)])

print('Count of questions answered by all members in each group is: ', all_counts)