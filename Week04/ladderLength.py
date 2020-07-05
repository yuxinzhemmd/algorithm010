class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # nums = collections.defaultdict(list)
        # for word in wordList:
        #     for i in range(len(beginWord)):
        #         nums[]
        # wordList = set(wordList)
        # l = len(beginWord)
        # deque = collections.deque([beginWord])
        # vistited = set()
        # step = 1
        # while deque:
        #     n = len(deque)
        #     for i in range(n):
        #         a = deque.popleft()
        #         for j in range(l):
        #             b = a[j]
        #             for k in range(26):
        #                 if chr(ord('a') + k) == a[j]:
        #                     continue
        #                 c = list(a)
        #                 c[j] = chr(ord('a') + k)
        #                 c = ''.join(c)
        #                 if c in wordList:
        #                     if c == endWord:
        #                         step += 1
        #                         return step
        #                     if c not in vistited:
        #                         deque.append(c)
        #                         vistited.add(c)
        #     step += 1
        # return 0
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set(beginWord)
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                visited.add(next_word)
                    word_list[j] = origin_char
            step += 1
        return 0