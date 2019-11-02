$(document).ready(() => {
    $('.deleteIcon').click(() => {
        $('.deleteIcon').siblings('input').text('');
    });
    $('#inputBoxWhat').keyup(() => {
        if ($('#inputBoxWhat').val() !== '') {
            $('.deleteIcon:first').show();
        } else {
            $('.deleteIcon:first').hide();
        }
    });
    $('#inputBoxWhat').blur(() => $('.deleteIcon:first').hide());
    $('#inputBoxWhat').focus(() => {
        if ($('#inputBoxWhat').val() !== '') {
            $('.deleteIcon:first').show();
        };
    });
    
    $('#inputBoxWhere').keyup(() => {
        if ($('#inputBoxWhere').val() !== '') {
            $('.deleteIcon:eq(1)').show();
        } else {
            $('.deleteIcon:eq(1)').hide();
        }
    });
    $('#inputBoxWhere').blur(() => $('.deleteIcon:eq(1)').hide());
    $('#inputBoxWhere').focus(() => {
        if ($('#inputBoxWhere').val() !== '') {
            $('.deleteIcon:eq(1)').show();
        };
    });

    $('#switchToFrench').click(() => alert('French version is provided by Indeed instead of my coding'));
});