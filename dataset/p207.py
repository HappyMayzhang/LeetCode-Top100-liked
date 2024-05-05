from resounds import completions

def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    """你这个学期必须选修numCourses门课程，记为0到numCourses - 1 。在选修某些课程之前需要一些先修课程。 先修课程按数组prerequisites给出，其中prerequisites[i] = [ai, bi]，表示如果要学习课程ai则必须先学习课程bi。例如，先修课程对[0, 1]表示：想要学习课程0，你需要先完成课程1。请你判断是否可能完成所有课程的学习？"""

code = completions(canFinish)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(canFinish(2, [[1,0]]))
