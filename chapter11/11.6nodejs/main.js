// import CryptoJS from "./crypto-js.min.js";
const  CryptoJS =require("./crypto-js.min.js")
// npm install express 
const express = require("express")
const app = express()
const port = 3000
app.use(express.json())


function getToken(player) {
    let key = CryptoJS.enc.Utf8.parse("fipFfVsZsTda94hJNKJfLoaqyqMZFFimwLt");
    const { name, birthday, height, weight } = player;
    let base64Name = CryptoJS.enc.Base64.stringify(CryptoJS.enc.Utf8.parse(name));
    let encrypted = CryptoJS.DES.encrypt(
      `${base64Name}${birthday}${height}${weight}`,
      key,
      {
        mode: CryptoJS.mode.ECB,
        padding: CryptoJS.pad.Pkcs7,
      }
    );
    return encrypted.toString();
  }
app.post("/",(req,res)=>{
    const data =req.body
    res.send(getToken(data))
})
app.post("/",(req,res)=>{
    const data =req.body
    console.log(req.body)
    res.send(getToken(data))
})
app.listen(port,()=>{
    console.log(`listening on port ${port}`)
})
const player  = {
    'name': '凯文-杜兰特',
    'image': 'durant.png',
    'birthday': '1988-09-29',
    'height': '208cm',
    'weight': '108.9KG'
}
console.log(getToken(player))
