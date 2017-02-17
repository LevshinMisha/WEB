messages_count = 0;
already_delete = false
animation_is_over = true

function ajax(url, onComplete)
{
    $.get(url).done(onComplete).fail(function(xhr, status, errorText) { alert(errorText) });
}

function addMessageToChat(message)
{
    animation_is_over = false
    $('#chat').append('<div class="message">' + message + '</div>');
    if (messages_count < 10)
        $('.message:last').fadeIn(1000);
    else
        $('.message:last').slideDown(1000);
    messages_count++;
    if (messages_count > 10)
        deleteFirstMessage()
    setTimeout(function() { animation_is_over = true;  }, 1000)
}

function deleteFirstMessage()
{
    if (already_delete)
        $('.message:first').remove();
    already_delete = true;
    $('.message:first').slideUp(1000);
}

function addMessagesToChat(data)
{
    JSON.parse(data).forEach(addMessageToChat)
}

function buttonOnClick()
{
    if (animation_is_over)
    {
        var text = $('#text').val()
        ajax('addMessage/' + text, addMessageToChat(text));
    }
}

function main()
{
    $('button').click(buttonOnClick);
    ajax('messages', addMessagesToChat);
}

$(main);