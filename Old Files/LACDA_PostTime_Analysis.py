class LACDA_PostTime_Analysis(total_people, total_reach, likes, shares, comments):
	#analyze data base on post time

	def ratio_reach(total_people, total_reach):
		return total_people/total_reach
		#how many people watch the post at that time?

	def ratio_likes(likes, total_people):
		return likes/total_people
		#do people have time to react to post at that time?

	def ratio_shares(shares, total_people):
		return shares/total_people
		#do people have time to react to post at that time?

	def ratio_comments(comments, total_people):
		return comments/total_people
		#do people have time to react to post at that time?