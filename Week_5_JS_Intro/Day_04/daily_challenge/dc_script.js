// Instructions
// Create a variable called sentence. The value of the variable should be a string that contains the words “not” and “bad”.
// For example, “The movie is not that bad, I like it”.

let sentence = "This dinner is bad!"

// Create a variable called wordNot where it’s value is the first appearance (ie. the position) 
// of the substring “not” (from the sentence variable).

let wordNot = sentence.indexOf("not")
console.log(wordNot)

// Create a variable called wordBad where it’s value is the first appearance (ie. the position) 
// of the substring “bad” (from the sentence variable).

let wordBad = sentence.indexOf("bad")
console.log(wordBad)

// If the word “bad” comes after the word “not”, you should replace the whole “not…bad” substring with “good”, 
// then console.log the result.

if (sentence.includes("not") && sentence.includes("bad") && wordBad > wordNot) {
    let stringToReplace = sentence.slice(wordNot, wordBad + 3);
    let newSentence = sentence.replace(stringToReplace, "good");
    console.log(newSentence);    
} else {
    console.log(sentence);
}

// For example, the result here should be : “The movie is good, I like it”
// If the word “bad” does not come after “not” or the words are not in the sentence, console.log the original sentence.
// Example:

//   Your string is : 'This dinner is not that bad ! You cook well', 
//   --> the result is : 'This dinner is good ! You cook well'

//   Your string is : 'This movie is not so bad !' 
//   --> the result is : 'This movie is good !'

//   Your string is : 'This dinner is bad !' 
//   --> the result is : 'This dinner is bad !'

// Instructions
// Write a JavaScript program that recreates the pattern below.
// Do this challenge twice: first by using one loop, then by using two nested for loops 
// (Nested means one inside the other - check out this tutorial of nested loops).
// Do this Daily Challenge by yourself, without looking at the answers on the internet.
// *  
// * *  
// * * *  
// * * * *  
// * * * * *
// * * * * * *

// let star = ""
// for (let iteration = 1; iteration < 7; iteration++) {
//     star += "* ";
//     console.log(star);
// }


// let starNew = "* "
// for (let iteration = 1; iteration < 7; iteration++) {
//     console.log(starNew.repeat(iteration));
// }

let stars = "";
for (let iteration = 1; iteration < 7; iteration++) {
    for (let nestIteration = 1; nestIteration <= iteration; nestIteration++) {
        stars += "* ";
    }
    stars += "\n";
}
console.log(stars);