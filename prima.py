
def is_prime(num):
	if num < 2:
		return False
	for prime in range(2, num):
		if num % prime == 0:
			return False
	return True
	
def find_primes(max_num):
	primes = []
	for prime in range(0, max_num):
		if is_prime(prime):
			primes.append(prime)
			
	total_primes = str(len(primes))
	largest_prime = str(primes[-1]) 
	smallest_prime = str(primes[0]) 
	print('\n[+] total bilangan prima 1 s/d %s : %s' % (max_num, total_primes))
	print('[+] bilangan prima terbesar : %s' % (largest_prime))
	print('[+] bilangan prima terkecil : %s\n' % (smallest_prime))
	
	x = 0
	while x < len(primes):
		for value in primes:
			x = x + 1
			print(str(x)+' Yaitu : '+str(value))

if __name__ == '__main__':
	max = int(raw_input('[*] masukan nilai max : '))
	find_primes(max)