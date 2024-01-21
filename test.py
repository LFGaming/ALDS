import random
import random
#%%
s = "test"
print(s[0])
print(s[1])
print(s[2])
print(s[3])
for i in reversed(range(len(s))):
    print(s[i])
# %%

#%%
def approximate_pi(N):
    Nin = 0
    for i in range(N):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            Nin += 1
    return 4 * Nin / N

print(approximate_pi(9000000))
#%%