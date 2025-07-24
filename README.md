# Cooking with Hash: Slicing, Dicing, and Mixing Data

A hash function is any function that takes an input of arbitrary length-a word, a file, or an entire dataset—and transforms it into a fixed-length string of bytes.
We call the input the has pre-image and the output of the function the hash value or digest.
No matter how big or small the original data, the output always has the same size (for example, 32 bytes in the case of SHA-256).

Hash functions are everywhere in computer science and cryptography.
We use them to create fingerprints of data for quick comparison, to check file integrity, to organize data in hash tables, and, crucially in cryptography, to commit to a secret—that is, to prove you know something without revealing it.

For many of these applications, especially in cryptography, it’s not enough for a hash function to just scramble data.
A good hash function must resist several types of attacks:

- Collision resistance: It should be practically impossible to find two different inputs that produce the same hash output.
- Pre-image resistance: Given a hash output, it should be infeasible to figure out what input produced it.
If a hash function is vulnerable to these attacks, it can’t be safely used for cryptographic purposes, as attackers could break commitments, forge digital fingerprints, or violate the security of protocols that rely on hashes.

In this assignment, you’ll experiment with toy hash functions to discover how and why these properties matter—and what can go wrong if they aren’t satisfied.

## Expected submissions

Explain how to submit the work.

## Scavenger hunt questions

### When two bytes collide: cryptanalysis of a weak hash funtion

Consider the hash function given in [functions/hash0.py](functions/hash0.py) that produces 32-bit digests.
You are supposed to analyze this hash function and produce the following attacks.
It is simple enough for you do do it by hand, you don't need to brute force anything (we are going to do that later on).

1. Calculate two different strings that will hash to the same value. 
Both strings should be composed of ascii characters and be 8 characters long (64 bits). 

We call this a collision attack.
If it's easy to find collisions for a hash function, it can't be trusted as a unique fingerprint of data, i.e., we can't use digests to identify or commit to data.

2. Calculate an input string that will have exactly the same hash as the input "bitcoin".

We call this a second pre-image attack.
Second pre-image resistance is crucial for integrity: if someone can create a different message with the same hash, they could replace legitimate data (documents, transactions, etc.) with malicious data that appears to be identical as far as the hash is concerned.
This property is especially important in digital signatures and commitment schemes.
For example, if you sign a document by signing its hash, you want to be sure nobody can forge a different document with the same hash (and thus the same signature).

3. Calculate an input string that will have exactly the hash `631a000d`.

We call this a first pre-image attack, i.e., we can construct the pre-image for a given hash.
If a hash function is not pre-image resistant, an attacker could “reverse” a hash value to recover or forge a message.
This would break the use of hashes for commitments (proving you knew a value without revealing it) or for securely storing passwords (as a hash could be reversed to recover the password).

Note that in the previous exercise you know the pre-image you want to attack and can use it as a starting point to mangle with since you know the structure of the hash function.
Here, you don't have an obvious starting point. 

### Brute forcing is always an option

For the next exercises, consider the function given in [functions/hash1.py](functions/hash1.py) that also produces 32-bits digests.
This is still an insecure function, but it's algebraic structure is a bit more complicated to render cryptanalysis infeasible for the scope of this course.
Yet, we can always brute force it, i.e., try many combinations of inputs and search for a conveniente output.
This is because the search space is quite small since 32-bits will render around 4 billion possible outputs, something that any modern computer can generate in a few minutes (if not seconds if properly implemented).

For the next exercises, you are expected to brute force the solutions.
Expect to let your program run for a few minutes if you are using a multicore solution or a few hours for single core.

4. Calculate two different strings that will hash to the same value. 
Both strings should be composed of ascii characters and be 8 characters long (64 bits).

5. Calculate an input string that will have exactly the same hash as the input "bitcoin".

6. Calculate an input string that will have exactly the hash `631a000d`.

### Constructions with hashes

7. Check the inclusion of a hash in a merkle tree.
We give the merkle root, a pre-image and the proofs.

8. Compute a partial collision: hash-cash style proof of work.

## Example:

*How many transactions are confirmed in block 666,666?*

Using local full node (or with proxy settings in `bitcoin.conf`):

```sh
hash=$(bitcoin-cli getblockhash 666666)
block=$(bitcoin-cli getblock $hash)
echo $block | jq .nTx
```

``` sh
$ bash solution.sh
2728
```
