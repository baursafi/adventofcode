
"""
--- Day 7: Handy Haversacks ---
You land at the regional airport in time for your next flight. 
In fact, it looks like you'll even have time to grab some food: 
all flights are currently delayed due to issues in luggage processing.

Due to recent aviation regulations, many rules (your puzzle input) 
are being enforced about bags and their contents; bags must be 
color-coded and must contain specific quantities of other color-coded bags. 
Apparently, nobody responsible for these regulations considered 
how long they would take to enforce!

For example, consider the following rules:

light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
These rules specify the required contents for 9 bag types. In this example, 
every faded blue bag is empty, every vibrant plum bag contains 11 bags 
(5 faded blue and 6 dotted black), and so on.

You have a shiny gold bag. If you wanted to carry it in at least one other bag, 
how many different bag colors would be valid for the outermost bag? 
(In other words: how many colors can, eventually, contain at least one shiny gold bag?)

In the above rules, the following options would be available to you:

A bright white bag, which can hold your shiny gold bag directly.
A muted yellow bag, which can hold your shiny gold bag directly, 
plus some other bags.
A dark orange bag, which can hold bright white and muted yellow bags, 
either of which could then hold your shiny gold bag.
A light red bag, which can hold bright white and muted yellow bags, 
either of which could then hold your shiny gold bag.
So, in this example, the number of bag colors that can eventually 
contain at least one shiny gold bag is 4.

How many bag colors can eventually contain at least one shiny gold bag? 
(The list of rules is quite long; make sure you get all of it.)
"""

with open('input.txt', 'r') as f:
    inp = f.readlines()

# collects the unique bag types in one run
def bags(bag, inp = inp):
    bags = set()
    for i in inp:
        if bag in i.split('contain')[1]:
            bags.add(i.split('bags')[0])
    return bags

# recursively apply 
colors = set()
def bags_in_bags(initial_color):
    for color in bags(initial_color):
        colors.add(color)
        bags_in_bags(color)
    return colors

number_of_bags = bags_in_bags('shiny gold')

"""
--- Part Two ---
It's getting pretty expensive to fly these days - not because of ticket prices, 
but because of the ridiculous number of bags you need to buy!

Consider again your shiny gold bag and the rules from the above example:

faded blue bags contain 0 other bags.
dotted black bags contain 0 other bags.
vibrant plum bags contain 11 other bags: 5 faded blue bags and 6 dotted black bags.
dark olive bags contain 7 other bags: 3 faded blue bags and 4 dotted black bags.
So, a single shiny gold bag must contain 1 dark olive bag (and the 7 bags within it) plus 
2 vibrant plum bags (and the 11 bags within each of those): 1 + 1*7 + 2 + 2*11 = 32 bags!

Of course, the actual rules have a small chance of going several levels deeper than this example; 
be sure to count all of the bags, even if the nesting becomes topologically impractical!

Here's another example:

shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags.
In this example, a single shiny gold bag must contain 126 other bags.

How many individual bags are required inside your single shiny gold bag?
"""

import numpy as np
from collections import defaultdict
from tqdm import tqdm

# read the input into lines
with open('input.txt', 'r') as f:
    inp = f.readlines()

# formalize a recursive function
def text_rec(bag_type='shiny gold', inp=inp):
    """returns the number of bags contained in the bag 
        of the initial type. It's a recursive function that 
        describes the first initial logic and returns 
        an output that reuses the same function but on the other 
        bag types found inside the previous bag

    Args:
        bag_type (str, optional): bag type. Defaults to 'shiny gold'.
        inp ([type], optional): input is the list of strings. Defaults to inp.

    Returns:
        int: returns the resulting number of bags in bags
    """
    # find the line that contains the sought bag type
    line = [line for line in inp if bag_type in line.split('bags contain')[0]][0]
    # if line has "no other bags" in line the output defaults to zero
    if 'no other' in line:
        return 0
    # otherwise, extract the multiplier for each type of bags found
    bag_number = [eval(bag.split(' ')[0].strip()) for bag in line.split('bags contain')[1].strip().split(', ')]
    # since the bags are in the original bag even if they don't have anything inside them
    # would still add to the total count
    total_bags = sum(bag_number)
    # get the list of the bag types in the original bag 
    bags = [' '.join(bag.split(' ')[1:3]).strip() for bag in line.split('bags contain')[1].strip().split(', ')]
    print()
    print(line)
    return total_bags + sum([count*text_rec(bag) for count, bag in zip(bag_number, bags)])

text_rec()

