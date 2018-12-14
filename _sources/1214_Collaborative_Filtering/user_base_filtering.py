# 텍스트 마이닝의 기본
# 사용자 베이스 필터링
# 데이터: 사용자별 제조사 별점 데이터 (애플, 삼성, LG, 소니, 샤오미)
# 유사도 알고리즘: 코사인 유사도
# 결과: 코사인 유사도를 이용하여 특정사람의 특정회사의 별점을 예측함

rating = [[4,0,5,0,1], [0,3,3,0,1], [3,0,4,2,1], [3,5,5,2,2], [0,0,2,0,0], [0,4,0,3,0],
	             [1,2,1,0,3], [3,4,4,1,1], [2,0,1,3,3]]

# 코사인 유사도 측정
def get_cos_sim(x, y):
	dot = 0
	norm_x = 0
	norm_y = 0

	for i in range(len(x)):
		dot += x[i] * y[i]
		norm_x += x[i] * x[i]
		norm_y += y[i] * y[i]

	return dot / ((norm_x ** 0.5) * (norm_y ** 0.5))


def get_neighbor_list(u, t):
	nbrlist = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]

	for i in range(len(rating)):
		# 아이템t의 값을 구하려고 하는것이기 때문에 t가 0이 아닌 사람만 유사도를 측정한다.
		if (rating[i][t] != 0):
			nbrlist[i] = [i, get_cos_sim(rating[u], rating[i])]

	# 코사인유사도를 내림차순으로 정렬 (1에 가까울수록 유사함)
	nbrlist = sorted(nbrlist, key=lambda nbr: nbr[1], reverse=True)

	return nbrlist


# 특정 아이템에 대한 사용자의 평점 예측하기
def get_rating_prediction(u, t):
	nbrlist = get_neighbor_list(u, t)

	print(nbrlist);

	# k가 3이라고 했을때 특정 사용자(u)와 가장 유사한 사용자의 소니 데이터의 평균
	return (rating[nbrlist[0][0]][t] +
	        rating[nbrlist[1][0]][t] +
	        rating[nbrlist[2][0]][t]) / 3.0


print (get_rating_prediction(0, 1))

score = get_rating_prediction(0, 3)
if (score >= 3.0):
	print("소니폰을 추천합니다.")
else:
	print("소니폰을 추천하지 않습니다.")

