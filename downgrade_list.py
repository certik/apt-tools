import apt_pkg

def version_too_high(pkg):
    version_installed = pkg.CurrentVer
    version_all = pkg.VersionList
    if len(version_all) > 1:
        print pkg.Name
        print "installed version:", version_installed.VerStr
        print "all versions:"
        for v in version_all:
            print " ", v.VerStr
        print "downloadable:", version_installed.Downloadable

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
    packages_downgrade = [pkg for pkg in packages_installed \
            if version_too_high(pkg)]
    print "number of all packages:      ", len(packages_all)
    print "number of installed packages:", len(packages_installed)


if __name__ == "__main__":
    main()
