class LACDA_PostType_Analysis(total_watch, total_people, likes, shares, comments):
	#analyze data by the type of the post

	def ratio_watch(total_watch, total_people):
		return total_watch/total_people
		#number of people who replay the video

	def ratio_likes(likes, total_people):
		return likes/total_people
		#number of people like this topic/type

	def ratio_shares(shares, total_people):
		return shares/total_people
		#number of people like this topic/type so much that they want to share it

	def ratio_comments(comments,total_people):
		return comments/total_people
		#number of people who want to talk about this topic/type
		