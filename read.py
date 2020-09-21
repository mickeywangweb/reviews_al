# 測試印出 data 資料
#只印出第 0 筆看看
#讀取檔案的過程中,印出 len(data) 才知道讀取進度
#建立版本上傳 Github
#算留言平均長度
#建立版本上傳 Github

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 
		if count % 1000 == 0:
			print(len(data))
print(len(data))
print(data[0])
print('------------------')
print(data[1])