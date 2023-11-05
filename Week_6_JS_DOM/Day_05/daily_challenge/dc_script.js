// Create a function that:

// takes in two strings as two parameters
// and returns a boolean that indicates whether or not the first string is an anagram of the second string.
// Some Help

// What is an anagram?
// An anagram is another word or phrase formed by rearranging letters of the first word or phrase.


// Example of anagrams

// "Astronomer" is an anagram of "Moon starer"
// "School master" is an anagram of "The classroom"
// "The Morse Code" is an anagram of "Here come dots"


// Do we need to consider whitespace?
// Trim whitespace prior to comparison.


function isAnagram(string1, string2) {
  let unify = (str) =>
    str.toLowerCase().replace(/[^a-z0-9]/g, "").split("").sort().join("");

  let sortedStr1 = unify(string1);
  let sortedStr2 = unify(string2);
  return sortedStr1 === sortedStr2;
}

const test1 = isAnagram("Astronomer", "Moon starer");
console.log(test1);
const test2 = isAnagram("School master", "The classroom");
console.log(test2);
const test3 = isAnagram("The Morse Code", "Here come dots");
console.log(test3);