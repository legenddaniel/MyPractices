function convertToRoman(num) {

    const converter = [
        { 'M': 1000 },
        { 'D': 500 },
        { 'C': 100 },
        { 'L': 50 },
        { 'X': 10 },
        { 'V': 5 },
        { 'I': 1 }
    ];

    let cacheNum = num;
    const cacheRoman = [];
    let converterValue;

    for (let i = 0, l = converter.length; i < l; i++) {
        converterValue = Object.values(converter[i])[0];
        if (cacheNum >= converterValue) {
            cacheRoman.push(Object.keys(converter[i])[0]);
            cacheNum -= converterValue;
            i--;
        }
    }

    const replace = {
        'IIII': 'IV',
        'XXXX': 'XL',
        'CCCC': 'CD',
        'VIV': 'IX',
        'LXL': 'XC',
        'DCD': 'CM'
    }

    const Roman = cacheRoman.join('').replace(/IIII|XXXX|CCCC/g, (item) => replace[item]).replace(/VIV|LXL|DCD/g, (item) => replace[item])
    return Roman;
}

console.log(convertToRoman(649));
