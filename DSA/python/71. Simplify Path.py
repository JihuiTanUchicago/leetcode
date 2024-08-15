class Solution:
    def simplifyPath(self, path: str) -> str:
        path_stack = []
        path = path.split('/')
        for p in path:
            if p == "" or p == ".":
                continue
            if p == "..":
                if len(path_stack) > 0:
                    path_stack.pop()
            else:
                path_stack.append(p)
        path = '/' + '/'.join(path_stack)
        return path
