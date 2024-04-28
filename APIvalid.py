import _Applier as app 
import sys
import os

project = sys.argv[1]
bugid = sys.argv[2]

# Apply patch
with open('patches/%s%s.txt' % (project,bugid),'r') as p:
    for line in p:
        file_path,lineid,patch =line.split(',',2)
        ori_file = os.path.basename(file_path)
        if not os.path.exists('tmp/%s%s/%s' % (project,bugid,ori_file)):
            os.system('cp %s tmp/%s%s/' % (file_path,project,bugid))
        with open(file_path,'r', encoding="latin-1") as f:
            src = f.readlines()
            src_app = app.applyPatch(src, patch, int(lineid))
            out_app = app.toSrc(src_app)
            f.close()
        
        #Write to file
        with open(file_path,'w', encoding="latin-1") as des_file:
            des_file.write(out_app)
            des_file.close()


        failing_test=os.popen('timeout -s 9 300 catena4j test -w 105_bugs_with_src/%s%s' % (project,bugid)).readlines()
        if not failing_test:
            with open('final/%s%s.txt' % (project,bugid),'at') as out:
                out.write('%s:%s:%s:Build Error\n' % (file_path,patch.strip(),lineid))
                out.close()
        elif failing_test[0].strip() == "Failing tests: 0":
            with open('final/%s%s.txt' % (project,bugid),'at') as out:
                out.write('%s:%s:%s:Pass\n' % (file_path,patch.strip(),lineid))
                out.close()
        else:
            with open('final/%s%s.txt' % (project,bugid),'at') as out:
                out.write('%s:%s:%s:Fail\n' % (file_path,patch.strip(),lineid))
                out.close()

        os.system('cp tmp/%s%s/%s  %s' % (project,bugid,ori_file,file_path))

    p.close()
