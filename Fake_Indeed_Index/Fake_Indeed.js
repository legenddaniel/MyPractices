//With content: r/w changes, unfocus restores
//Without content: no change
//Icon with link but failed
```if (document.getElementById('inputBoxWhat') != '') {
    document.getElementById('inputBoxWhat').onchange = () => document.getElementsById('noDeleteIconWhat').id = 'deleteIconWhat';
    document.getElementById('inputBoxWhat').onblur = () => document.getElementsById('deleteIconWhat').id = 'deleteIconWhat';
}```

```const defaultSubmit = () => {
    const [inputWhat, inputWhere] = [document.getElementById('q').replace(/s+/g, ''), document.getElementById('l').replace(/s+/g, '')];
    if (!inputWhat.value && !inputWhere.value) {
        inputWhat.value = inputWhat.placeholder;
        inputWhere.value = inputWhere.placeholder;
    }
    return inputWhat.value, inputWhere.value;
}```//bug, submit info in placeholder by default

document.getElementById('switchToFrench').onclick = () => alert('French version is provided by Indeed instead of my coding');