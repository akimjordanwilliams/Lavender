const web3 = require("@solana/web3.js");

// Define network connection
const network = "<NETWORK_URL>";
const connection = new web3.Connection(network);

// Assuming you have the sender's private key array
// Example: const senderPrivateKey = [/* array of numbers representing the private key */];
const fromKeypair = web3.Keypair.fromSecretKey(new Uint8Array(senderPrivateKey));

// For the receiver, you would typically use their public key instead of generating a new keypair
const toPublicKey = new web3.PublicKey("<RECEIVER_PUBLIC_KEY>");

// Get blockhash
const { blockhash } = await connection.getLatestBlockhash();

// Create transaction
const transaction = new web3.Transaction({
    feePayer: fromKeypair,
    recentBlockhash: blockhash
});

// Add transaction instructions
transaction.add(
  web3.SystemProgram.transfer({
    fromPubkey: fromKeypair.publicKey,
    toPubkey: toKeypair.publicKey,
    lamports: 1
  })
);

const { signature } = await window.coinbaseSolana.signAndSendTransaction(transaction);