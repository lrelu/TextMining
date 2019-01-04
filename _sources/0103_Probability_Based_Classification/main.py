# Naïve Bayes
# Prior, Likelihood, Posterior

#입력 데이터 주말, 맑음, 오후
indoor = [[1,0,1], [0,0,1], [0,0,1], [1,1,0], [0,1,0], [0,1,0]]
outdoor = [[1,1,0], [0,0,0], [1,1,0], [0,1,1]]

#indoor, outdoor 입력 데이터의 주말, 맑음, 오후의 각각의 우도 계산
def get_likelihood(data):
	c = [0,0,0]         #각각의 피쳐의 발생 횟수를 저장할 임시 변수
	p = [0.0, 0.0, 0.0] #우도 계산 결과

	for i in range(len(c)):
		for j in range(len(data)):
			c[i] += data[j][i]          #갯수 계산
		p[i] = c[i] / len(data)

	return p


print("indoor likelihood \n[주말, 맑음, 오후]")
print(get_likelihood(indoor))
print("outdoor likelihood \n[주말, 맑음, 오후]")
print(get_likelihood(outdoor))

#주말에 날씨가 맑을 경우, 어디에서 활동을?
#posterior = prior * likelihood

prior_indoor = len(indoor) / (len(indoor) + len(outdoor))
prior_outdoor = len(outdoor) / (len(indoor) + len(outdoor))

likelihood_indoor = get_likelihood(indoor)
likelihood_outdoor = get_likelihood(outdoor)

posterior_indoor = prior_indoor * likelihood_indoor[0] * likelihood_indoor[1]
posterior_outdoor = prior_outdoor * likelihood_outdoor[0] * likelihood_outdoor[1]

if (posterior_indoor > posterior_outdoor):
	print("결과: 실내에 있을 확율이 높습니다.")
else:
	print("결과: 야외에 나갈 확율이 높습니다.")

print("posterior_indoor: {0}".format(posterior_indoor))
print("posterior_outdoor: {0}".format(posterior_outdoor))

print("실내에 있을 확율: {0}%".format(posterior_indoor / (posterior_indoor + posterior_outdoor)))
print("야외에 있을 확율: {0}%".format(posterior_outdoor / (posterior_indoor + posterior_outdoor)))