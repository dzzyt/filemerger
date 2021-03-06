# -*- coding: utf-8 -*-

import pandas as pd

#functions

def create_spreadsheet_entry(
	article_id,
	token,
	index,
	tag,
	dep,
	g1,
	g2,
	g3
	):
#enters data into csv entry (row) format preprocessor
	result = [[
		article_id,
		token,
		index,
		tag,
		dep,
		g1,
		g2,
		g3
		]]
	return pd.DataFrame(result, columns=list(columns))

def put_values_in_spreadsheet(entry_list, data_frame):
	data_frame = data_frame.append(
		create_spreadsheet_entry( 
		entry_list[0], 
		entry_list[1],
		entry_list[2],
		entry_list[3],
		entry_list[4],
		entry_list[5],
		entry_list[6],
		entry_list[7]
		),ignore_index=True)
	return data_frame

def new_row_write(i,row_offset,data_frame):
	new_row=[
	new_file.iloc[i+row_offset,1],
	new_file.iloc[i+row_offset,2],
	new_file.iloc[i+row_offset,3],
	new_file.iloc[i+row_offset,4],
	new_file.iloc[i+row_offset,5]
	]
	new_row.append(
	data_df.iloc[i,6])
	new_row.append(
	data_df.iloc[i,7])
	new_row.append(
	data_df.iloc[i,8])

	return put_values_in_spreadsheet(new_row, data_frame)


#####################################################################3
#main recursive
def matcher(matches,shift,row_offset,tok_data,tok_new,i):
	if matches == 3:
		return row_offset, new_row_write(i,row_offset,data_frame)
	elif shift == 3:
		row_offset +=1
		shift = 0
		matches = 0
		tok_data = data_df.iloc[i,2].split(' ')
		tok_new = new_file.iloc[i+row_offset,2].split(' ')
		matcher(matches,shift,row_offset,tok_data,tok_new,i)
		
	elif tok_data[matches] == tok_new[matches+shift]:
		matches +=1
		matcher(matches,shift,row_offset,tok_data,tok_new,i)
	elif tok_data[matches] != tok_new[matches+shift]:
		shift += 1
		matcher(matches,shift,row_offset,tok_data,tok_new,i)

################################################################3
#variables
columns = [
	'Article',
	'Token',
	'index',
	'TAG',
	'Dependency@connection',
	'Group1',
	'Group2',
	'Group3'
]
data_frame = pd.DataFrame(columns = list(columns))
row_offset = 0
has_data = 'file_with_data.tsv'
#shorter
data_df = pd.read_csv(has_data, sep = '\t')
new_data = 'file_to_merge.tsv'
#longer
new_file = pd.read_csv(new_data, sep = '\t')

######################################################################################
#output run

#iloc is dataframe interger read by [row,column]
for i in range(len(data_df)):
	shift =0
	tok_data = data_df.iloc[i,2].split(' ')
	tok_new = new_file.iloc[i+row_offset,2].split(' ')
	matches = 0
	row_offset, data_frame = matcher(matches,shift,row_offset,tok_data,tok_new,i)

data_frame.to_csv('merged.tsv',sep='\t')
