# Installing a package using puppet
package { 'flask' :
  name = 'flask',
  command = 'pip3 install flask==2.1.0'
}
