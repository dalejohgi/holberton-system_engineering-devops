#Configure broader limits
exec { 'change-os-configuration-for-holberton-user':
  command => "/bin/sed -i -e 's/nofile 5/nofile 1000/g;s/nofile 4/nofile 1000/g' /etc/security/limits.conf"
}