# Killing a process using puppet

exec { 'killmenow':
    command => 'pkill -f killmenow',
    path    => ['/usr/bin'],
    returns => [0],
}