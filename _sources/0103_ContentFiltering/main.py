#아이템 데이터 선언
#사과, 배, 딸기, 메론, 토마토
item = [[5,4,1], [4,4,2], [2,1,2], [3,5,3], [1,3,5]]
itme_name = ["사과", "배", "딸기", "메론", "토마토"]

items = {"사과":[5,4,1], "배":[4,4,2], "딸기":[2,1,2], "메론":[3,5,3], "토마토":[1,3,5]}

#유클리디안 거리 측정
def get_euclidean_sim(x, y):
	dist = 0.0

	for i in range(len(x)):
		dist += (x[i] - y[i]) ** 2

	return dist ** 0.5

#아이템 name(네임)와 유사한 아이템 리스트 구하기
def get_nbr_list_dic(n):
	# 빈 배열 정리
	nbrlist = {"사과":0, "배":0, "딸기":0, "메론":0, "토마토":0}

	for name in nbrlist:
		nbrlist[name] = get_euclidean_sim(items[n], items[name])

	#정렬
	result = sorted(nbrlist.items(), key=lambda nbr:nbr[1], reverse=False)

	return result[1][0], result[1][1]

#아이템 t(인덱스 값)와 유사한 아이템 리스트 구하기
def get_nbr_list(t):
	# 빈 배열 정리
	nbrlist = [[0,0], [1,0], [2,0], [3,0], [4,0]]

	# 유클리디안 거리 계산
	for i in range(len(item)):
		nbrlist[i] = [i, get_euclidean_sim(item[t], item[i])]

	# 소팅
	nbrlist = sorted(nbrlist, key=lambda nbr:nbr[1], reverse=False)

	# nbr 리스트 가져오기
	return nbrlist

def get_knn(t, k):
	#원하는 K 가져오기
	nbrlist = get_nbr_list(t)
	return nbrlist[1:1+k]


#멜론와 유사한 리스트
print("nbrlist: ", get_nbr_list(3))
print("")

#멜론과 비슷한 과일 2개 가져오기
nbrlist = get_knn(3, 2)

#출력
for i in range(len(nbrlist)):
	print("{0}순위: {1}".format(i+1, itme_name[nbrlist[i][0]]))


fruit, distance = get_nbr_list_dic("메론")
print("{0} 을(를) 추천합니다. 거리: {1}".format(fruit, distance))