import csv

story_to_columns = {
	"s.no":{"pos": 0},
	"Issue key":{"pos": 1, "gen_pos": {"gcol_name": "STORY ID", "npos": 3}},
	"Issue id": {"pos": 2},
	"Custom field (Epic Link)": {"pos": 3, "gen_pos": {"gcol_name": "EPIC ID", "npos":1}},
	"Ename":{"pos": 4},
	"ESdate":{"pos":5, "gen_pos": {"gcol_name": "STORY\nPLANNED\nSTART", "npos": 7}},
	"ETdate":{"pos": 6, "gen_pos": {"gcol_name":"STORY\nPLANNED\nEND", "npos": 8}},
	"EASdate":{"pos": 7, "gen_pos": {"gcol_name":"STORY\nACTUAL\nSTART", "npos": 13}},
	"EAEdate":{"pos": 8,"gen_pos": {"gcol_name":"STORY\nACTUAL\nEND", "npos": 14}},
	"Assignee":{"pos":9, "gen_pos": {"gcol_name": "ASSIGNED TO", "npos": 5}},
	"progress":{"pos":10,"gen_pos": {"gcol_name":"STORY\nEffort\ncompletion\n%", "npos": 15}},
	"Custom field (Story Points)":{"pos":11, "gen_pos": {"gcol_name": "ESTIMATED\nSTORY\nPOINTS", "npos": 6}},
	"Original Estimate":{"pos":12,"gen_pos": {"gcol_name": "Time spent\n(IN Secs)", "npos": 10 }},
        "originalhours": {"pos": 13, "gen_pos": {"gcol_name": "EFFORT\nCONSUMED\n(IN HRS)", "npos": 11 }},
        "Time Spent": {"pos": 14},
        "spenthours": {"pos":15, "gen_pos": {"gcol_name": "ESTIMATED\nEFFORT\n(IN HRS))", "npos": 9}},
        "Remaining Estimate":{"pos":16},
        "remaininghours": {"pos": 17, "gen_pos": {"gcol_name": "PENDING\nEFFORT\n(IN HRS)", "npos":12}},
        "Sprint":{"pos":18, "gen_pos": {"gcol_name": "SPRINT ID", "npos": 2}},
        "Sprint2":{"pos":19},
        "Sprint3":{"pos":20},
        "Summary":{"pos": 21, "gen_pos": {"gcol_name": "STORY DESCRIPTION", "npos": 4}},
        "story_schedule_progress":{"gen_pos": {"gcol_name" : "STORY\nSchedule\nProgress % ","pos": 22}},
        "story_schedule_overrun":{"gen_pos": {"gcol_name": "STORY\nSchedule\nOverrun %", "pos": 23}}
}
epics_to_columns = {
	"s.no": {"pos":0},
	"Custom field (Epic Link)": {"pos": 1},
	"Ename": {"pos": 2},
	"ESdate": {"pos":3},
	"ETdate":{"pos":4},
	"EASDate": {"pos":5},
	"EAEDate": {"pos": 6}
}
def get_s_no_pos():
    return story_to_columns["s.no"]["pos"]

def get_issue_key_pos():
    return story_to_columns["Issue key"]["pos"]

def get_issue_id_pos():
    return story_to_columns["Issue id"]["pos"]

def get_custom_field_link_pos():
    return story_to_columns["Custom field (Epic Link)"]["pos"]
def get_ename_pos():
    return story_to_columns["Ename"]["pos"]
def get_esdate_pos():
    return story_to_columns["ESdate"]["pos"]
def get_etdate_pos():
    return story_to_columns["ETdate"]["pos"]
def get_easdate_pos():
    return story_to_columns["EASdate"]["pos"]
def get_eaedate_pos():
    return story_to_columns["EAEdate"]["pos"]

def get_assignee_pos():
    return story_to_columns["Assignee"]["pos"]
def get_progress_pos():
    return story_to_columns["progress"]["pos"]
def get_custom_field_points_pos():
    return story_to_columns["Custom field (Story Points)"]["pos"]

def get_orig_esti_pos():
    return story_to_columns["Original Estimate"]["pos"]

def get_originalhours_pos():
    return story_to_columns["originalhours"]["pos"]
def get_time_spent_pos():
    return story_to_columns["Time Spent"]["pos"]

def get_spenthours_pos():
    return story_to_columns["spenthours"]["pos"]
def get_rem_esti_pos():
    return story_to_columns["Remaining Estimate"]["pos"]

def get_remaininghours_pos():
    return story_to_columns["remaininghours"]["pos"]
def get_sprint_pos():
    return story_to_columns["Sprint"]["pos"]

def get_sprint2_pos():
   return story_to_columns["Sprint2"]["pos"]

def get_sprint3_pos():
    return story_to_columns["Sprint3"]["pos"]
	
def get_summary_pos():
    return story_to_columns["Summary"]["pos"]
	

