# Using Puppet, this is a manifest that kills a process named killmenow
# use the exec and using pkill
exec{ 'killmenow':
  command  => 'pkill killmenow',
  provider => 'shell',
  path     => '/usr/bin/',
}
