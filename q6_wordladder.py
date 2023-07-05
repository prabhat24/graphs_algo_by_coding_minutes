from collections import deque


class Solution:

	def ladderLength(self, begin_word, end_word, word_list):
		q = deque()
		level = 1
		q.append([begin_word, level])
		word_list = set(word_list)
		while len(q) != 0:
			ele, level = q.popleft()
			if ele in word_list:
				word_list.remove(ele)
			if ele == end_word:
				return level

			for i in range(0, len(ele)):
				elest = ele[:i]
				eleend = ele[i+1:]
				for j in range(0, 26):
					if chr(ord('a') + j) == ele[i]:
						continue
					new_ele = elest + chr(ord('a') + j) + eleend
					if new_ele in word_list:
						q.append([new_ele, level+1])
		return 0
    		




if __name__ == '__main__':
	begin_word = "hit" 
	end_word = "cog"
	word_list = ["hot","dot","dog","lot","log"]
	sol = Solution()
	print(sol.ladderLength(begin_word, end_word, word_list))
