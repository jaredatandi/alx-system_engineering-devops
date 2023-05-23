file { '/home/0addd783f77a':
	ensure => present,
	source => 'puppet:/home/user/Documents/code/alx-system_engineering-devops/0x12-web_stack_debugging_2/0-iamsomeoneelse'
	mode => '0755',
	owner => 'root',
	group => 'root',
}
