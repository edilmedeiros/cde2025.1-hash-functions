import random
import string
import time
from multiprocessing import Process, Event, Manager, cpu_count, Value

def simple_hash(s: str) -> str:
    hash_val = 0
    for char in s:
        hash_val = ((hash_val << 5) - hash_val + ord(char)) & 0xFFFFFFFF
    return f"{hash_val:08x}"

def search_collision(target, found, collision_result, batch_size=10000):
    tries = 0
    while not found.is_set():
        # Generate a batch of random strings
        candidates = [
            ''.join(random.choices(string.ascii_lowercase, k=7))
            for _ in range(batch_size)
        ]
        tries += batch_size
        for candidate in candidates:
            if candidate == "bitcoin":
                continue
            if simple_hash(candidate) == target:
                collision_result['candidate'] = candidate
                collision_result['tries'] = tries
                found.set()
                return

if __name__ == "__main__":
    target = simple_hash("bitcoin")
    print(f'Target hash for "bitcoin": {target}')

    manager = Manager()
    found = manager.Event()
    collision_result = manager.dict()

    num_processes = min(cpu_count(), 11)

    processes = []
    for i in range(num_processes):
        p = Process(target=search_collision, args=(target, found, collision_result))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    if collision_result:
        print(f'Collision found: "{collision_result["candidate"]}" after {collision_result["tries"]} tries (in one process).')
    else:
        print("No collision found.")
