import hashlib
import base64
import os

class Bcrypt:
    @staticmethod
    def hashpw(password, rounds=12):
        # Generate a salt
        salt = os.urandom(16)
        
        # Hash the password using SHA-256
        hashed_password = hashlib.sha256(password.encode('utf-8')).digest()
        
        # Iteratively hash using bcrypt's modified EksBlowfishSetup
        derived_key = b''
        for _ in range(rounds):
            derived_key = hashlib.sha256(derived_key + salt + hashed_password).digest()
        
        # Format the output as a bcrypt hash
        output = b'$2b$' + str(rounds).encode('utf-8') + b'$' + base64.b64encode(salt + derived_key).rstrip(b'=')
        
        return output.decode('utf-8')

    @staticmethod
    def checkpw(password, hashed_password):
        # Extract salt and derived key from the hashed password
        decoded_hash = base64.b64decode(hashed_password.encode('utf-8'))
        rounds = int(decoded_hash[4:6])
        salt = decoded_hash[7:29]
        derived_key = decoded_hash[29:]

        # Hash the provided password using the same method
        test_hash = Bcrypt.hashpw(password.encode('utf-8'), rounds=rounds).encode('utf-8')

        # Compare the generated hash with the provided hashed password
        return hashed_password.encode('utf-8') == test_hash

# Example usage
password = "my_secure_password"
hashed_password = Bcrypt.hashpw(password)
print("Hashed Password:", hashed_password)

# Check if a password matches the hashed version
is_matched = Bcrypt.checkpw(password, hashed_password)
print("Password Matched:", is_matched)
