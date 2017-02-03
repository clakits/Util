import os

n = 1

while n < 4:
    f = open("mkdocs.yml","w")
    f.write("# BEGIN ANSIBLE MANAGED BLOCK\n")
    f.write("site_name: LTRACI-2800 Pod %s\n" % n)
    f.write("pages:\n")
    f.write(" - Introduction: 'LTRACI-2800_pod%s/Introduction.md'\n" % n)
    f.write(" - Getting Started: 'LTRACI-2800_pod%s/Getting_Started.md'\n" % n)
    f.write(" - Pre Exercise Verification: 'LTRACI-2800_pod%s/Pre_Exercise_Verification.md'\n" % n)
    f.write(" - Lab 1: 'LTRACI-2800_pod%s/Lab_1.md'\n" % n)
    f.write(" - Lab 2: 'LTRACI-2800_pod%s/Lab_2.md'\n" % n)
    f.write(" - Lab 3: 'LTRACI-2800_pod%s/Lab_3.md'\n" % n)
    f.write("docs_dir: output_docs\n")
    f.write("# END ANSIBLE MANAGED BLOCK\n")
    f.close()
    os.system("mkdocs build")
    os.system("sleep 5")
    os.system("ls site/*")
    os.system("ditto site/LTRACI-2800_pod%s ALLSITES/LTRACI-2800_pod%s" %(n,n))
    n = n + 1