def get_sno_pos():
    return epics_to_columns["s.no"]["pos"]
def get_epic_custom_field_link():
    return epics_to_columns["Custom field (Epic Link)"]["pos"]
def get_epic_ename():
    return epics_to_columns["Ename"]["pos"]
def get_epic_esdate():
    return epics_to_columns["ESdate"]["pos"]
def get_epic_etdate():
    return epics_to_columns["ETdate"]["pos"]
def get_epic_easDate():
    return epics_to_columns["EASDate"]["pos"]
def get_epic_eaedate():
    return epics_to_columns["EAEDate"]["pos"]
	
def get_epic_id_col():
    return story_to_columns["Custom field (Epic Link)"]["gen_pos"]["gcol_name"]
def get_epic_id_npos():
    return story_to_columns["Custom field (Epic Link)"]["gen_pos"]["npos"]
def get_story_id_col():
    return story_to_columns["Issue key"]["gen_pos"]["gcol_name"]
def get_story_id_npos():
    return story_to_columns["Issue key"]["gen_pos"]["npos"]
def get_sprint_id_col():
    return story_to_columns["Sprint"]["gen_pos"]["gcol_name"]
def get_sprint_id_npos():
    return story_to_columns["Sprint"]["gen_pos"]["npos"]
def get_story_desc_col():
    return story_to_columns["Summary"]["gen_pos"]["gcol_name"]
def get_story_desc_npos():
    return story_to_columns["Summary"]["gen_pos"]["npos"]
def get_assigned_to_col():
    return story_to_columns["Assignee"]["gen_pos"]["gcol_name"]
def get_assigned_to_npos():
    return story_to_columns["Assignee"]["gen_pos"]["npos"]
def get_esti_story_points_col():
    return story_to_columns["Custom field (Story Points)"]["gen_pos"]["gcol_name"]
def get_esti_story_points_npos():
    return story_to_columns["Custom field (Story Points)"]["gen_pos"]["npos"]
def get_story_planned_start_col():
    return story_to_columns["ESdate"]["gen_pos"]["gcol_name"]
def get_story_planned_start_npos():
    return story_to_columns["ESdate"]["gen_pos"]["npos"]
def get_story_planned_end_col():
    return story_to_columns["ETdate"]["gen_pos"]["gcol_name"]
def get_story_planned_end_npos():
    return story_to_columns["ETdate"]["gen_pos"]["npos"]
def get_esti_effort_in_hrs_col():
    return story_to_columns["spenthours"]["gen_pos"]["gcol_name"]
def get_esti_effort_in_hrs_npos():
    return story_to_columns["spenthours"]["gen_pos"]["npos"]
def get_time_spent_in_sec_col():
    return story_to_columns["Original Estimate"]["gen_pos"]["gcol_name"]
def get_time_spent_in_sec_npos():
    return story_to_columns["Original Estimate"]["gen_pos"]["npos"]

def get_effort_cons_in_hrs_col():
    return story_to_columns["originalhours"]["gen_pos"]["gcol_name"]
def get_effort_cons_in_hrs_npos():
    return story_to_columns["originalhours"]["gen_pos"]["npos"]
def get_pending_effort_in_hrs_col():
    return story_to_columns["remaininghours"]["gen_pos"]["gcol_name"]
def get_pending_effort_in_hrs_npos():
    return story_to_columns["remaininghours"]["gen_pos"]["npos"]
def get_story_actual_start_col():
    return story_to_columns["EASdate"]["gen_pos"]["gcol_name"]
def get_story_actual_start_npos():
    return story_to_columns["EASdate"]["gen_pos"]["npos"]
def get_story_actual_end_col():
    return story_to_columns["EAEdate"]["gen_pos"]["gcol_name"]
def get_story_actual_end_npos():
    return story_to_columns["EAEdate"]["gen_pos"]["npos"]
def get_story_effort_comp_col():
    return story_to_columns["progress"]["gen_pos"]["gcol_name"]
def get_story_effort_comp_npos():
    return story_to_columns["progress"]["gen_pos"]["npos"]
def get_story_schedule_progress_col():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["gcol_name"]
def get_story_schedule_progress_npos():
    return story_to_columns["story_schedule_progress"]["gen_pos"]["pos"]
def get_story_schedule_overrun_col():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["gcol_name"]
def get_story_schedule_overrun_npos():
    return story_to_columns["story_schedule_overrun"]["gen_pos"]["pos"]

	
	
def open_file_by_name(filename):
    data_list = []

    fd = open(filename, "rt")
    fdata = csv.reader(fd)

    for row in fdata:
        data_list.append(row)

    fd.close()
    return data_list
	
def get_sort_sprint(data):
    

    for i in range(1, len(data)):
        s1 = data[i][s1_pos]
        s2 = data[i][s2_pos]
        s3 = data[i][s3_pos]

        t = [s1, s2, s3]
        t.sort(reverse = True)
        data[i][s1_pos] = s1
        data[i][s2_pos] = s2
        data[i][s3_pos] = s3
    
    return data


