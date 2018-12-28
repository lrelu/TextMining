#아이템 데이터 선언
items = [[4,0,3,3,0,0,1,3,2],
         [0,3,0,5,0,4,2,4,0],
         [5,3,4,5,2,0,1,4,1],
         [0,0,2,2,0,3,0,1,3],
         [1,1,1,2,0,0,3,1,3]]

#코사인 유사도 구하기
#코사인 유사도 = 내적 / item1의 요소제곱의 합의 루트 * item2의 요소제곱의 합의 루트
def get_cos_sim(item1, item2):
	dot = 0
	norm_item1 = 0
	norm_item2 = 0

	for i in range(len(items)):
		dot += item1[i] * item2[i]
		norm_item1 += item1[i] * item1[i]
		norm_item2 += item2[i] * item2[i]

	return dot / ((norm_item1 ** 0.5) * (norm_item2 ** 0.5))

#코사인 유사도에 의한 네이버리스트 구하기
def get_nbrlist(item_idx, user_idx):

	# 빈 배열 선언
	nbrlist = [[0,0], [1,0], [2,0], [3,0], [4,0]]

	for i in range(len(nbrlist)):
		# 해당 아이템의 사용자값이 0이 아닌것만 코사인 유사도 계산
		#if (items[i][user_idx] != 0):
		nbrlist[i] = [i, get_cos_sim(items[item_idx], items[i])]

	#구해진 코사인 유사도에 따라 내림차순으로 정렬
	nbrlist = sorted(nbrlist, key = lambda nbr:nbr[1], reverse=True)

	return nbrlist

# K=2로 설정
def prediction(item_idx, user_idx):
	nbrlist = get_nbrlist(item_idx, user_idx)

	# 단순히 KNN의 값의 평균으로 예측
	# return (items[nbrlist[1][0]][user_idx] + items[nbrlist[2][0]][user_idx]) / 2.00

	# 각 순위의 가중치를 추가하여 평균으로 예측
	#유사도 순위1
	no1 = items[nbrlist[1][0]][user_idx]
	#유사도 순위2
	no2 = items[nbrlist[2][0]][user_idx]

	total = no1 + no2
	#가중치1
	weight1 = no1 / total
	#가중치2
	weight2 = no2 / total


	return ((no1 * weight1) + (no2 * weight2)) / 2.00

# 0번째 아이템의 두번째 사용자의 예측값
print(get_nbrlist(1, 0))

#print(get_cos_sim(items[0], items[1]))

# 삼성 아이템의 사용자1의 예측값
print("삼성 아이템의 사용자1의 예측값: ", prediction(1, 0))