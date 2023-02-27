import streamlit as st
import pandas as pd
import numpy as np
import joblib

def predict():
        prediction = clf.predict(X)[0]
        if(prediction == 0):
            return('Instance reported is Not Fraud')
        else:
            return('Instance reported is Fraud')

#Create UI

st.title('Insurance Claims Fraud Detection')

#INPUTS
months_as_customer = st.number_input("Months As Customer")

policy_number = st.number_input("Policy Number")

policy_state = st.selectbox("Policy State (Select 0 for OH, 1 for IN, 2 for IL)",('0','1','2'))

policy_csl = st.selectbox("Policy csl (Select 0 for 250/500, 1 for 100/300, 2 for 500/1000)",('0','1','2'))

policy_deductable = st.text_input('Policy Deductable')

policy_annual_premium = st.text_input('Policy Annual Premium')

umbrella_limit = st.text_input('Umbrealla Limit')

insured_zip = st.text_input('Insured Zip')

insured_sex = st.selectbox("Insured Sex (Select 0 for Female and 1 for Male )" , ('0','1'))

insured_education_level = st.selectbox("Insured Education Level (Select 0 for High School, 1 for College, 2 for Masters, 3 for JD, 4 for MD, 5 for Associate, 6 for PhD)",('0','1','2','3','4','5','6'))

insured_occupation = st.selectbox("Insured Occupation (Select 0 for farming-fishing,1 for handlers-cleaners,2 for protective-serv,3 for adm-clerical,4 for armed-forces,5 for priv-house-serv,6 for other-service,7 for transport-moving,8 for craft-repair,9 for exec-managerial,10 for sales,11 for tech-support,12 for prof-specialty,13 for machine-op-inspct)",
                                  ('0','1','2','3','4','5','6','7','8','9','10','11','12','13'))

insured_hobbies = st.selectbox("Insured Hobbies (Select 0 for basketball, 1 for cross-fit, 2 for sleeping, 3 for dancing, 4 for chess, 5 for polo, 6 for board-games, 7 for base-jumping, 8 for skydiving, 9 for video-games, 10 for hiking, 11 for yachting, 12 for kayaking, 13 for camping, 14 for golf, 15 for movies, 16 for bungie-jumping, 17 for paint-ball, 18 for exercise , 19 for reading)",
                               ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19'))

insured_relationship = st.selectbox("Insured Relationship (Select 0 for unmarried,1 for wife,2 for husband,3 for not-in-family,4 for other-relative,5 for own-child)",
                                    ('0','1','2','3','4','5'))

capital_gains = st.text_input('Capital - Gains')

capital_loss = st.text_input('Capital - Loss')

collision_type = st.selectbox("Collision Type (Select 0 for Front-Collision, 1 for Side-Collision, 2 for Rear-Collision)",('0','1','2'))

incident_severity = st.selectbox('Incident Severity (Select 0 for Trivial Damage, 1 for Major Damage, 2 for Total Loss, 3 for Minor Damage)',("0","1","2"))

authorities_contacted = st.selectbox('Authorities Contacted (Select 0 for None, 1 for Ambulance, 2 for Other, 3 for Fire, 4 for Police)',("0","1","2","3","4"))

incident_state = st.selectbox("Incident State (Select 0 for OH, 1 for PA, 2 for NC, 3 for VA, 4 for WV, 5 for SC, 6 for NY)",('0','1','2','3','4','5','6'))

incident_city = st.selectbox("Incident City (Select 0 for Northbrook, 1 for Riverwood, 2 for Hillsdale, 3 for Northbend, 4 for Columbus,5 for Arlington, 6 for Springfield)",('0','1','2','3','4','5','6'))

incident_hour_of_the_day = st.text_input("Incident Hour of the day")

property_damage = st.selectbox("Property Damage (Select 0 for NO, 1 for YES)",('0','1'))

bodily_injuries = st.text_input('Bodily Injuries')

witnesses = st.text_input('Witnesses')

police_report_available = st.selectbox('Police Report Available (Select 0 for NO and 1 for YES)',("0","1"))

auto_make = st.selectbox("Auto Make (Select 0 for Honda , 1 for Mercedes , 2 for Jeep, 3 for Volkswagen, 4 for Accura, 5 for Audi,6 for Toyota, 7 for BMW, 8 for Ford , 9 for Chevrolet, 10 for Nissan, 11 for Suburu, 12 for Dodge, 13 for Saab)",
                         ('0','1','2','3','4','5','6','7','8','9','10','11','12','13'))

auto_model = st.selectbox("Auto Model(Select 0 for RSX, 1 for Accord, 2 for M5, 3 for X6, 4 for 3 Series, 5 for C300, 6 for CRV, 7 for TL,8 for Corolla, 9 for Impreza, 10 for ML350, 11 for Fusion, 12 for Silverado, 13 for Civic, 14 for Highlander, 15 for X5, 16 for Ultima, 17 for Maxima, 18 for Tahoe, 19 for Escape, 20 for Grand Cherokee, 21 for 93, 22 for E400, 23 for 95, 24 for F150, 25 for Forrestor, 26 for Camry, 27 for 92x, 28 for Malibu, 29 for Pathfinder, 30 for Legacy, 31 for A5, 32 for Passat,33 for Jetta, 34 for MDX, 35  for Neon,36 for A3,37 for Wrangler, 38 for RAM)",
                          ('0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38'))

auto_year = st.text_input("Auto Year")

policy_bind_Day = st.text_input('Policy Bind Day')

policy_bind_Month = st.text_input('Policy Bind Month')

policy_bind_Year = st.text_input('Policy Bind Year')

incident_Day = st.text_input('Incident Day')

incident_Month = st.text_input('Incident Month')

#Code after clicking the submit button
report = ''

if st.button("Submit") :

    clf = joblib.load('Insurance Claims- Fraud Detection.pkl')

    X = pd.DataFrame([[months_as_customer,policy_number,policy_state,policy_csl,policy_deductable,policy_annual_premium,umbrella_limit,insured_zip,
                       insured_sex,insured_education_level,insured_occupation,insured_hobbies,insured_relationship,capital_gains,capital_loss,
                       collision_type,incident_severity,authorities_contacted,incident_city,incident_state,incident_hour_of_the_day,
                       property_damage,bodily_injuries,witnesses,police_report_available,auto_make,auto_model,auto_year,
                       policy_bind_Day,policy_bind_Month,policy_bind_Year,incident_Day,incident_Month]],
                       
                       columns=['months_as_customer', 'policy_number', 'policy_state', 'policy_csl','policy_deductable', 'policy_annual_premium', 'umbrella_limit','insured_zip', 'insured_sex', 'insured_education_level',
                                'insured_occupation', 'insured_hobbies', 'insured_relationship','capital-gains', 'capital-loss', 'collision_type', 'incident_severity','authorities_contacted', 'incident_state', 'incident_city',
                                'incident_hour_of_the_day', 'property_damage', 'bodily_injuries','witnesses', 'police_report_available', 'auto_make', 'auto_model',
                                'auto_year', 'policy_bind_Day', 'policy_bind_Month', 'policy_bind_Year','incident_Day', 'incident_Month'])
   
    
    report = predict()


st.success(report)