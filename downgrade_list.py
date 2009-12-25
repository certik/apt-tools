import apt_pkg

def version_too_high(pkg):
    version_installed = pkg.CurrentVer
    version_all = pkg.VersionList
    if len(version_all) > 1:
        print pkg.Name
        print "installed version:", version_installed.VerStr
        print "all versions:"
        for v in version_all:
            print " ", v.VerStr, v.Downloadable
        print "downloadable:", version_installed.Downloadable
        stop

def downloadable(pkg):
    version_installed = pkg.CurrentVer
    return version_installed.Downloadable == 1

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
    packages_old = [pkg for pkg in packages_installed \
            if not downloadable(pkg)]
    #packages_downgrade = [pkg for pkg in packages_installed \
    #        if version_too_high(pkg)]
    print "number of all packages:      ", len(packages_all)
    print "number of installed packages:", len(packages_installed)
    for pkg in packages_old:
        print pkg.Name


if __name__ == "__main__":
    main()
