class LACDA_Core:
	import xlrd
	file = xlrd.open_workbook("Facebook Insights Data Export (Post Level) - LOK - 2017-07-27.xlsx")
	main_sheet = file.sheet["Key Metric"]
	minor_sheet = file.sheet["Lifetime Talking About This(..."]
	data_col = {}
	for sheet in file.sheets():
		nrows = sheet.nrows
		ncols = sheet.ncols
		for row in range(2, nrows):
			value = []
			for col in range(1, ncols):
				if col in [1,3,6,8,10,14,23,24,25,26,27,28,29,30,31,32]:
					value.append(sheet.cell(row, col).value)
					data[sheet.cell(row, 2).value] = value
	#data collector

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
		

