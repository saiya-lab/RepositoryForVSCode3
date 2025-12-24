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
