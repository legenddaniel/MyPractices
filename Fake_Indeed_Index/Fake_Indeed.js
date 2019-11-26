// As I mentioned in the html document, delete-icon functions are not required since <input type='search'> can do the same thing

$(() => {
    // Delete-icon function
    $('.delete-icon').mousedown(function () {
        $(this).prev().val('');
    })

    // const prev() = next() = $(this).siblings('deleteIcon'/'inputBox')

    // Delete-icon show/hide
    $('.inputbox').keyup(function () {
        $(this).val() !== '' ? $(this).next().show() : $(this).next().hide();
    });
    $('.inputbox').blur(function () {
        $(this).next().hide();
    });
    $('.inputbox').focus(function () {
        if ($(this).val() !== '') {
            $(this).next().show();
        };
    });

    // Without issue of 'this' we can use arrow function, but would better unify the format (ES5/ES6)
    $('.french').on('click', () => alert('French version is provided by Indeed instead of my coding'));
});