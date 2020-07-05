class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        wordList = set(wordList)
        l = len(beginWord)
        deque = collections.deque()
        deque.append((beginWord,[beginWord]))
        vistited = set()
        vistited.add(beginWord)
        res = []
        flag = False
        while deque:
            new_visited = set()
            n = len(deque)      
            for i in range(n):
                a,path = deque.popleft()
                if a == endWord:
                    res.append(path)
                for j in range(l):
                    b = list(a)
                    for k in range(26):
                        if chr(ord('a') + k) == a[j]:
                            continue
                        b[j] = chr(ord('a') + k)
                        c = ''.join(b)
                        if c in wordList:
                            if c == endWord:
                                flag == True
                            if c not in vistited: 
                                deque.append((c,path+[c]))
                                new_visited.add(c)  #同一层的节点不需要判重
            vistited |= new_visited
            if flag:
                break
        return res