class Solution {
  groupAnagrams(strs) {
    const dictionary = {};
    for (var i = 0; i < strs.length; i++) {
      let sorted_string = strs[i].split("").sort().join("");
      if (sorted_string in dictionary) {
        dictionary[sorted_string].push(strs[i]);
      } else {
        dictionary[sorted_string] = [strs[i]];
      }
    }
    return Object.values(dictionary);
  }
}

my_solution = new Solution();
strs = ["eat", "tea", "tan", "ate", "nat", "bat"];
console.log(my_solution.groupAnagrams(strs));
