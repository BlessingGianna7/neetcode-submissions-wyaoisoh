class Solution:
  def validPalindrome(self, string):
    l = 0
    r = len(string) - 1

    while l < r:
        if string[l] != string[r]:
            return self.check(string, l+1, r) or self.check(string, l, r-1)

        l += 1
        r -= 1

    return True

  def check(self,string, l, r):
    while l < r:
        if string[l] != string[r]:
            return False
        l += 1
        r -= 1
    return True