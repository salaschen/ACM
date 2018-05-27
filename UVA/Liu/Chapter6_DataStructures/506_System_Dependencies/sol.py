'''
System Dependencies, ACM/ICPC World Finals 1997.
Date: 27/May/2018
Lang: Python3
'''
class Solution:
    def __init__(self):
        self.Installed = [] ; 
        self.Depend = dict() ; 
        self.Support = dict() ; 
        self.Explicit = dict() ; 

    def work(self):
        command = input(); 
        while command != "END":
            self.handle(command) ; 
            command = input() ;
        print("END") ; 
        return ; 

    def DependAdd(self, command):
        line = command.split() ; 
        usrapp = line[1] ; 
        if usrapp in self.Depend.keys(): # error
            print("ERROR: double depend entry for " + usrapp) ;
            return ; 
        self.Depend[usrapp] = [] ;
        for i in range(2, len(line)):
            libapp = line[i] ;
            self.Depend[usrapp].append(libapp) ; 
            if libapp in self.Support.keys():
                self.Support[libapp].append(usrapp) ; 
            else:
                self.Support[libapp] = [usrapp] ; 
        return ; 

    def InstallApp(self, command):
        line = command.split(); 
        app = line[1] ; 
        if app in self.Installed:
            print("{1}{0} is already installed.".format(app, ' '*3)) ; 
            return ; 
        else:
            self.Explicit[app] = True ; 
            self.TryInstall(app) ; 
        return ;

    def TryInstall(self, app):
        # try install all the dependent apps first
        if app in self.Installed:
            return ; 
        if app in self.Depend.keys():
            for dependApps in self.Depend[app]:
                self.TryInstall(dependApps) ; 
        print("{1}Installing {0}".format(app, ' '*3)) ; 
        self.Installed.append(app) ; 
        return ; 
        
    def RemoveApp(self, command):
        line = command.split() ; 
        app = line[1] ;
        if app not in self.Installed:
            print("{1}{0} is not installed.".format(app, ' '*3)) ; 
            return ;
        elif app in self.Support.keys() and self.GetNumAppSupporting(app) > 0:
            print("{1}{0} is still needed.".format(app, ' '*3)) ; 
            return ; 
        else:
            self.Explicit[app] = False ; 
            self.TryRemove(app) ; 
        return ;
    
    def TryRemove(self, app):
        if app not in self.Installed:
            return ;
        elif app in self.Explicit and self.Explicit[app]:
            # do not remove explicity installed apps implicitly
            return ; 
        else:
            self.Installed.remove(app) ;
            print("{1}Removing {0}".format(app, ' '*3)) ; 
            if app in self.Depend.keys():
                for dApp in self.Depend[app]:
                    if self.GetNumAppSupporting(dApp) == 0:
                        self.TryRemove(dApp) ; 
        return ; 

    def GetNumAppSupporting(self, app):
        if app not in self.Support.keys():
            return 0;
        else:
            result = 0 ; 
            for sapp in self.Support[app]:
                if sapp in self.Installed:
                    result +=1 ; 
        return result ; 

    def handle(self, command):
        # handle command
        print(command) ; # echo the command

        # debug prints

        #print('\nInstalled: ',self.Installed) ;
       # print('Depend: ', self.Depend) ; 
       # print('Support: ', self.Support) ; 

        line = command.split() ; 
        if line[0] == "LIST":
            self.ListApps() ;
        elif line[0] == "DEPEND":
            self.DependAdd(command) ;
        elif line[0] == "INSTALL":
            self.InstallApp(command) ; 
        elif line[0] == "REMOVE":
            self.RemoveApp(command) ; 
        else:
            print("[ERROR]:Something wrong with (" + command + ")") ; 
        return ;

    def ListApps(self):
        for i in range(0, len(self.Installed)):
            print("{1}{0}".format(self.Installed[i], ' '*3)) ; 
        return ; 
    

########### END of SOLUTION ###########3
        
def main():
    s = Solution() ; 
    s.work(); 

if __name__ == "__main__":
    main() ;

