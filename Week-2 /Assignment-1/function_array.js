// Assignment 1

// function max(numbers)

function max(numbers) {
    let max_value = 0;
    for (let i = 0; i < numbers.length; i += 1){  
        if(numbers[i] > max_value){
            max_value = numbers[i]
        }  
    }
    return max_value
}
console.log( max([1, 2, 4, 5]) ); // should print 5
console.log( max([5, 2, 7, 1, 6]) ); // should print 7


// function findPosition(numbers, target)

function findPosition(numbers, target) {
    whether = numbers.includes(target)
    for (let i = 0;i < numbers.length; i += 1){
        if (whether == false) {
            return -1;
            // break;
        }
        if (numbers[i] == target) {
            return i;
            // break;
        }
    }
}
console.log( findPosition([5, 2, 7, 1, 6], 5) ); // should print 0
console.log( findPosition([5, 2, 7, 1, 6], 7) ); // should print 2
console.log( findPosition([5, 2, 7, 7, 7, 1, 6], 7) ); // should print 2 (the first one) 
console.log( findPosition([5, 2, 7, 1, 6], 8) ); // should print -1

//Note
/*
// function max(numbers)
//function version
function max(numbers) {
    let max_value = 0;
    for (let i = 0; i < numbers.length; i += 1){  
        if(numbers[i] > max_value){
            max_value = numbers[i]
        }  
    }
    console.log(max_value)
}
console.log( max([1, 2, 4, 5]) ); // should print 5
console.log( max([5, 2, 7, 1, 6]) ); // should print 7

// NOT function version
numbers = [5, 2, 7, 1, 6]
let max_value = 0;
for (let i = 0; i < numbers.length; i += 1){  
    if(numbers[i] > max_value){
        max_value = numbers[i]
    }  
}
console.log(max_value)

// function findPosition(numbers, target)
// function version
function findPosition(numbers, target) {
    whether = numbers.includes(target)
    for (let i = 0;i < numbers.length; i += 1){
        if (whether == false) {
            console.log(-1)
            break;
        }
        if (numbers[i] == target) {
            console.log(i)
            break;
        }
    }
}

// NOT function version
numbers = [5, 2, 7, 1, 6]
whether = numbers.includes(8)
for (let i = 0;i < numbers.length; i += 1){
    if (whether == false) {
        console.log(-1)
        break;
    }
    if (numbers[i] == 8) {
        console.log(i)
        break;
    }
}

*/
