Exec {
  path => ['/bin', '/sbin', '/usr/bin', '/usr/local/bin', '/usr/sbin'],
}

exec { "apt-update":
    command => "/usr/bin/apt-get update"
}

Exec["apt-update"] -> Package <| |>

$packages = hiera('common_packages')

package { $packages:
  ensure => present,
}

include pg_sql

