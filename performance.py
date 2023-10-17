import threading
import time
import random
# Function to simulate a profile creation process with user information
def create_profile(profile_id):
    username = f"user{profile_id}"
    email = f"user{profile_id}@example.com"
    password = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789') for _ in range(8))
    print(f"Creating profile {profile_id}:")
    print(f"Username: {username}")
    print(f"Email: {email}")
    print(f"Password: {password}")   
    # Simulate some processing time (2 seconds)
    time.sleep(2)
    print(f"Profile {profile_id} created")
# Number of profiles to create
num_profiles = 5
# Create a list of threads
threads = []
# Start time of the test
start_time = time.time()
# Create threads for profile creation
for i in range(num_profiles):
    thread = threading.Thread(target=create_profile, args=(i,))
    threads.append(thread)
    thread.start()
# Wait for all threads to finish
for thread in threads:
    thread.join()
# End time of the test
end_time = time.time()
# Calculate the total test duration
total_duration = end_time - start_time
print(f"Total test duration: {total_duration:.2f} seconds")
