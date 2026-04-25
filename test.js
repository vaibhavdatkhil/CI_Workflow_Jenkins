// Simple test case
console.log("Running test...");

function add(a, b) {
    return a + b;
}

const result = add(2, 2);

if (result === 4) {
    console.log("✅ Test Passed");
    process.exit(0);   // success
} else {
    console.log("❌ Test Failed");
    process.exit(1);   // fail
}