def get_colnames_with_pos(data):
    
    datalist = []
    data[0][cfl_pos] = ei_col
    data[0][ik_pos] = si_col
    data[0][s1_pos] = sprint_id_col
    data[0][s_pos] = sd_col
    data[0][a_pos] = at_col
    data[0][cfp_pos] = esp_col
    data[0][es_pos] = sps_col
    data[0][et_pos] = spe_col
    data[0][sh_pos] = ee_in_hrs_col
    data[0][oe_pos] = ts_in_sec_col
    data[0][oh_pos] = ec_in_hrs_col
    data[0][rh_pos] = pe_in_hrs_col
    data[0][eas_pos] = sas_col
    data[0][eae_pos] = sae_col
    data[0][p_pos] = sec_col
    data[0].insert(ssp_npos, ssp_col)
    data[0].insert(sso_npos, sso_col)
    for j in range (1, len(data)):
        data[j].insert(ssp_npos, "100%")
        data[j].insert(sso_npos, "0%")
    for j in range(0, 23):
        print(j, data[0][j])

    for i in range(0, len(data)):
        list = [data[i][sno_pos],data[i][cfl_pos], data[i][s1_pos], data[i][ik_pos], data[i][s_pos], data[i][a_pos], data[i][cfp_pos], data[i][es_pos], 
                data[i][et_pos], data[i][oh_pos], data[i][oe_pos], data[i][oh_pos], data[i][rh_pos], data[i][eas_pos],
                data[i][eae_pos], data[i][p_pos], data[i][ssp_npos], data[i][sso_npos]]
        datalist.append(list)
    print(datalist)
    
		
		
		
    return datalist
sno_pos = get_s_no_pos()
ik_pos =get_issue_key_pos()
ii_pos = get_issue_id_pos()
cfl_pos = get_custom_field_link_pos()
en_pos = get_ename_pos()
a_pos = get_assignee_pos()
oe_pos = get_orig_esti_pos() 
p_pos = get_progress_pos()
cfp_pos = get_custom_field_points_pos()
sh_pos = get_spenthours_pos()
re_pos = get_rem_esti_pos()
es_pos = get_esdate_pos()
et_pos = get_etdate_pos()
eas_pos = get_easdate_pos() 
eae_pos = get_eaedate_pos()
oh_pos = get_originalhours_pos()
rh_pos = get_remaininghours_pos()
ts_pos = get_time_spent_pos()
s1_pos = get_sprint_pos()
s2_pos = get_sprint2_pos()
s3_pos = get_sprint3_pos()
s_pos = get_summary_pos()
ei_col = get_epic_id_col()
ei_npos = get_epic_id_npos()
si_col = get_story_id_col()
si_npos = get_story_id_npos()
sprint_id_col = get_sprint_id_col()
sprint_id_npos = get_sprint_id_npos()
sd_col = get_story_desc_col()
sd_npos = get_story_desc_npos()
at_col = get_assigned_to_col()
at_npos = get_assigned_to_npos()
esp_col = get_esti_story_points_col()
esp_npos = get_esti_story_points_npos()
sps_col = get_story_planned_start_col()
sps_npos = get_story_planned_start_npos()
spe_col = get_story_planned_end_col()
spe_npos = get_story_planned_end_npos()
ee_in_hrs_col = get_esti_effort_in_hrs_col()
ee_in_hrs_npos = get_esti_effort_in_hrs_npos()
ec_in_hrs_col = get_effort_cons_in_hrs_col()
ec_in_hrs_npos = get_effort_cons_in_hrs_npos()
ts_in_sec_col = get_time_spent_in_sec_col()
ts_in_sec_npos = get_time_spent_in_sec_npos()
pe_in_hrs_col = get_pending_effort_in_hrs_col()
pe_in_hrs_npos = get_pending_effort_in_hrs_npos()
sas_col = get_story_actual_start_col()
sas_npos = get_story_actual_start_npos()
sae_col = get_story_actual_end_col()
sae_npos = get_story_actual_end_npos()
sec_col = get_story_effort_comp_col()
sec_npos = get_story_effort_comp_npos()
ssp_col = get_story_schedule_progress_col()
ssp_npos = get_story_schedule_progress_npos()
sso_col = get_story_schedule_overrun_col()
sso_npos = get_story_schedule_overrun_npos()
def main():
    filename = "gdata.csv"
    datalines = open_file_by_name(filename)
    sorted_file = get_sort_sprint(datalines)
    processed_file = get_colnames_with_pos(sorted_file)
    print(processed_file)

	
    with open("generated.csv", "w") as csv_file:
        gd = csv.writer(csv_file)
        for row in processed_file:
            gd.writerow(row)
if(__name__ == "__main__"):
    main()
