$(document).ready(() => {
    //Delete icon function
    const deleteIcons = [$('#deleteIconWhat'), $('#deleteIconWhere')];
    for (let deleteIcon of deleteIcons) {
        deleteIcon.mousedown(function() {
            $(this).prev().val('');
        })
    }

    //const prev() = next() = $(this).siblings('deleteIcon'/'inputBox')

    //Delete icon show/hide
    const inputBoxes = [$('#inputBoxWhat'), $('#inputBoxWhere')];
    for (let inputBox of inputBoxes) {
        inputBox.keyup(function() {
            if ($(this).val() !== '') {
                $(this).next().show();
            } else {
                $(this).next().hide();
            }
        });
        inputBox.blur(function() {
            $(this).next().hide();
        });
        inputBox.focus(function() {
            if ($(this).val() !== '') {
                $(this).next().show();
            };
        });
    }

    //Without issue of 'this' we can use arrow function
    $('#switchToFrench').click(() => alert('French version is provided by Indeed instead of my coding'));
});