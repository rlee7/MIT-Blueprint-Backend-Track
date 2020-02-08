
$(document).ready(function () {

    $("#submit").click(function () {
        const message = $("#message").val();
        console.log(message);
        $.post('/message', {
            message: message
        }).done(function () {
            document.location.reload();
        });
    });

});