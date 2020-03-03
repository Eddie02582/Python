# Dataframe

## 建立dataframe
### array
```
arr = [["Math",85], ["Chemistry",90], ["Chinese",40],["physics",40],["English",60]]
df = pd.DataFrame(map, columns = ["subject", "scores"])# 指定欄標籤名稱  

```

Output df:
```
      subject  scores
0       Math      85
1  Chemistry      90
2    Chinese      40
3    physics      40
4    English      60
```


### dictionary
```
subject = ["Math", "Chemistry", "Chinese","physics","English"]  
scores = [85, 90, 40, 40, 60]  
map  = {"subject": subject,  
        "scores": scores
       }

df = pd.DataFrame(map)
```

Output df:
```
      subject  scores
0       Math      85
1  Chemistry      90
2    Chinese      40
3    physics      40
4    English      60
```
若使用col,則是選擇dict to df 的欄位
```
pd.DataFrame(map,columns = ["subject"])
```


Output
```
     subject
0       Math
1  Chemistry
2    Chinese
3    physics
4    English
```
### dictionary array








