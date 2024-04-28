import pandas as pd
from decimal import Decimal

class gzoltar:
    def clear_zero(self, file_dir):
        # file_dir = "/home/lxy/research/multi_location_bug_repair/NIChecker/SuspiciousCodePositions/Chart_15"
        new_file = []
        with open(file_dir + '/ranking.txt') as ranking:
            file_ranking = ranking.readlines()
            for line in file_ranking:
                line = line.replace("\n", "")
                rindex_jing = line.rindex("#")
                sedindex_dollar = line.find("$", line.index("$") + 1, len(line))
                if sedindex_dollar > 0 and sedindex_dollar < rindex_jing:
                    rindex_jing = sedindex_dollar
                java_class = line[0:rindex_jing]
                java_class = java_class.replace("$", ".")
                line_num = line[line.rindex(':') + 1:line.rindex(';')]
                score = line[line.rindex(';') + 1:]
                if (float(score) > 0):
                    new_file.append(java_class + "@" + line_num)
        # rank
        w_ranking = open(file_dir + '/ranking.txt', 'w')
        for i in new_file:
            w_ranking.write(i + '\n')
        w_ranking.close()

    def transfer_for_tbar(self, src_file, dst_file):
        new_file = []
        with open(src_file) as ranking:
            file_ranking = ranking.readlines()
            for line in file_ranking:
                line = line.replace("\n", "")
                rindex_jing = line.rindex("#")
                sedindex_dollar = line.find("$", line.index("$") + 1, len(line))
                if sedindex_dollar > 0 and sedindex_dollar < rindex_jing:
                    rindex_jing = sedindex_dollar
                java_class = line[0:rindex_jing]
                java_class = java_class.replace("$", ".")
                line_num = line[line.rindex(':') + 1:line.rindex(';')]
                score = line[line.rindex(';') + 1:]
                if (float(score) > 0):
                    new_file.append(java_class + "@" + line_num)
        # rank
        w_ranking = open(dst_file, 'w')
        for i in new_file:
            w_ranking.write(i + '\n')
        w_ranking.close()

    def transfer_for_simfix(self, src_file, dst_file):
        dic={}
        new_file = []
        with open(src_file) as ranking:
            file_ranking = ranking.readlines()
            for line in file_ranking:
                line = line.replace("\n", "")

                pkg,res = line.split('$',maxsplit=1)
                cls,res = res.split('#',maxsplit=1)
                func,res = res.split(':',maxsplit=1)
                lineNum,score = res.split(';',maxsplit=1)
                
                str_simfix = pkg + '.' + cls + '#' + lineNum + ',' + score
                dic[str_simfix] = Decimal(score)


            rank_list = pd.Series(dic)
            r_min = rank_list.rank(method="min",ascending=False)
            r_max = rank_list.rank(method="max",ascending=False)
            
            count = 0
            for key, value in dic.items():
                tmp = key+",("+ str(int(r_min[count]))+','+str(int(r_max[count]))+')'
                new_file.append(tmp)
                count = count + 1

        # save file
        w_ranking = open(dst_file, 'w')
        for i in new_file:
            w_ranking.write(i + '\n')
        w_ranking.close()
