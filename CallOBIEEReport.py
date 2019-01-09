from suds.client import Client

cl = Client('https://dev1-abbinav.analytics.ocp.oraclecloud.com/analytics-ws/saw.dll/wsdl/v7')

# Logon
#print(cl)
sessionid = cl.service['SAWSessionService'].logon('sristiraj.b@gmail.com', 'gOOgle@2340178')
print(sessionid)
sa_list = cl.service['MetadataService'].getSubjectAreas(sessionid)
print(sa_list)
for sa in sa_list:
    print(sa.name)

sa_description=cl.service['MetadataService'].describeSubjectArea(sa_list[0].name,'IncludeTablesAndColumns',sessionid)
#
for table in sa_description.tables:
    print(table.name)
for col in table.columns:
    print(col.name)
#
# # ----------------------
# # Reference
# # Print all methods and services
print(str(cl))
