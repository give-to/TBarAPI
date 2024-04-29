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
        # 保存文件
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
        # 保存文件
        w_ranking = open(dst_file, 'w')
        for i in new_file:
            w_ranking.write(i + '\n')
        w_ranking.close()

    def transfer_for_alpharepair(self, src_file, dst_file):
        new_file = []
        with open(src_file) as ranking:
            file_ranking = ranking.readlines()
            for line in file_ranking:
                line = line.strip()
                rindex_jing = line.rindex("#")
                method_name = line[rindex_jing:line.index("(") + 1]
                sedindex_dollar = line.find("$", line.index("$") + 1, len(line))
                if sedindex_dollar > 0 and sedindex_dollar < rindex_jing:
                    rindex_jing = sedindex_dollar
                java_class = line[0:rindex_jing]
                java_class = java_class.replace("$", ".")
                line_num = line[line.rindex(':') + 1:line.rindex(';')]
                score = line[line.rindex(';') + 1:]
                if (float(score) > 0):
                    new_file.append(java_class + "#" + line_num)
        # 保存文件
        w_ranking = open(dst_file, 'w')
        for i in new_file:
            w_ranking.write(i + '\n')
        w_ranking.close()
