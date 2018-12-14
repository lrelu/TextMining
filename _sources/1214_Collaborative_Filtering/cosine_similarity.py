class Distance:

	# 코사인 유사도 측정
	def get_cos_sim(self, x, y):
		dot = 0
		norm_x = 0
		norm_y = 0

		for i in range(len(x)):
			dot += x[i] * y[i]
			norm_x += x[i] * x[i]
			norm_y += y[i] * y[i]

		return dot / ((norm_x ** 0.5) * (norm_y ** 0.5))

