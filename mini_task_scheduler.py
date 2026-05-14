# Imagine you are managing 3 workers in a company.
# Each worker can do tasks, and every task takes a certain amount of time.
#
# You are given a list of task durations:
#
# tasks = [5, 2, 7, 1, 4, 3]
#
# Your program should:
#
# Create 3 workers, each starting with workload 0
# Go through the tasks one by one
# Always assign the next task to the worker with the SMALLEST current workload
# After each assignment, print:
# which worker received the task
# the updated workloads of all workers
# At the end, print the final workloads
#
# Example idea:
#
# Worker 1 gets task 5
# Current loads: [5, 0, 0]
#
# Worker 2 gets task 2
# Current loads: [5, 2, 0]
#
# You may use:
#
# lists
# loops
# conditions
# min()
# .index()

# tasks = [5, 2, 7, 1, 4, 3, 1]
# workers = [0, 0, 0]
# Task 5:
# workers = [5, 0, 0]
# Task 2:
# workers = [5, 2, 0]
# Task 7:
# workers = [5, 2, 7]
# Task 1:
# workers = [5, 2+1, 7] = [5, 3, 7]
# task 4:
# workers = [5, 7, 7]
# task 3:
# workers = [8, 7, 7]
# task 1:
# workers = []

tasks = [5, 2, 7, 1, 4, 3]
workers = [0, 0, 0]

for task in tasks:
    smallest_worker = workers.index(min(workers))

    workers[smallest_worker] += task

    print(f"Worker {smallest_worker + 1} get task {task}")
    print("Current workloads:", workers)

print("Final workloads:", workers)