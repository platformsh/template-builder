class ReadmeMixin:
    readMeFileName = "README"
    readMeFileExt = "md"
    readMeUpstreamFile = "_UPSTREAM"
    readMePSHFile = "_PSH"

    def rename_psh_readme(self):
        return 'cd {0} && if [[ -f "{1}.{2}" ]]; then echo "Moving {1}.{2} to {1}{3}.{2}"; mv "{1}.{2}" "{1}{3}.{2}";' \
               'fi;'.format(self.builddir, self.readMeFileName, self.readMeFileExt, self.readMePSHFile)

    def rename_psh_readme_back(self):
        return 'cd {0} && if [[ -f "{1}{3}.{2}" ]]; then echo "Moving our {1}{3}.{2} back to {1}.{2}";mv "{1}{3}.{2}" '\
               '"{1}.{2}";fi;'.format(self.builddir,self.readMeFileName,self.readMeFileExt,self.readMePSHFile)

        # return 'cd {0} && if [[ -f "{1}{3}.{2}" ]]; then echo "Moving our {1}{3}.{2} back to {1}.{2}";mv "{1}{3}.{2}" '\
        #        '"{1}.{2}";git add {1}.{2};git commit -m "Committing our {1}.{2}";fi;'.format(self.builddir,
        #                                                                                      self.readMeFileName,
        #                                                                                      self.readMeFileExt,
        #                                                                                      self.readMePSHFile)

    def rename_upstream_readme(self):
        return 'cd {0} && if [[ -f "{1}.{2}" ]]; then echo "moving upstream {1}.{2} to {1}{3}.{2}";mv "{1}.{2}" "{1}{' \
               '3}.{2}";fi;'.format(self.builddir,self.readMeFileName,self.readMeFileExt,self.readMeUpstreamFile)
        # return 'cd {0} && if [[ -f "{1}.{2}" ]]; then echo "moving upstream {1}.{2} to {1}{3}.{2}";mv "{1}.{2}" "{1}{' \
        #        '3}.{2}"; git add "{1}{3}.{2}";git commit -m "renamed {1} to {1}{3}";fi;'.format(self.builddir,
        #                                                                                         self.readMeFileName,
        #                                                                                         self.readMeFileExt,
        #                                                                                         self.readMeUpstreamFile)
