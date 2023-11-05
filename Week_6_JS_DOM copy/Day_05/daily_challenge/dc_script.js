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
  const unify = (str) =>
    str
      .toLowerCase()
      .split("")
      .sort()
      .join("");

  const sortedStr1 = normalize(str1);
  const sortedStr2 = normalize(str2);

  return sortedStr1 === sortedStr2;
}

// Example usage:
const result1 = isAnagram("Astronomer", "Moon starer");
const result2 = isAnagram("School master", "The classroom");
const result3 = isAnagram("The Morse Code", "Here come dots");

console.log(result1);
console.log(result2);
console.log(result3);