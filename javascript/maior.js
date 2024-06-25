function maior(){
    let n = 2
    let p = 1

    if (n>p){
        return `O número ${n} é maior que ${p}.`
    } else{
        return `O número ${p} é maior que ${n}.`
    }
}

//Esse é u jeito, porem não muito prático;

function pratico(){
    let cu = [1, 2, 4, 5]
    

    return cu.indexOf(2)
}

console.log(pratico())