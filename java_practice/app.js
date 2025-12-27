// テスト ;で文の終わり ctrl/コメント化
//console.log("Hello World!");consoleはprintに近い動作確認
// foo bar サンプルコードでよく使われる baz, qux, foobar, hoge, huga, piyo
// コーテションはどちらでもいいが、一つのプロジェクトで片方しか使わない。
//const foo = 1 + 1;
//console.log(foo)
//console.log(1 + 1);
//変数　const 変数名　=　値
//const foo = 1;
//console.log(foo)

const colorDark = "#333"
if(new Date().getHours() >= 0){
    document.body.style.backgroundColor = colorDark;
}
//if(user.setting.darkMode === true){
//   document.body.style.backgroudColor = colorDark;
//}
//constは値の再代入ができない letは再代入可能
let foo = 1;
foo = 2;
console.log(foo);
//↑はエラーが起きない　とりあえずの場合constが推奨される
//forループのカウント変数はlet　
//予約語 const let などは変数名としてしようできない。
const result = 1 + 2;
console.log(result);

let myPokemon = "ピカチュウ";
myPokemon = "ニャオハ";
myPokemon = "ホゲータ";
console.log(myPokemon);

//データ型　
console.log("Hello + World!");//HelloWorld!
console.log("1" + "1");//11

//if(isLogin === True){
//
//}

//null あえて値がからであること明示したい場合
//undefined 意図してない？値が空
//typeofを使うとそれぞれの値が何型かわかる
console.log(typeof "ピカチュウ");
console.log(typeof 10);
console.log(typeof true);
console.log(typeof "null");

console.log("ピカチュウ" + "lv" + 10);
//↑ｊｓだとエラーにならないがほかのプログラミング言語上だと文字+数値はエラーになるためよい仕様ではない。


//配列　複数の値をまとめて並列に管理するまとまり
const foo1 = "bar1"
const array = [1, "Hello", foo1];

console.log(array[0]);//1


const firstPolemons = ["ニャオハ", "ホゲータ", "クワッス"];
//ホゲータを出力するには
console.log(firstPolemons[1]);

//ループ文
const questions =[
    "現在の日本の総理大臣の名前は？",
    "令和7年は西暦で言うと？",
    "最も人口の多い国はどこ？"
];

//let index = 0初期値　index < questions.length　←indexがquestionsの配列の長さよりも小さいことを示す。//question.lengthの値は３
// index++  ++は1を足すことを意味する --は1を引くことを意味する
for (let index = 0; index < questions.length; index++) {
console.log(questions[index]);
}
//console.log(questions[index])は配列questionsのindex番目の値をconsoleで表示するという意味

//条件文
//if(condition){
    //ここに処理を書く
//}
// if(!isLogin) !論理否定
let isLogin = true;
if(!isLogin ){
    alert("ログインしてください")
}else{
    console.log("ログイン成功中");
}
//if(isLogin === true)とif(islogin)は同じ意味になる
// === 等しい
// !== 等しくない
// &&　かつ
// if(foo2 > 0 && foo2 < 1000){

// }
// const userType = "menber"; //menber, admin, owner
// if(userType === "menber"){
//     //alert("アクセスできません");
// }else if(userType === "admin"){
//     alert("今から10分間だけアクセスできます");
// }else {
//     console.log("アクセス成功");
// }

//ex;mymoney500以上ならisShippingでtrueを返すようにしなさい
const myMoney = 1000;
let isShipping = false;
if(myMoney >= 500){

}
console.log(!isShipping);
//回答
//const myMoney = 1000;
//let isShipping = false;
//if(myMoney >= 500){
//  isShipping = true;
//}
//  console.log(isShipping);

//関数
// function 関数名(引数){
    //処理
// }

// const 関数名 =() =>{
    //処理
// }

//元のコード
// if (new Date().getHours() > 20){
//     document.body.style.backgroundColor = "#000";
// }

//関数化したコード
function changeDarkMode(time) {
    if (new Date().getHours() > time) {
        document.body.style.backgroundColor = color;
    }
}

// if (season === "winter"){
//     changeDarkMode(18);
// }  else  {
//     changeDarkMode(20);
// }
//changeDarkMode();
//関数化すれば↑でよびだせる関数+()

function changeDarkMode(time, color) {
    if (new Date().getHours() > time){
        document.body.style.backgroundColor = color;
    }
}

changeDarkMode(20, "#333");

function changeDarkMode(time = 20, color = "#333") {
    if (new Date().getHours() > time){
        document.body.style.backgroundColor = color;
    }
}

changeDarkMode();//time=20とcolor=#333のデフォルト値が適用される。
//引数はオブジェクト形式でも渡すことができる。

// function changeDarkMode(obj) {
//     if (new Date().getHours() > obj.time){
//         document.body.style.backgroundColor = obj.color;
//     }
// }

