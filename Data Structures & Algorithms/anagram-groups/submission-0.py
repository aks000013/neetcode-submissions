class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map = {}
        
        for word in strs:
            sorted_word = tuple(sorted(word))
            
            if sorted_word not in ana_map:
                ana_map[sorted_word] = []
                
            ana_map[sorted_word].append(word)
            
        return list(ana_map.values())