class Solution {
    public int firstMissingPositive(int[] nums) {
         int i = 0;
            while (i < nums.length) {
                if (nums[i] > 0 && nums[i] != i + 1 && nums[i] - 1 < nums.length && nums[i] != nums[nums[i] - 1]) {
                    swap(nums, i, nums[i] - 1);
                } else {
                    i++;
                }
            }

            for (int j = 0; j < nums.length; j++) {
                if (nums[j] != j + 1) {
                    return j + 1;
                }
            }

            return nums.length + 1;
        }
//swap
        void swap(int[] nums, int i, int j) {
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }
    }
    