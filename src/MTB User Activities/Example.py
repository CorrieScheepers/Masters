def GetCalendarDateQuery(calendarName, beginDate, endDate):
	"""
	Function to construct SQL query for calendar
	:param calendarName: The calendar name to fetch
	:param beginDate: from which date to retrieve
	:param endDate: until which date to retrieve
	"""
	beginDate = beginDate.strftime("%Y-%m-%d")
	endDate = endDate.strftime("%Y-%m-%d")
	return  """ SELECT c_pd_CalendarMonth AS 'EskomCalendarMonth', c_pd_StartDate AS 'StartDate', c_pd_EndDate AS 'EndDate'
						  FROM Calendar_PeriodData WHERE fk_c_ID IN (SELECT c_ID  FROM Calendar WHERE c_Description = '"""+ calendarName +"""') AND
							( 
								(DATE('"""+beginDate+"""') >= c_pd_StartDate AND DATE('"""+beginDate+"""') <= c_pd_EndDate) OR
								(DATE('"""+beginDate+"""') <= c_pd_StartDate AND (DATE('"""+endDate+"""') >= c_pd_StartDate OR DATE('"""+endDate+"""') >= c_pd_EndDate))
							) ORDER BY c_pd_StartDate """
def GetEskomBillingCalendar(ids, db, startDate, calendarName):
	"""
	Function to query MTB SQL table for Eskom Billing Calendar
	:param ids: The list of Tag IDs to query (as ObjectId entries)
	:param db: The group database to query
	:param startDate: From which date to retrieve
	:param calendarName: The calendar name to fetch
	"""
	endDate = GetLatestDate(ids, db)
	mydb = mysql.connector.connect(host=MTBDatase["Host"],user=MTBDatase["User"],password=MTBDatase["Password"],database=MTBDatase["DB"])
	query = GetCalendarDateQuery(calendarName, startDate, endDate)
	return pd.read_sql(query, con=mydb)