# 사용자 데이터 선언 (애플 | 삼성 | LG | 소니 | 샤오미)
user_rating = [[4, 0, 5, 0, 1], [0, 3, 3, 0, 1], [3, 0, 4, 2, 1], [3, 5, 5, 2, 2], [0, 0, 2, 0, 0], [0, 4, 0, 3, 0],
               [1, 2, 1, 0, 3], [3, 4, 4, 1, 1], [2, 0, 1, 3, 3]]


# 코사인 유사도 측정
def get_cos_sim(user1, user2):
	dot = 0
	norm_user1 = 0
	norm_user2 = 0

	for i in range(len(user1)):
		dot += user1[i] * user2[i]  # 내적 구하기
		norm_user1 += user1[i] * user1[i]  # 각 요소의 제곱의 합
		norm_user2 += user2[i] * user2[i]  # 각 요소의 제곱의 합

	return dot / ((norm_user1 ** 0.5) * (norm_user2 ** 0.5))


# 소니 사용자중 특정 사용자와 유사항 사용자 리스트 구하기
def get_neighbor_list(user, item):
	# 순위를 담을 빈 리스트 추가
	neighborList = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]

	# 코사인 유사도 값 계산
	for i in range(len(neighborList)):
		# 인자로 받은 아이템의 값이 0이면 패스
		if (user_rating[i][item] != 0):
			neighborList[i] = [i, get_cos_sim(user_rating[user], user_rating[i])]

	# 구해진 코사인 유사도 값(neighbor리스트의 1번째 값)으로 내림차순
	neighborList = sorted(neighborList, key=lambda nbr: nbr[1], reverse=True)

	return neighborList


# 특정 아이템에 대한 사용자의 평점 구하기
def get_rating_prediction(user, item):
	neighborList = get_neighbor_list(user, item)

	# 가장 유사도가 큰 앞의 3명의 사용자의 소니값의 평균
	return (user_rating[neighborList[0][0]][item] + user_rating[neighborList[1][0]][item] +
	        user_rating[neighborList[2][0]][item]) / 3.00


print(get_neighbor_list(0, 3))

# 첫번째 사용자의 소니 평점을 예측하자
print(get_rating_prediction(0, 3))