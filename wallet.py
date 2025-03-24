import bdkpython as bdk

# Step 1: Generate a mnemonic
print("Generating mnemonic seed...")
mnemonic = bdk.Mnemonic(bdk.WordCount.WORDS12)
print(f"Mnemonic: {mnemonic}")

# Step 2: Create a descriptor secret key from the mnemonic
descriptor_secret = bdk.DescriptorSecretKey(
    network=bdk.Network.TESTNET, 
    mnemonic=mnemonic, 
    password=""
)

# Step 3: Extract the correct public key
descriptor_public = descriptor_secret.as_public()

# Step 4: Correct descriptor paths (BIP84 Native SegWit)
external_descriptor = bdk.Descriptor(
    f"wpkh({descriptor_public.as_string()}/84h/1h/0h/0/*)",  
    bdk.Network.TESTNET
)

change_descriptor = bdk.Descriptor(
    f"wpkh({descriptor_public.as_string()}/84h/1h/0h/1/*)",  
    bdk.Network.TESTNET
)

# Step 5: Initialize the wallet
wallet = bdk.Wallet(
    descriptor=external_descriptor, 
    change_descriptor=change_descriptor, 
    network=bdk.Network.TESTNET, 
    database_config=bdk.DatabaseConfig.MEMORY()
)

# Step 6: Generate 3 testnet addresses
print("\nGenerated Testnet Addresses:")
for i in range(3):
    address = wallet.get_address(bdk.AddressIndex.NEW).address
    print(f"Address {i+1}: {address}")
