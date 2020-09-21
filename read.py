#寫程式來讀取留言檔
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
print('檔案讀取完了，總共有', len(data), '筆資料')

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)

print('留言的平均長度為',sum_len/len(data))

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於 100')
print(new[0])
print(new[1])
