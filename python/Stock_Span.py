# Optimised Solution in complexity O(n):

def stockSpan(arr, n):
	s = []
	v = []
	span = []

	for i in range(0, n):
		while(len(s) != 0 and s[-1][0] <= arr[i]):
			s.pop()

		if len(s) == 0 :
			v.append(-1)

		else:
			v.append(s[-1][1])

		s.append([arr[i], i])

	for i in range(n):
		span.append(i - v[i])
	return span

if __name__ == '__main__':
    # arr = [100, 80, 60, 70, 60, 75, 85]
	arr = list(map(int,input().split()))
	ans = stockSpan(arr, len(arr))
	print(ans)


# Naive Solution O(N^2)

# lst = list(map(int, input().split()))
# l = len(lst)
# res = []
# res.append(1)
# for i in range(1, l):
#     count = 1
#     for j in range(i-1, -1, -1):
#         # print(lst[i], lst[j])
#         if lst[i] >= lst[j]:
#             count += 1
#         else:
#             res.append(count)
#             break
# print(res)
