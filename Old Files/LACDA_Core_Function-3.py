import xlrd

class LACDA_Core:
	file = xlrd.open_workbook("Facebook Insights Data Export (Post Level) - LOK - 2017-07-27.xlsx")
	main_sheet = file.sheet_by_name("Key Metrics")
	minor_sheet = file.sheet_by_name("Lifetime Talking About This(...")
	data_col = {}

	data_entry = ["Post ID", "Permalink", "Type", "Posted", "post_impressions_unique:lifetime", "post_impressions_paid_unique:lifetime", "post_engaged_users:lifetime", "post_video_complete_views_organic_unique:lifetime", "post_video_complete_views_organic:lifetime", "post_video_complete_views_paid_unique:lifetime", "post_video_complete_views_paid:lifetime", "post_video_views_organic_unique:lifetime", "post_video_views_organic:lifetime", "post_video_views_paid_unique:lifetime", "post_video_views_paid:lifetime", "post_video_avg_time_watched:lifetime", "post_video_length:lifetime", "Content", "share", "like", "comment"]

	#get column index
	def get_col_index(self, colname, sheetname):
		for colindex in range(0, sheetname.ncols):
			if sheetname.cell(0, colindex).value == colname:
				return colindex


	# for i in range(0, len(data_entry)):
	# 	if data_entry[i] == "share" or data_entry[i] == "like" or data_entry[i] == "comment":
	# 		data_col[data_entry[i]] = get_col_index(data_entry[i], minor_sheet)
	# 	else:
	# 		data_col[data_entry[i]] = get_col_index(data_entry[i], main_sheet)

	#post's likes
	def get_like(self, Permalink):
		like_index = get_col_index("like", minor_sheet)
		link_index = get_col_index("Permalink", minor_sheet)
		for index in range(self.minor_sheet.nrows):
			if self.minor_sheet.cell(index, link_index).value == Permalink:
				return self.minor_sheet.cell(index, like_index).value

	#post's shares
	def get_share(self, Permalink):
		share_index = get_col_index("share", minor_sheet)
		link_index = get_col_index("Permalink", minor_sheet)
		for index in range(self.minor_sheet.nrows):
			if self.minor_sheet.cell(index, link_index).value == Permalink:
				return self.minor_sheet.cell(index, share_index).value

	#post's comments
	def get_comment(self, Permalink):
		cmt_index = get_col_index("comment", minor_sheet)
		link_index = get_col_index("Permalink", minor_sheet)
		for index in range(self.minor_sheet.nrows):
			if self.minor_sheet.cell(index, link_index).value == Permalink:
				return self.minor_sheet.cell(index, cmt_index).value

	#post's view
	def get_reach(self, Permalink):
		link_index = get_col_index("Permalink", main_sheet)
		unpaid_index = get_col_index("post_impressions_unique:lifetime", main_sheet)
		paid_index = get_col_index("post_impressions_paid_unique:lifetime", main_sheet)
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, link_index).value == Permalink:
				if self.main_sheet.cell(index, paid_index).value != 0:
					return self.main_sheet.cell(index, paid_index).value
				else:
					return self.main_sheet.cell(index, unpaid_index).value

	#post's reaction ratio
	def get_reaction_ratio(self, Permalink):
		link_index = get_col_index("Permalink", main_sheet)
		reach = get_reach(Permalink)
		ratio = {'like', 'share', 'comment'}
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, link_index).value == Permalink:
				ratio['like'] = get_like(Permalink)/reach
				ratio['share'] = get_share(Permalink)/reach
				ratio['comment'] = get_comment(Permalink)/reach
				return ratio

	#topic's reaction and their ratio with reach
	def get_topic_reaction(self, topic):
		arranged = arrange_topic()
		if not arranged.has_key(topic):
			return null
		reaction = {'like', 'share', 'comment', 'like ratio', 'shrae ratio', 'comment ratio'}
		total_reach = 0
		total_like = 0
		total_share = 0
		total_comment = 0
		for index in range(len(arranged[topic])):
			total_view += get_reach(arranged[topic][index])
			total_like += get_like(arranged[topic][index])
			total_share += get_share(arranged[topic][index])
			total_comment += get_comment(arranged[topic][index])
		reaction['like'] = total_like
		reaction['share'] = total_share
		reaction['comment'] = total_comment
		reaction['like ratio'] = total_like/total_reach
		reaction['share ratio'] = total_share/total_reach
		reaction['comment ratio'] = total_comment/total_reach
		return reaction

	#list of topic with posts
	def arrange_topic(self):
		topic_index = get_col_index("Topic", main_sheet)
		link_index = get_col_index("Permalink", main_sheet)
		arranged = {}
		for index in range(self.main_sheet.nrows):
			if not arranged_topic.has_key(self.main_sheet.cell(index, topic_index)):
				arranged[self.main_sheet.cell(index, topic_index)] = []
				arranged[self.main_sheet.cell(index, topic_index)].append(self.main_sheet.cell(index, link_index))
			else:
				arranged[self.main_sheet.cell(index, topic_index)].append(self.main_sheet.cell(index, link_index))
		return arranged

	#95% views/total views
	def get_audience_ratio(self, Permalink):
		link_index = self.get_col_index("Permalink", self.main_sheet)
		complete_paid_index = self.get_col_index("post_video_complete_views_paid_unique:lifetime", self.main_sheet)
		total_paid_index = self.get_col_index("post_video_views_paid_unique:lifetime", self.main_sheet)
		complete_unpaid_index = self.get_col_index("post_video_complete_views_organic_unique:lifetime", self.main_sheet)
		total_unpaid_index = self.get_col_index("post_video_views_organic_unique:lifetime", self.main_sheet)
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, link_index).value == Permalink: 				#search for the needed link in the column index Permalink
				if (self.main_sheet.cell(index, complete_paid_index).value != 0) and (self.main_sheet.cell(index, total_paid_index).value != 0):
					audience_watch_full = self.main_sheet.cell(index, complete_paid_index).value
					audience_total = self.main_sheet.cell(index, total_paid_index).value
				elif (self.main_sheet.cell(index, complete_unpaid_index).value != 0) and (self.main_sheet.cell(index, total_unpaid_index ).value != 0):
					audience_watch_full = self.main_sheet.cell(index, complete_unpaid_index).value
					audience_total = self.main_sheet.cell(index, total_unpaid_index).value	
				else:
					return -1	 		
		return (audience_watch_full) / (audience_total) 

	#average watch duration
	def get_average_duration(self, Permalink):
		link_index = self.get_col_index("Permalink", self.main_sheet)
		average_index = self.get_col_index("post_video_avg_time_watched:lifetime", self.main_sheet)
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, link_index).value == Permalink:
				return (self.main_sheet.cell(index, average_index).value / 1000)

	#average duration/total duration
	def get_duration_ratio(self, Permalink):
		link_index = self.get_col_index("Permalink", self.main_sheet)
		average_index = self.get_col_index("post_video_avg_time_watched:lifetime", self.main_sheet)
		length_index = self.get_col_index("post_video_length:lifetime", self.main_sheet)
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, link_index).value == Permalink:
				return (self.main_sheet.cell(index, average_index).value / self.main_sheet.cell(index, length_index).value)

	#promotion efficiency
	def get_promotion_ratio(self, Permalink):
		unique_paid_index = self.get_col_index("post_video_views_paid_unique:lifetime", self.main_sheet)
		total_paid_index = self.get_col_index("post_video_views_paid:lifetime", self.main_sheet)
		unique_unpaid_index = self.get_col_index("post_video_views_organic_unique:lifetime", self.main_sheet)
		total_unpaid_index = self.get_col_index("post_video_views_organic:lifetime", self.main_sheet)
		link_index = self.get_col_index("Permalink", self.main_sheet)		
		promotion_ratio = {'audience': [], 'watch_time': [], 'reach': [] }
		for index in range(self.main_sheet.nrows):
			if self.main_sheet.cell(index, 1).value == Permalink:
				promotion_ratio['audience'].append(self.main_sheet.cell(index, unique_unpaid_index).value / self.main_sheet.cell(index, unique_paid_index).value)
				promotion_ratio['watch_time'].append(self.main_sheet.cell(index, total_unpaid_index).value / self.main_sheet.cell(index, total_paid_index).value)
				promotion_ratio['reach'].append(self.main_sheet.cell(index,10).value / self.main_sheet.cell(index,8).value)
		return promotion_ratio


def main():
	tmp = LACDA_Core()
	
	print(tmp.get_audience_ratio('https://www.facebook.com/lokvietnam/posts/1908312159381431:0'))
	print(tmp.get_average_duration('https://www.facebook.com/lokvietnam/videos/1911244905754823/'))
	print(tmp.get_duration_ratio('https://www.facebook.com/lokvietnam/videos/1911244905754823/'))
	print(tmp.get_like("https://www.facebook.com/lokvietnam/videos/1911244905754823/"))
	print(tmp.get_promotion_ratio('https://www.facebook.com/lokvietnam/videos/1911244905754823/'))

main()
