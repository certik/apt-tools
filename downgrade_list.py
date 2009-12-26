import apt_pkg

def version_too_high(pkg):
    version_installed = pkg.CurrentVer
    version_all = pkg.VersionList
    for v in version_all:
        if v.Downloadable and v.VerStr != version_installed.VerStr:
            return True
    return False

def install_ver(pkg):
    for v in pkg.VersionList:
        if v.Downloadable:
            return v.VerStr
    raise ValueError("Sorry")

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
    packages_downgrade = [pkg for pkg in packages_old \
            if version_too_high(pkg)]
    print "number of all packages:      ", len(packages_all)
    print "number of installed packages:", len(packages_installed)
    print
    print "List of unknown packages:"
    for pkg in packages_old:
        print pkg.Name,
    print
    print
    print "List of packages to downgrade:"
    for pkg in packages_downgrade:
        print pkg.Name,
    print
    print
    print "Command to downgrade the packages listed above:"
    print "sudo aptitude install",
    for pkg in packages_downgrade:
        print "%s=%s" % (pkg.Name, install_ver(pkg)),
    print


if __name__ == "__main__":
    main()
