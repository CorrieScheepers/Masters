# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import mysql.connector as MySQL
import pandas as pd 
import numpy as np

#  deepcode ignore NoHardcodedPasswords: <comment the reason here>
lDatabase = MySQL.connect(host='localhost', user='root', password='Hvacint001', database='mtb_database')

# %%
# User Actvities
lQuery = "SELECT lma_ID, lma_Time, fk_d_ID, fk_u_ID, lma_ViewAsID, lma_File, lma_ActivityType FROM mtb_database.Log_MTBActivity;"
MTBUserActivities = pd.read_sql(lQuery, con=lDatabase)
MTBUserActivities["fk_d_ID"] = MTBUserActivities["fk_d_ID"].fillna(0).astype(int)
# %%
# User rights
lQuery = """SELECT id, firstname, surname, groupid, isDeleted, fk_ut_ID, 
			CASE WHEN fk_ur_ID = 59 THEN TRUE ELSE FALSE END AS DeveloperRights
			FROM mtb_database.mt_Users left join
			mtb_database.mt_UserLINKRight UR ON id = UR.fk_u_ID AND fk_ur_ID = 59"""
Users = pd.read_sql(lQuery, con=lDatabase)

# Contract MTB Groups
lQuery = "SELECT id, description, is_admin_grp FROM mtb_database.mt_et_Systems_Group;"
ContractGroups = pd.read_sql(lQuery, con=lDatabase)

# ViewAsID links
lQuery = """SELECT DISTINCT(lma_ViewAsID), groupid FROM mtb_database.Log_MTBActivity Activity
    	    left join mtb_database.mt_Users Users ON Activity.lma_ViewAsID = Users.id"""
ViewAsIDLink = pd.read_sql(lQuery, con=lDatabase)
# %%
# Toolboxes
lQuery = "SELECT d_ID, d_Key, d_Name FROM mtb_database.mt_Dashboard;"
Dashboard = pd.read_sql(lQuery, con=lDatabase)
Dashboard = Dashboard.append(pd.DataFrame({"d_ID" : [0], "d_Key" : ["Undefined"], "d_Name" : ["Undefined"]}))

# Toolboxes
lQuery = "SELECT tb_ID, tb_Name, tb_DisplayName, tb_DisplayInMenu FROM mtb_database.mt_Toolbox;"
Toolboxes = pd.read_sql(lQuery, con=lDatabase)
Toolboxes = Toolboxes.append(pd.DataFrame({"tb_ID" : [0], "tb_Name" : "undefined", "tb_DisplayName": "Undefined", "tb_DisplayInMenu" : ["1"]}))

# Toolbox link
lQuery = "SELECT fk_tb_ID, fk_d_ID FROM mtb_database.mt_ToolboxLINKDashboard;"
DashboardLink = pd.read_sql(lQuery, con=lDatabase)
DashboardLink = DashboardLink.append(pd.DataFrame({"fk_tb_ID" : [0], "fk_d_ID": [0]}))

# Dashboard Link to Account
lQuery = "SELECT * FROM mtb_database.mt_UserLINK_Dashboard;"
UserLinkDashboard = pd.read_sql(lQuery, con=lDatabase)

# View Link
lQuery = "SELECT * FROM mtb_database.mt_View;"
Views = pd.read_sql(lQuery, con=lDatabase)

lQuery = "SELECT * FROM mtb_database.mt_ViewLINKDashboards;"
ViewLinkDashboard = pd.read_sql(lQuery, con=lDatabase)
