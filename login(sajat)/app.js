var userElem = document.getElementById("user");  
var jelszoElem = document.getElementById("jelszó");
var szamitGomb = document.getElementById("szamitGomb");
var belepesIn = document.getElementById("belepes");

szamitGomb.addEventListener('click', function (){ 
   

    let minta = /^[0-9a-zA-Zéáúőóüö'"+!%/=()]+$/; 
    if(userElem == jelszoElem) {  
        alert("Nem egyezhet a név és a jelszó!")
    }else{
        alert("A felhasználód elkészült!");
        return;
    }

    let anyag = Number(anyagStr);
    let reszecske = anyag * 6* Math.pow(10, 23);
    console.log(reszecske.toLocaleString()) 
    eredmenyIn.value = reszecske.toLocaleString();
});