// changeDarkMode({
//     time: 20,
//     color: "#333"
// })
//objを使うと引数の順番を気にする必要がなくなり、可読性がよくなる。

//callback関数
function foo3(callback){
    console.log("Hi, Tom!");
    callback();
}

function bar2(){
    console.log("Hi, Ken!");
}

foo3(bar2);
//関数foo()の引数に関数barを渡している。関数barはcallback()の時点で実行される。

//戻り値
// function 関数名(){
//     //処理
//     return 戻り値;
// }

function getSeason(){
    const month = new Date().getMonth() + 1;
    if (month >= 3 && month <= 5) {
        return "spring";
    } else if (month >= 6 && month <= 8) {
        return "summer";
    } else if (month >= 9 && month <= 11) {
        return "autumn";
    } else {
        return "winter";
    }
}

const season = getSeason();
console.log(season);

//Q.実行したら戻り値20を返す関数"sonicboomを作成しなさい。
const sonicBoom = () => {
    return 20;
}
console.log(sonicBoom());

//アロー関数...javasprictの関数を短くシンプルにかける方法
//Q.引数 lastDamage を持ち、実行したらlastDamageに1.5をかけた値を
//戻り値として返す関数metalBurstを返しなさい
const metalBurst = (lastDamage) => {
    return lastDamage * 1.5;
}
console.log(metalBurst(50));
// function metalBurst (lastDamage) {
//     return lastDamage * 1.5;
// }

//Q.引数theirHpを持ち、実行したらtheirHpの値をそのまま戻り値として返す関数hornDrillを作成しなさい
//ただし成功確率は30％とし、失敗した場合は0を返すようにしなさい
const hornDrill = (theirHp) => {
    if (Math.random() <= 0.3){
        return theirHp;
    }else {
        return 0
    }
}

console.log(hornDrill(100));

//オブジェクト
// const オブジェクト名 ={
//     プロパティ名:値
// };
//let でもいいが constを使って定義することが多い
const snsUser ={
    id: 1,
    userName: "Taro",
    gender: "male",
    like: function(){

    },
    post: function (contents) {
        return contents + "を投稿しました。by" + this.userName;
    },
}

console.log(snsUser.post("プログラミングなう"));
//thisは利用シーンで参照するものが変わる、オブジェクト内で使えばオブジェクト自体を参照する。
//メソッドを定義する際はアロー関数ではなくfunctionで定義した関数を使う。

//Q.ピカチュウのオブジェクトをつくりなさい。含めるべきプロパティ↓
//name(文字列 -> "ピカチュウ")
//level(数字 -> 18)
//type(文字列の配列 -> 電気)
//skills(文字列の配列 -> 10万ボルト、でんこうせっか、たいあたり)

const pikachu = {
    name:"ピカチュウ",
    level: 18,
    types:["電気"],
    skills:["10万ボルト", "でんこうせっか", "たいあたり"],
    levelUp: function(){
        this.level++;
        if(this.level >= 20){
            this.skills.push("スパーク")
        }
    }

};
console.log(pikachu.skills);
console.log(pikachu.level);
pikachu.levelUp();
pikachu.levelUp();
console.log(pikachu.level);
console.log(pikachu.skills);

//標準組み込み関数標準組み込みオブジェクト
console.log(parseInt("2"));


const myPokemons = ["サンダー", "ホウオウ", "スイクン", "ラティアス", "パルキア"];
myPokemons.push("ミュウツー");
console.log(myPokemons.length);

const oldVersions =["赤", "緑", "青"];
const newVersions =["ルビー", "サファイア", "エメラルド"];

console.log(oldVersions.concat(newVersions));
//concatを使うと2つの配列を一つにまとめることができる

//ブラウザAPI jsを実行しwebページを操作できる。
// const timer = setTimeout(function(){
//     alert("Hello!")
// }, 5000);
// clearTimeout(timer);
//定数は大文字に
//true falseの変数はis◌◌
//二つ以上の英単語をつなげるばあい大文字にするpokemonName
//pythonだとpokemon_name

const $post = document.createElement("article");
$post.setAttribute("class", "post");
$post.innerText = "おなか減ったなう";

const $timeline = document.querySelectorAll(".timeline")[0];
$timeline.appendChild($post);

//イベント
//scroll resize 
//mouthover touchmove
window.addEventListener("load", function(){
    alert("読み込みかんりょう");
});
// document.querySelector("#button").addEventListener("click", function(){
//     console.log("clickされた");
// });
// document.querySelector("#button")
// .addEventListener("click",function(){
//     document.querySelector("#output")
//     .textContent = "ピカチュウ";
// });
document.querySelector("#button").addEventListener("click", function(){
    if(Math.random() <= 0.2){
        alert("ピカチュウをゲットした！");
    }else{
        alert("ざんねん！もうすこしでつかまえられたのに！");
    }
});
