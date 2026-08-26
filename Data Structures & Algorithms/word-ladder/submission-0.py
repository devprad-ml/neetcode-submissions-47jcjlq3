class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        if beginWord == endWord:
            return 1
        
        q = deque([(beginWord, 1)])

        while q:
            word, steps = q.popleft()

            if word == endWord:
                return steps + 1
            
            for i in range(len(beginWord)):
                for c in range(ord('a'), ord('z')+1):
                    if ord(word[i]) == c:
                        continue
                    new_word = word[:i] + chr(c) + word[i+1:]

                    if new_word == endWord:
                        return steps+1
                
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        q.append((new_word, steps+1))
        return 0
            
                
        