class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_counts = Counter(tasks)
        max_count = max(task_counts.values())
        num_max_tasks = sum(1 for count in task_counts.values() if count == max_count)
        result = (max_count - 1) * (n + 1) + num_max_tasks
        return max(result, len(tasks))
