class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        ana_map ={}
        for i in range(len(strs)):
            freq_arr = [0] * 26
            for j in strs[i]:
                index = ord(j) - ord('a')
                freq_arr[index] = freq_arr[index] + 1
            key = tuple(freq_arr)
            if key in ana_map:
                ana_map[key].append(strs[i])
            else:
                ana_map.setdefault((key), []).append(strs[i])
        answer = [val for val in ana_map.values()]
        return answer

                # hamp[len(strs[i])] = hmap[len(strs[i])].append[strs[i]]
        


            