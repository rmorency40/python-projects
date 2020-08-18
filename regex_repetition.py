#!/usr/bin/env python

import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search('The Adventure of Batman')
print(mo.group())

print('**' * 20)
mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())

print('++' * 20)
mo = batRegex.search('The Adventure of Batwoman')
print(mo.group())

print('*=' * 30)

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 111-222-4444. Call me tomorrow')
print(mo.group())


# phone number  with no area code - regex with ? mean zero or one

print('*=*' * 20)
phoneRegex = re.compile(r'(\d\d\d)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search( 'My phone number is 111-222-4444. Call me tomorrow')
print(mo.group())


# Using * in regexex zero or more 

print('*=' * 28)

batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search('The adventure of Batman')
print(mo.group())

print('*=*' * 25)
mo = batRegex.search('The Adventure of Batwowowowowowowoman')
print(mo.group())


# Using + in regexex one  or more
print('"' * 60)
print('Match one or more')
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search('The adventure of Batwoman')
print(mo.group())
mo = batRegex.search('The Adventure of Batwowowowowowowoman')
print(mo.group())
# Other regex

print('PPP' * 25)
regex = re.compile(r'\+\*\?')
mo = regex.search('I learned about +*? regex syntax')
print(mo.group())


print('POP' * 25)
regex = re.compile(r'(\+\*\?)+')
mo = regex.search('I learned about +*?+*?+*?+*? regex syntax')
print(mo.group())


# Regex - exact match a numeber of times
print('PIP' * 25)
haRegex = re.compile(r'(Ha){3}')
mo =  haRegex.search('He said "HaHaHa"')
print(mo.group())

# Looking for 3 phone numbers in  a row
print('PAP' * 25)
phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('Ny numbers are 234-111-3333,777-444-5555,888-999-1010')
print(mo.group())

# Greedy and non greedy regexes

print('*&' * 30)

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# Other
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo3 = phoneNumRegex.findall('Dell: 555-123-4444 work: 555-543-9898')
print(mo3)

print('BLA' * 20)

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo4 = phoneRegex.findall('Dell: 555-123-4444 work: 555-543-9898')
print(mo4)

print('newRegexex' * 7)

digitRegex =re.compile(r'(\d){3,5}')
mo6 = digitRegex.search('1234567890')
print(mo6.group())



# New regexes

print('Regex_with_findall_method' * 4)
phoneRgex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
phonemessage = '''###################################################################################################
AUTHOR:  AOTA team

CR/Fix date: Aug 28, 2018
Title: CR55 and DOV-146/AOTAS-332 QFix patch
Customer: Verizon

Delivery contents:
	app/rum-api.jar

	app/rum.ear/Activation-Core.jar
	app/rum.ear/HttpWorkflow-Core.jar
	app/rum.ear/Polling-Core.jar
	app/rum.ear/APP-INF/lib/ConfManager-Api.jar
	app/rum.ear/APP-INF/lib/Polling-Api.jar

	History/CR55_AOTAS-332_for_DOV-146.txt


Details: This patch contains the changes for CR55 and the QFix delivery for DOV-146/AOTAS-332  

### Installation procedure: ###

1. Stop all managed servers

2. Save a backup of the following files: 

	${domain_root}/${domain_name}/servers/AdminServer/upload/rum.ear/${specification_version}@${implementation_version}/app/rum.ear
	${domain_root}/${domain_name}/servers/AdminServer/upload/rum-api.jar/${specification_version}@${implementation_version}/app/rum-api.jar

3a. Copy the jars from rum.ear directory for the patch to the corresponding same directory inside the rum.ear to be patched.

3b. Copy the rum-api.jar to the corresponding same directory of the rum-api.jar to be patched

4. Remove all managed server folders by performing the following command (please replace the placeholders with correct values) on each weblogic node.

   cd ${domain_root}/${domain_name}/servers && rm -rf managed*   

5. Copy History/CR55_AOTAS-332_for_DOV-146.txt file to ${domain_root}/${domain_name}/History directory
890-123-5678
6. Execute the SQL for 

       insert into OAPS_PARAMETERS (N_ID,C_PRODUCT_TYPE,C_GROUP_NAME,C_PARAM_NAME,C_PARAM_NAME_SUFFIX,C_PARAM_VALUE,C_PARAM_DEFAULT,N_CATEGORY,N_PARAMETER_TYPE,C_DESCRIPTION,N_SCOPE_MIN_VALUE,N_SCOPE_MAX_VALUE,C_SCOPE_LIST,N_ACCESS_TYPE,N_BUSINESS_CONTEXT_ID,D_TIMESTAMP) values (SEQ_OAPS_PARAMETER.nextval,'RUM','configuration','device.tracking.filter.rule','System','(^[0-9]{8})000000([0-9]*$)|[0-9]*[a-zA-Z]+[0-9a-zA-Z]*|^106800000000$','',1,7,'imei tracking filtering rule (regexp)',null,null,null,2,null,CURRENT_TIMESTAMP);

7. Start all managed servers.

766-098-1234
### Rollback procedure: ###

1. Stop managed servers

2a. Replace the rum.ear file in the following directory
    ${domain_root}/${domain_name}/servers/AdminServer/upload/rum.ear/${specification_version}@${implementation_version}/app/ 
    with the rum.ear file from your backup directory.

2b. Replace the rum-api.jar file in the following directory
    ${domain_root}/${domain_name}/servers/AdminServer/upload/rum-api.jar/${specification_version}@${implementation_version}/app/ 
    with the rum-api.jar file from your backup directory.

3. Remove all manageds by performing the following command (please replace the placeholders with correct values) on each weblogic node

   cd ${domain_root}/${domain_name}/servers && rm -rf managed* 
 
4. Remove CR55_AOTAS-332_for_DOV-146.txt file from ${domain_root}/${domain_name}/History directory

5. Execute the following SQL

	delete from OAPS_PARAMETERS where C_PARAM_NAME = 'device.tracking.filter.rule';

6. Start all managed servers.

512-588-0964

###################################################################################################
'''
print(phoneRegex.findall(phonemessage))
