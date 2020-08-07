class Solution(object):

  def lengthLongestPath(self, input):
    """
    :type input: str
    :rtype: int
    """
    a = input.split("\n")
    current_path = []
    max_length = 0
    for i, t in enumerate(a):
      split = t.split("\t")
      n_tabs = len(split)-1

      if n_tabs < len(current_path):
        current_path = current_path[:n_tabs]
      current_path.append(split[-1])

      current_length = len("/".join(current_path))
      if "." in split[-1]:
        if current_length > max_length:
          max_length = current_length
        current_path = current_path[:-1]
    return max_length


a = Solution()
result = a.lengthLongestPath(
    "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext")
print(result)
