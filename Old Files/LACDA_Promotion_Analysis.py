class LACDA_Promotion_Analysis(pre_people, post_people, pre_watch, post_watch, pre_reach, post_reach):
	#analyze data by status of promotion (only apply to promoted post)

	def ratio_people(pre_people, post_people):
		return post_people/pre_people
		#promotion works well on number of people watching?

	def ratio_watch(pre_watch, post_watch):
		return post_watch/pre_watch
		#promotion works well on number of watch times?

	def ratio_reach(pre_reach, post_reach):
		return post_reach/pre_reach
		#promotion works well on extending reach?