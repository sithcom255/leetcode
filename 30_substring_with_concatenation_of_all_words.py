from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        text_l = len(words[0])
        res = []




        for f_yoi in range(text_l):
            l = f_yoi
            w = dict()
            for word in words:
                if word in w:
                    w[word] += 1
                else:
                    w[word] = 1
            for i in range(f_yoi, len(s), text_l):
                substring = s[i: min(i + text_l, len(s))]

                if not w:
                    add = s[l: l + text_l]
                    if add in w:
                        w[add] += 1
                    else:
                        w[add] = 1
                    l += text_l

                if substring in w:
                    c = w[substring]
                    if c == 1:
                        del w[substring]
                        if not w:
                            res.append(l)
                    elif c > 0:
                        w[substring] -= 1
                    continue

                next = True
                while l < i and next:
                    add = s[l:l + text_l]
                    if add in w:
                        w[add] += 1
                    else:
                        w[add] = 1
                    l += text_l

                    if substring in w:
                        c = w[substring]
                        if c == 1:
                            del w[substring]
                            next = False
                            continue
                        elif c > 0:
                            w[substring] -= 0
                            next = False
                            continue

                if l == i and next:
                    l += text_l
        return res


if __name__ == '__main__':
    print([0, 9] == Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
    print([6, 9, 12] == Solution().findSubstring("barfoofoobarthefoobarman", ["bar", "foo", "the"]))
    print([8] == Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print([8] == Solution().findSubstring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]))
    print(Solution().findSubstring("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo","barr","wing","ding","wing"]))
    print(Solution().findSubstring("aaaaaaaaaaaaaa", ["aa", "aa"]))
