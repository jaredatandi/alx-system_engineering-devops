# Installing a package using puppet
package { 'flask':
  ensure  => '2.1.0',
  name    => 'flask',
  command => 'pip3 install flask==2.1.0'
}
