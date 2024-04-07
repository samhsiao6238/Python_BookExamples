dic= {'Taipei':95, 'Tainan':94, 'Kaohsiung':96} #設定字典
print (dic)  #查看字典內容，會輸出{'Taipei': 95, 'Tainan': 94, 'Kaohsiung': 96}
dic['Taipei']  #取得字典中'Taipei'鍵的值，會輸出95
dic['Tainan']=93 #將字典中的「'Tainan'」鍵的值修改為93
print (dic) #會輸出修改後的字典 {Taipei': 95, 'Tainan': 93, 'Kaohsiung': 96}
dic['Ilan']= 87	#在字典中新增「'Ilan'」，該鍵所設定的值為87
dic #新增元素後的字典  {'Taipei': 95, 'Tainan': 93, 'Kaohsiung': 96, 'Ilan': 87}
print (dic)
