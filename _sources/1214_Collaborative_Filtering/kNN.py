import user_item_rating_matrix
import cosine_similarity


class KNN:

	def get_neighbor_list(self, u, t):
		nbrlist = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]

		for i in range(len(Users.rating)):
			# 아이템t의 값을 구하려고 하는것이기 때문에 t가 0이 아닌 사람만 유사도를 측정한다.
			if (user[i][t] != 0):
				nbrlist[i] = [i, Distance.get_cos_sim(Users.rating[u], Users.rating[i])]

		# 코사인유사도를 내림차순으로 정렬 (1에 가까울수록 유사함)
		nbrlist = sorted(nbrlist, key=lambda nbr: nbr[1], reverse=True)

		return nbrlist

	# 특정 아이템에 대한 사용자의 평점 예측하기
	def get_rating_prediction(self, u, t):
		nbrlist = KNN.get_neighbor_list(u, t)

		# k가 3이라고 했을때 특정 사용자(u)와 가장 유사한 사용자의 소니 데이터의 평균
		return (Users.rating[nbrlist[0][0]][t] +
		        Users.rating[nbrlist[1][0]][t] +
		        Users.rating[nbrlist[2][0]][t]) / 3.0
