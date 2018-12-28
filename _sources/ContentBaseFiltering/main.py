#아이템 데이터 (당도, 크기, 수분함량)
item = [[5,4,1],[4,4,2],[2,1,2],[3,5,3],[1,3,5]]

#유클리디안 거리 측정
def get_euclidean_sim(x, y):
	dist = 0.0

	for i in range(len(x)):
		dist += (x[i] - y[i]) ** 2

	return dist ** 0.5

#아이템 t(인덱스 값)와 유사한 아이템 리스트 구하기
def get_nbr_list(t):
	nbrlist = [[0,0],[1,0],[2,0],[3,0],[4,0]]

	for i in range(len(item)):

		if (i != t):        #동일 아이템 건너뛰기
			nbrlist[i] = [i, get_euclidean_sim(item[t], item[i])]

	nbrlist = sorted(nbrlist, key = lambda nbr:nbr[1], reverse=False)
s
	return nbrlist


#특정 아이템의 유클리디안 거리 측정
print(get_euclidean_sim(item[0], item[1]))

#유클리디안으로 구하여 1번과일과 남은 과일들의 유사도 리스트
print(get_nbr_list(1))

#사용자1이 메론(i=3)을 좋아할 경우, 유사한 아이템을 추천
print(get_nbr_list(3))