import apt_pkg

def main():
    print "Init..."
    apt_pkg.InitConfig()
    apt_pkg.InitSystem()
    print "Init cache..."

    cache = apt_pkg.GetCache()

    print "Start..."
    packages_all = sorted(cache.Packages, key=lambda pkg: pkg.Name)
    packages_installed = [pkg for pkg in packages_all \
            if pkg.CurrentState == apt_pkg.CurStateInstalled]
    print "number of all packages:      ", len(packages_all)
    print "number of installed packages:", len(packages_installed)

if __name__ == "__main__":
    main()
