import random
import time

print("50/50 ~ ViralCactus")
svar1 = input("[50/50] Mata in första halvan: \n>>")
svar2 = input("\n[50/50] Mata in andra halvan: \n>>")

samladesvar = [svar1, svar2]

print("\n[50/50]: " + random.choice(samladesvar))
time.sleep(5)
