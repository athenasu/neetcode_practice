class Solution {
  twoSum(nums, target) {
    const hashmap = {};
    for (var i = 0; nums.length; i++) {
      const diff = target - nums[i];
      if (diff in hashmap) {
        return [hashmap[diff], i];
      } else {
        hashmap[nums[i]] = i;
      }
    }
    return [];
  }
}

const my_solution = new Solution();
nums = [1, 2, 5, 8];
target = 10;
console.log(my_solution.twoSum(nums, target));
