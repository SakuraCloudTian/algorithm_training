from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0] * numCourses      # 入度：某课程需要先完成几门课
        out_degree = [0] * numCourses     # 出度：某课程是其他课程的前置课
        graph = defaultdict(list)

        # 构建入度和出度图
        for a, b in prerequisites:
            in_degree[a] += 1      # a 需要先完成 b，所以 a 的入度 +1
            out_degree[b] += 1     # b 是 a 的前置课，所以 b 的出度 +1
            graph[b].append(a)

        # 找出初始入度或出度为 0 的课程（安全点）
        safe_courses = set(i for i in range(numCourses) if in_degree[i] == 0 or out_degree[i] == 0)

        # 用 set 记录已经删除的课程
        removed = set()

        while safe_courses:
            course = safe_courses.pop()
            removed.add(course)

            # 删除该课程后，更新与它连接的课程的入度和出度
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if neighbor not in removed and (in_degree[neighbor] == 0 or out_degree[neighbor] == 0):
                    safe_courses.add(neighbor)

            # 也要更新被该课程指向的课程（反向）
            for i in range(numCourses):
                if course in graph[i]:
                    out_degree[i] -= 1
                    if i not in removed and (in_degree[i] == 0 or out_degree[i] == 0):
                        safe_courses.add(i)

        # 最后检查是否所有课程都被安全删除
        return len(removed) == numCourses
        