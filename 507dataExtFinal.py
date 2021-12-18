#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 18:09:21 2021

@author: coreywiley
"""

import pandas as pd
import pandas_profiling 
from pandas_profiling import ProfileReport
import sweetviz as sv
import dtale
from janitor import clean_names, remove_empty
import time

### CSV Files

df_hospital = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/hospital_info.csv")
df_inpatient = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/inpatient_2015.csv")
df_outpatient = pd.read_csv("https://raw.githubusercontent.com/hantswilliams/AHI_DataSci_507/main/Deployment_Streamlit/outpatient_2015.csv")

### Length of each dataframe
print('HospitalLength: ', len(df_hospital)) - #5314 rows[Each is unique hospital]
print('OutpatientLength: ', len(df_outpatient)) - #32532 rows[Each row represents an APC code for outpatient locations]
print('InpatientLength: ', len(df_inpatient)) - #201876 rows[Each row is a unique DRG code for inpatient locations]

### Profile Report for hospital
profile_hospital = ProfileReport(df_hospital, minimal=True)
profile.to_file("output.html")
profile_hospital
list(df_hospital)

### Clean hospital data
clean_hospital = pd.DataFrame.from_dict(df_hospital)
clean_hospital = clean_names(df_hospital)
clean_hospital = remove_empty(df_hospital)
clean_hospital.isnull().sum()

### Profile Report for inpatient
profile_inpatient = ProfileReport(df_inpatient, minimal=True)
profile.to_file("output.html")
profile_inpatient
list(df_inpatient)

### Clean inpatient data
clean_inpatient = pd.DataFrame.from_dict(df_inpatient)
clean_inpatient = clean_names(df_inpatient)
clean_inpatient = remove_empty(df_inpatient)
clean_inpatient.isnull().sum()

### Profile report for outpatient
profile_outpatient = ProfileReport(df_hospital, minimal=True)
profile.to_file("output.html")
profile_outpatient
list(df_outpatient)

### Clean outpatient data
clean_outpatient = pd.DataFrame.from_dict(df_outpatient)
clean_outpatient = clean_names(df_outpatient)
clean_outpatient = remove_empty(df_outpatient)
clean_outpatient.isnull().sum()
 
### Samples of all 3 clean dataframes
clean_hospital.sample(20)
clean_inpatient.sample(20)
clean_outpatient.sample(20)                     

### Convert 'provider_id' to string for all 3 clean dataframes
clean_hospital['provider_id'] = clean_hospital['provider_id'].astype(str)
clean_inpatient['provider_id'] = clean_inpatient['provider_id'].astype(str)
clean_outpatient['provider_id'] = clean_outpatient['provider_id'].astype(str)

### Merge hospital/inpatient clean dataframes
in_merge = clean_inpatient.merge(clean_hospital, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
in_merge.sample(20)

### Merge hospital/outpatient clean dataframes
out_merge = clean_outpatient.merge(clean_hospital, how = 'left', left_on = 'provider_id', right_on = 'provider_id')
out_merge.sample(20)

### Stonybrook only df with hospital/inpatient merge
sb_in_merge = in_merge[in_merge['provider_id'] == '330393']
sb_in_merge.sample(20)

### Stonybrook only df with hospital/outpatient merge
sb_out_merge = out_merge[out_merge['provider_id'] == '330393']
sb_out_merge.sample(20)

### NYS only df with hospital/inpatient merge
ny_in_merge = in_merge[in_merge['state'] == 'NY']
ny_in_merge.sample(20)

### NYS only df with hospital/outpatient merge
ny_out_merge = out_merge[out_merge['state'] == 'NY']
ny_out_merge.sample(20)

### General Stonybrook Info
sbinfo = clean_hospital[clean_hospital['hospital_name'] == 'SUNY/STONY BROOK UNIVERSITY HOSPITAL']]
sbinfo
# provider_id - 330393
# hospital type - Acute Care Hospitals
# hospital_ownership - Government - State
# hospital_overall_rating - 4
# mortality_national_comparison - Above national average
# safety_of_care_national_comparison - Above national average
# readmission_national_comparison - Below national average
# patient_experience_national_comparison - Below national average
# effectiveness_of_care_national_comparison - Same as national average
# timeliness_of_care_national_comparison - Below national average
# efficient_use_of_medical_imaging_national_comparison - Same as national average

### NYS Hospital 
ny_hosp = clean_hospital[clean_hospital['state'] == 'NY']
ny_hosp.sample(20)

### NYS Inpatient
ny_inp = clean_inpatient[clean_inpatient['provider_state'] == 'NY']
NY_inp.sample(20)

### NYS Outpatient
ny_outp = clean_outpatient[clean_outpatient['provider_state'] == 'NY']
ny_outp.sample(20)



