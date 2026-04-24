class Solution:
    def simplifyPath(self, path: str) -> str:
        # RULES:
            # . is cwd
            # .. is pwd
            # anything more than / (so basically all `/`) are treated like a single /
            # anything more than two dots is treated as a file entry `...` ex


        # output:
            # path is absolute and starts with /
            # dirs are separated with / (think of returning a join!)
            # no ending with / unless a root dir( "/" + "/".join(entries))
            # remove all of the single or double periods!!!

        
        # parse the / out of there to get the entries
        
        # use a stack and follow conventions for removing parent and cwd entries!

        # treat the raw entries like our stream 
        raw_entries = list(filter(lambda x: x, path.split("/")))

        # init a stack to use to traverse up and down the file tree
        s = []

        for ent in raw_entries:
            if ent == '.':
                continue
            elif ent == '..':
                if len(s) > 0:
                    s.pop()
            else:
                s.append(ent)

        return '/' + '/'.join(s)


