# Raport
Program simply predicts the next number of linear congruencial generator. I requires couple of generated numbers to work corectly.

*package functools is used in the script

mainfun.py makes LCG objects and generates 10 pseduo-random numbers, whitch are used in PRNGCracker object to find all parameters. After that the script prints predicted number and the one from the real generator.

PRNGCracker.py has 3 main methods:

find_addends simply calculate the increment value from 2 output numbers by soving the equation. 

find_multiplier calculates multiplier value by solving system of equations with 3 LCG numbers. The system is simplified to one equation whitch needs to use modular inverse function modinv from the utils.py file.

find_mod finds the modulus value using number theory fact that if we have few random multiples of n, with large probability their GCD will be equal to n.
Difference between neighbor numbers (t0, t1...) is computed with the equation:
>t2 * t0 - t1 * t1 = (m * m * t0 * t0) - (m * t0 * m * t0) = 0 (mod n)
m - multiplier

this way we get numbers which GCD is LCG multiplier.

After finding modulus, script finds multiplier and iterator.