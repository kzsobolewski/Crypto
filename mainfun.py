from LCG import LCG
from PrngCracker import PRNGCracker

lcg = LCG(
    seed=123,
    mod=2 ** 31,
    multiplier=17389,
    addends=54321
)

prng_cracker = PRNGCracker()

previous_states = []
for i in range(10):
    previous_states.append(lcg.run())

prng_cracker.find_parameters(previous_states)

predicted = prng_cracker.run(previous_states[-1])
generated = lcg.run()

print("Predicted: ", predicted)
print("From the Generator: ", generated)
