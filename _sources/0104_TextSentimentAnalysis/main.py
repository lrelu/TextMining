# 입력데이터
negative = ["재미 없음 지루하고 평범", "뻔한 스토리, 감동 없음", "웃음도 없고 신선하지도 않음"]
positive = ["올해 본 영화 중 가장 재미 있음", "감동 백배"]

#불필요 단어 제거 및 리스트화
def preprocess(text):
	#원래는 자연어처리(형태소 분석기)를 사용하여 단어를 추려야 하지만 여기선 임시로 그냥 처리
	return text.replace(',','').replace(' 중','').replace(' 본','').split()

#입력 리뷰 문장의 부정, 긍정 감성 각각의 확율 계산
def get_likelihood(data):

	#입력 데이터의 feature(단어 리스트)구하기
	d = preprocess(' '.join(data))              #모든 문장을 공백넣어 한문장으로 합친후, 전처리
	f = list(set(d))                            #중복단어가 없는 피쳐리스트 만듬
	c = [0] * len(f)                            #피쳐리스트 카운트 담을 리스트
	p = {}                                      #결과셋 담을 리스트

	for i in range(len(f)):
		for j in range(len(d)):
			if f[i] in d[j]:
				c[i] += 1
		p[f[i]] = c[i] / len(d)

	return p


def get_likelihood_Q(text):
	features = preprocess(text)
	likelihood_p = 1.0
	likelihood_n = 1.0

	feature_p = get_likelihood(positive)
	feature_n = get_likelihood(negative)

	for feature in features:
		#우도계산 - positive
		if feature in feature_p:
			#피쳐가 있을 경우에 우도 계산
			likelihood_p *= feature_p[feature]
		else:
			#피쳐가 처음 나올 경우에 평활화
			likelihood_p *= 1 / (len(feature_p) + 2)

		# 우도계산 - negative
		if feature in feature_n:
			# 피쳐가 있을 경우에 우도 계산
			likelihood_n *= feature_n[feature]
		else:
			# 피쳐가 처음 나올 경우에 평활화
			likelihood_n *= 1 / (len(feature_n) + 2)

	return likelihood_p, likelihood_n


print(get_likelihood(positive))
print(get_likelihood(negative))

#prior 계산
prior_positive = len(positive) / (len(positive) + len(negative))
prior_negative = len(negative) / (len(positive) + len(negative))

#likelihood 계산
#재미, 감동 있음 내용은 평범
text = "재미, 감동 있음 내용은 평범"
likelihood_positivie, likelihood_negative = get_likelihood_Q(text)

#posterior 계산
posterior_positive = prior_positive * likelihood_positivie
posterior_negative = prior_negative * likelihood_negative

if (posterior_positive > posterior_negative):
	print("해당 댓글은 긍정일 확율이 높습니다.")
else:
	print("해당 댓글은 부정일 확율이 높습니다.")

print("p:{0:10e} n:{1:10e}".format(posterior_positive, posterior_negative))