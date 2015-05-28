class pg_sql {

    $pg_values = hiera('postgresql')

    class { 'postgresql::globals':
      encoding            => 'UTF-8',
      locale              => 'en_US.UTF-8',
      manage_package_repo => true,
      version             => '9.3',
    }->

    class { 'postgresql::server':
      ip_mask_deny_postgres_user => '0.0.0.0/32',
      ip_mask_allow_all_users => '0.0.0.0/0',
      listen_addresses        => $pg_values['bind_address'],
      postgres_password       => $pg_values['root_pass'],
    }

    postgresql::server::role { $pg_values['user']:
      password_hash => postgresql_password($pg_values['user'], $pg_values['pass']),
      createdb      => true,
      superuser     => true
    }

    $db_options = {
        user => $pg_values['user'],
        password => $pg_values['pass'],
    }

    create_resources(pg_db, $pg_values['databases'], $db_options)

    define pg_db (
      $user,
      $password,
      $grant    = 'ALL',
      $sql_file = false
    ) {

        postgresql::server::database { $name:
        }

        postgresql::server::database_grant { $name:
          privilege => $grant,
          db        => $name,
          role      => $user,
        }
    }
}
