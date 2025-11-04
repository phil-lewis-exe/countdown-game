import time

print("hello", time.time())
time.sleep(1)
print("goodbye", time.time())

# 1_762_257_245.313716
# number of seconds since Jan 1st 1970

x = 30
for i in range(x):
    print(x-i, end=" ", flush=True)
    time.sleep(1)
print()
print("timer is up")


time_now = time.time()
print("Press enter when ready")
user_ans = input(">")
time_next = time.time()

print(f"you took {time_next - time_now} seconds")