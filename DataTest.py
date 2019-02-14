# iUrl = "api/noncore/v1/student/$studentid/pcSelfDetectionProcessInfo/$oppoid"
# extract = {"studentid": 11, "oppoid": 2}
# if "$" in iUrl:
# 	iUrl = 'api/noncore/v1/student/$oppoid/pcSelfDetectionProcessInfo/$studentid'
# 	for k in extract.keys():
# 		niubilityExtract=iUrl.replace("$"+k,str(extract[k]))
# 		iUrl=niubilityExtract
# print(iUrl)
# print(type(iUrl))
#




a={"a":1,"b":2}

print(a.get("c","d"))

