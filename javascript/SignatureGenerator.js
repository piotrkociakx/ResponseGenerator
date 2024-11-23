function get(number) {
    let sum = 0;
    while (number > 0) {
        sum += number % 10;
        number = Math.floor(number / 10);
    }
    return sum;
}

function generate() {
    const nowDarwin = new Date().toLocaleString("en-AU", { timeZone: "Australia/Darwin" });
    const now = new Date(nowDarwin);
    const x = now.getMinutes();
    const result = (x + 30) + (x - 15) + (x * 2) + get(x);

    return result;
}