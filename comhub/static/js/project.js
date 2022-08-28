/* Project specific Javascript goes here. */
var email_field = $('#id_email'),
    username_field = $('#id_username');

$(email_field).change(function (e) { 
    var username_text = e.target.value.split("@")[0];
    username_field.val(username_text)
});