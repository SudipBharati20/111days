class RecommendationEngine:
    def get_best_task(self, tasks):
        if not tasks:
            return None
        tasks = [t for t in tasks if not t.completed]
        if not tasks:
            return None
        return max(tasks, key=lambda t: t.priority)