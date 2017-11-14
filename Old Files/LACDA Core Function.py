class LACDA_Core:
	import xlrd
	file = xlrd.open_workbook("Facebook Insights Data Export (Post Level) - LOK - 2017-07-27.xlsx")
	main_sheet = file.sheet["Key Metric"]
	minor_sheet = file.sheet["Lifetime Talking About This(..."]
	data_col = {}

	data_entry = ["Post ID", "Permalink", "Type", "Posted", "post_impressions_unique:lifetime", "post_impressions_paid_unique:lifetime", "post_engaged_users:lifetime", "post_video_complete_views_organic_unique:lifetime", "post_video_complete_views_organic:lifetime", "post_video_complete_views_paid_unique:lifetime", "post_video_complete_views_paid:lifetime", "post_video_views_organic_unique:lifetime", "post_video_views_organic:lifetime", "post_video_views_paid_unique:lifetime", "post_video_views_paid:lifetime", "post_video_avg_time_watched:lifetime", "post_video_length:lifetime", "Content", "share", "like", "comment"]

	def get_data()
		for i in range(0, len(data_entry))
			if data_entry[i] == "share" or data_entry[i] == "like" or data_entry[i] == "comment"
				data_col[data_entry[i]] = get_col_index(data_entry[i], minor_sheet)
			else
				data_col[data_entry[i]] = get_col_index(data_entry[i], main_sheet)


	#get column index
	def get_col_index(colname, sheetname)
		for colindex in range(0, sheetname.ncols)
			if sheetname.cell(0, colindex).value == colname
				return colindex

	print (data_col)
		

