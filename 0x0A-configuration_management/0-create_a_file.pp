# This Puppet manifest creates a file at /tmp/school with specific properties:
# - File path: /tmp/school
# - File permission: 0744
# - File owner: www-data
# - File group: www-data
# - File content: "I love Puppet"

file { '/tmp/school':
  ensure  => file,
  content => 'I love Puppet',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
}
