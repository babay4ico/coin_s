derived_key = bip32_ctx.DerivePath(sol_path)

private_key_bytes = derived_key.PrivateKey().Raw().ToBytes()[:32]

signing_key = nacl.signing.SigningKey(private_key_bytes)

public_key_bytes = signing_key.verify_key.encode()

solana_private_key_64 = private_key_bytes + public_key_bytes

solana_address = base58.b58encode(public_key_bytes).decode()

print("Private key (64-byte, base58 like Phantom):", base58.b58encode(solana_private_key_64).decode())
print("Solana address:", solana_address)
