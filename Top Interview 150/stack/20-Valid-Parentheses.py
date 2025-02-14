class Solution(object):
    def isValid(self, s):
        \\\
        :type s: str
        :rtype: bool
        \\\
        \\\
        :type s: str
        :rtype: bool
        \\\

        stack_s = [] #initialization

        hash_map = {\)\:\(\, \]\:\[\, \}\:\{\}
        # left = [\(\, \[\, \{\]
        # right = [\)\, \]\, \}\]

        for char in s:
            if char in hash_map.values():
                stack_s.append(char)
            elif char in hash_map.keys():
                
                if not stack_s:
                    return False
                elif stack_s[-1] == hash_map[char]:
                    stack_s.pop()
                else:
                    return False
        
        if not stack_s:
            return True
        else:
            return False
