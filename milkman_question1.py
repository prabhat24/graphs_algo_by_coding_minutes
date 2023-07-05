
# Assume english alphabet letters can be given the values as a=1, b=2, c=3 and so on. Given the two numbers n and k, where n is number of letters and k is the sum of their values, find the lexicographically smallest string with n letters and sum of letters as k.
# Example 1: Input: n=3, k=27 Output: aay
# Example 2: Input: n=5, k=73 Output: aaszz

def get_face_value(val):
	return chr(val + ord('a') - 1)



def fill_values(n, k):
	num = n
	wt = k


	# iterate from right to left -> from n-1 to 0 
	# find out `new_digit` to be filled by using [weight left(wt) - spaces_left]
	# if new disit filled is less than z keep on filling `a`

	fillinga_flag = False
	ans = ""
	for i in range(n-1, -1, -1):
		print(i)
		if fillinga_flag:
			ans = "a" + ans
			continue
		else:
			spaces_left = i
			new_digit = wt - spaces_left
			if new_digit <= 26:
				ans = get_face_value(new_digit) + ans
				wt -= new_digit
				fillinga_flag = True
			else:
				ans = "z" + ans
				wt -= 26
	return ans


n=3
k=27
print(fill_values(n, k))